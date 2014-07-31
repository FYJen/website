import argparse
import imp
import sys
import os.path

from migrate.versioning import api
from db_config import SQLALCHEMY_DATABASE_URI
from db_config import SQLALCHEMY_MIGRATE_REPO
from app import db


def _creatDB(dryrun):
    db.create_all()
    if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
        api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
        api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
    else:
        api.version_control(SQLALCHEMY_DATABASE_URI,
                            SQLALCHEMY_MIGRATE_REPO,
                            api.version(SQLALCHEMY_MIGRATE_REPO))

def _generateMigrationScript(dryrun):
    newVersion = findMaxAvailableVersion() + 1
    migration = SQLALCHEMY_MIGRATE_REPO + \
                '/versions/%03d_migration.py' % (newVersion)
    tmp_module = imp.new_module('old_model')
    old_model = api.create_model(SQLALCHEMY_DATABASE_URI,
                                 SQLALCHEMY_MIGRATE_REPO)

    exec old_model in tmp_module.__dict__
    script = api.make_update_script_for_model(SQLALCHEMY_DATABASE_URI,
                                              SQLALCHEMY_MIGRATE_REPO,
                                              tmp_module.meta,
                                              db.metadata)
    if not dryrun:
        open(migration, "wt").write(script)
        api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
        print 'New migration saved as ' + migration
        print 'Current database version: ' + \
              str(api.db_version(SQLALCHEMY_DATABASE_URI,
                                 SQLALCHEMY_MIGRATE_REPO))
    else:
        print 'Dryrun:'
        print '\nNew migration will be as ' + migration
        print '\nNew migration script will be:\n"\n%s"' % str(script)
        print '\nNew database version will be: ' + str(newVersion)

def _upgradeDB(expectedVersion, dryrun):
    if not dryrun:
        api.upgrade(SQLALCHEMY_DATABASE_URI,
                    SQLALCHEMY_MIGRATE_REPO,
                    expectedVersion)
    
    print 'Current database version: ' + \
          str(api.db_version(SQLALCHEMY_DATABASE_URI,
                             SQLALCHEMY_MIGRATE_REPO))
    if dryrun:
        print 'Dryrun:'
        print '\tNew database version will be: ' + str(expectedVersion)

def _downgradeDB(expectedVersion, dryrun):
    if not dryrun:
        api.downgrade(SQLALCHEMY_DATABASE_URI,
                      SQLALCHEMY_MIGRATE_REPO,
                      expectedVersion)
    
    print 'Current database version: ' + \
          str(api.db_version(SQLALCHEMY_DATABASE_URI,
                         SQLALCHEMY_MIGRATE_REPO))
    if dryrun:
        print 'Dryrun'
        print '\tNew database version will be: ' + str(expectedVersion)

def findMaxAvailableVersion():
    migrationDir = os.path.join(SQLALCHEMY_MIGRATE_REPO, 'versions')
    allVersions = os.listdir(migrationDir)

    # Only keep the files that start with number and not end with 'c' like
    # python compiled files.
    allVersions = filter(lambda v: v[0].isdigit() \
                                   and not v[-1].endswith('c'),
                         allVersions)
    allVersions = map(lambda v: int(v.split('_')[0]), allVersions)

    if len(allVersions) > 0:
        return max(allVersions)
    else:
        return 0

def hasValidDBVersion(action, expectedVersion):
    maxAvailableVersion = findMaxAvailableVersion()
    curVision = api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
    if action == 'upgrade' and expectedVersion < curVision:
        return False

    if action == 'downgrade' and expectedVersion > curVision:
        return False

    if expectedVersion <= 0 or expectedVersion > maxAvailableVersion:
        return False

    return True

def _getCommandLineOptions():
    """Get the options from the command line.

    Returns:
        An argument parser.
    """
    parser = argparse.ArgumentParser(
                description='Create/Upgrade/downgrade database.')

    parser.add_argument('action',
                        choices=['create', 'upgrade', 'downgrade', 'generate'],
                        help='Action to preform on a database.')
    parser.add_argument('--db-version', default=-1,
                        help='Desired database version to upgrade/downgrade' \
                             'to. If none specified, it will upgrade to latest ' \
                             'or downgrade by 1. The version specified should ' \
                             'be between 1 and maximum available version. If ' \
                             'upgrade is the action, ',
                        type=int)
    parser.add_argument('--execute', dest='dryrun', action='store_false',
                        help='If passed, this will run the actual command, ' \
                             'otherwise a dry run happens.')

    opts = parser.parse_args()

    if opts.db_version != -1 and not \
            hasValidDBVersion(opts.action, opts.db_version):
        parser.print_help()
        print '\nERROR: Invalid DB version. Please make sure the specified DB' \
              ' version is correct.'
        return None
    else:
        return opts

def main():
    args = _getCommandLineOptions()

    if not args:
        return -1

    if args.action =='create':
        _creatDB(args.dryrun)
    elif args.action == 'upgrade':
        if args.db_version == -1:
            latestVersion = findMaxAvailableVersion()
            _upgradeDB(latestVersion, args.dryrun)
        else:
            _upgradeDB(args.db_version, args.dryrun)
    elif args.action == 'downgrade':
        if args.db_version == -1:
            newVersion = api.db_version(SQLALCHEMY_DATABASE_URI,
                                       SQLALCHEMY_MIGRATE_REPO) - 1
            _downgradeDB(newVersion, args.dryrun)
        else:
            _downgradeDB(args.db_version, args.dryrun)
    elif args.action == 'generate':
        _generateMigrationScript(args.dryrun)

    return 0

if __name__ == '__main__':
    sys.exit(main())
