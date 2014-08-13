from datetime import datetime

ADDRESS_LIST = {
    'user_address': {
        'id': 1,
        'suite_number': '302',
        'street_name': '321 Lester St.',
        'city': 'Waterloo',
        'province_state': 'ON',
        'postalcode_zip': 'N2L 3W6',
        'country': 'Canada'
    },
    'school_address': {
        'id': 2,
        'street_name': '200 University Ave W.',
        'city': 'Waterloo',
        'province_state': 'ON',
        'postalcode_zip': 'N2L 3G1',
        'country': 'Canada'
    },
    'inkling_address': {
        'id': 3,
        'floor': '4th',
        'street_name': '153 Kearny St.',
        'city': 'San Francisco',
        'province_state': 'CA',
        'postalcode_zip': '94108',
        'country': 'USA'
    },
    'OICR_address': {
        'id': 4,
        'suite_number': '510',
        'street_name': '661 University Ave.',
        'city': 'Toronto',
        'province_state': 'ON',
        'postalcode_zip': 'M5G 0A3',
        'country': 'Canada'
    },
    'NCHC_address': {
        'id': 5,
        'apt_number': 'No. 7',
        'street_name': 'R&D 6th Rd.',
        'city': 'Hsinchu',
        'country': 'Taiwan'
    },
    'Awareness_address': {
        'id': 6,
        'street_name': '5050 S Service Rd.',
        'city': 'Burlington',
        'province_state': 'ON',
        'postalcode_zip': 'L7L 5Y7',
        'country': 'Canada',
        'active': False
    }
}

USER_LIST = {
    'main_user': {
        'id': 1,
        'first_name': 'Fei-Yang',
        'last_name': 'Jen',
        'email': 'fjen@uwaterloo.ca',
        'phone': '(226) 972-0522',
        'address_id': ADDRESS_LIST['user_address']['id']
    }
}

WORKPLACE_LIST = {
    'inkling_intern_1': {
        'name': 'Inkling',
        'position_title': 'Cloud Engineering Intern',
        'start_date': datetime(2014, 5, 1),
        'end_date': datetime(2014, 8, 31),
        'address_id': ADDRESS_LIST['inkling_address']['id'],
        'user_id': USER_LIST['main_user']['id']
    },
    'inkling_intern_2': {
        'name': 'Inkling',
        'position_title': 'Web Ops Engineering Intern',
        'start_date': datetime(2013, 9, 1),
        'end_date': datetime(2013, 12, 31),
        'address_id': ADDRESS_LIST['inkling_address']['id'],
        'user_id': USER_LIST['main_user']['id']
    },
    'OICR_intern': {
        'name': 'Ontario Institute for Cancer Research',
        'initial': 'OICR',
        'position_title': 'Cloud Computing Software Developer',
        'start_date': datetime(2013, 1, 1),
        'end_date': datetime(2013, 4, 30),
        'address_id': ADDRESS_LIST['OICR_address']['id'],
        'user_id': USER_LIST['main_user']['id']
    },
    'Awareness_intern': {
        'name': 'Awareness Inc.',
        'position_title': 'Cloud Operation Analyst',
        'start_date': datetime(2012, 5, 1),
        'end_date': datetime(2012, 8, 31),
        'address_id': ADDRESS_LIST['Awareness_address']['id'],
        'user_id': USER_LIST['main_user']['id']
    },
    'NCHC_intern': {
        'name': 'National Center for High-Performance Computing',
        'initial': 'NCHC',
        'position_title': 'Project Engineering Assistant',
        'start_date': datetime(2011, 9, 1),
        'end_date': datetime(2011, 12, 31),
        'address_id': ADDRESS_LIST['NCHC_address']['id'],
        'user_id': USER_LIST['main_user']['id']
    }
}

TAGS_LIST = ['C++/C', 'Cloud', 'Database', 'Others', 'Python',
             'Ruby on Rails', 'Server', 'Tools']
TOOLS_LIST = ['Git', 'Sublime Text 2', 'Vim', 'Linux (Ubuntu)', 'Windows',
              'Macintosh']
CLOUD_LIST = ['AWS (EC2, S3, Route 53, EMP)', 'GCE', 'RackSpace', 'CloudStack',
              'OpenStack']
SERVER_LIST = ['Apache', 'Nginx', 'DNS', 'HAproxy', 'Jenkins CI Server',
               'Azkaban Server']
DATABASE_LIST = ['Redis', 'SQLite', 'MySQL', 'PostgreSQL']
OTHER_LIST = ['Bash', 'Docker', 'HTML', 'CSS', 'Bootstrap', 'JavaScript', 'Perl']
C_LIST = ['A program with concurrency and synchronization using Administrator model']
CPP_LIST = ['An OS with file system, memory management, threads and scheduling']
PYTHON_LIST = ['Feature implementations, APIs, performance optimizations and bug fixes',
               'A personal website powered by Flask and hosted on AWS']
RUBY_LIST = ['Feature implementations, APIs, performance optimizations and bug fixes']

