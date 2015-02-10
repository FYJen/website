from datetime import datetime

ADDRESS_LIST = {
    'user_address': {
        'id': 1,
        'suite_number': 'Suite 302',
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
        'floor': '4th Floor',
        'street_name': '153 Kearny St.',
        'city': 'San Francisco',
        'province_state': 'CA',
        'postalcode_zip': '94108',
        'country': 'USA'
    },
    'OICR_address': {
        'id': 4,
        'suite_number': 'Suite 510',
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
    },
    'Yelp_address': {
        'id': 7,
        'street_name': '140 Montgomery St.',
        'city': 'San Francisco',
        'province_state': 'CA',
        'postalcode_zip': '94105',
        'country': 'USA'
    }
}

USER_LIST = {
    'main_user': {
        'id': 1,
        'first_name': 'Fei-Yang',
        'last_name': 'Jen',
        'email': 'fjen@uwaterloo.ca',
        'alt_email': 'fei.yang.jen@gmail.com',
        'phone': '(226) 972-0522',
        'skype': 'arthur5110',
        'github': 'https://github.com/FYJen',
        'linkedin': 'https://www.linkedin.com/pub/arthur-jen/56/528/914',
        'address_id': ADDRESS_LIST['user_address']['id'],
        'intro': '',
    }
}

WORKPLACE_LIST = [
    ('yelp_intern',
     {
        'name': 'Yelp Inc.',
        'position_title': 'Software Engineering Intern',
        'start_date': datetime(2015, 1, 5),
        'end_date': datetime(2015, 5, 1),
        'address_id': ADDRESS_LIST['Yelp_address']['id'],
        'user_id': USER_LIST['main_user']['id'],
        'web_link': 'http://www.yelp.com'
     }),
    ('inkling_intern_1',
     {
        'name': 'Inkling',
        'position_title': 'Cloud Engineering Intern',
        'start_date': datetime(2014, 5, 1),
        'end_date': datetime(2014, 8, 31),
        'address_id': ADDRESS_LIST['inkling_address']['id'],
        'user_id': USER_LIST['main_user']['id'],
        'web_link': 'http://www.inkling.com'
     }),
    ('inkling_intern_2',
     {
        'name': 'Inkling',
        'position_title': 'Web Ops Engineering Intern',
        'start_date': datetime(2013, 9, 1),
        'end_date': datetime(2013, 12, 31),
        'address_id': ADDRESS_LIST['inkling_address']['id'],
        'user_id': USER_LIST['main_user']['id'],
        'web_link': 'http://www.inkling.com'
     }),
    ('OICR_intern',
     {
        'name': 'Ontario Institute for Cancer Research',
        'initial': 'OICR',
        'position_title': 'Cloud Computing Software Developer',
        'start_date': datetime(2013, 1, 1),
        'end_date': datetime(2013, 4, 30),
        'address_id': ADDRESS_LIST['OICR_address']['id'],
        'user_id': USER_LIST['main_user']['id'],
        'web_link': 'http://www.oicr.on.ca'
     }),
    ('Awareness_intern',
     {
        'name': 'Awareness Inc.',
        'position_title': 'Cloud Operation Analyst',
        'start_date': datetime(2012, 5, 1),
        'end_date': datetime(2012, 8, 31),
        'address_id': ADDRESS_LIST['Awareness_address']['id'],
        'user_id': USER_LIST['main_user']['id'],
        'web_link': 'http://www.awarenesshub.com'
     }),
    ('NCHC_intern',
     {
        'name': 'National Center for High-Performance Computing',
        'initial': 'NCHC',
        'position_title': 'Project Engineering Assistant',
        'start_date': datetime(2011, 9, 1),
        'end_date': datetime(2011, 12, 31),
        'address_id': ADDRESS_LIST['NCHC_address']['id'],
        'user_id': USER_LIST['main_user']['id'],
        'web_link': 'http://www.nchc.org.tw/en'
     })
]

WORKTASK_LIST = {
    'yelp_intern': [
        'Created metric with Elasticsearch and Kibana to provide insight on business data.'
    ],
    'inkling_intern_1': [
        'Implemented several features in the backend services of Inkling Habitat using Python and Ruby',
        'Refactored the workflow for publishing books to the Inkling Store',
        'Fixed bugs and optimized slow HTTP requests in the code base'
    ],
    'inkling_intern_2': [
        'Developed and fixed internal workflows and tools to facilitate company new hire process using Python and JavaScript',
        'Participated in daily production deployments and maintenance of Cloud environments',
        'Implemented a job scheduler with open-source Azkaban Server and AWS EMR'
    ],
    'OICR_intern': [
        'Improved software Installation time by 80% using Bash',
        'Built applications to deploy scalable SGE Cluster with NFS on GCE using Perl',
        'Created generic application to launch scalable environments on AWS'
    ],
    'Awareness_intern': [
        'Implemented a private Cloud with CloudStack and LDAP to provide IaaS locally',
        'Deployed scalable Cloud environment with Alarm Clock, SQS, S3 and Load-Balance on AWS',
        'Performed benchmarking of database and disk I/O on Amazon and RackSpace'
    ],
    'NCHC_intern': [
        'Configured DNS with geo-location feature to distribute client connections',
        'Implemented load-balancer using HAproxy, Dstat and third-party libraries',
        'Co-Developed nation-wide Cloud storage service'
    ]
}

PROJECT_LIST = {
    'personal_webiste': {
        'id': 1,
        'name': 'Personal Website',
        'user_id': USER_LIST['main_user']['id'],
        'thumbnail': '/static/img/projects/personal_website.png',
        'link': 'https://github.com/FYJen/website',
        'start_date': datetime(2014, 7, 15)
    },
    'youtube_playlist_curl': {
        'id': 2,
        'name': 'YouTube Playlist Curler',
        'user_id': USER_LIST['main_user']['id'],
        'thumbnail': '/static/img/projects/playlistCurler.png',
        'link': 'https://github.com/FYJen/playlistCurler',
        'start_date': datetime(2014, 5, 15)
    },
    'eat_all_candy': {
        'id': 3,
        'name': 'Eat Candies',
        'user_id': USER_LIST['main_user']['id'],
        'thumbnail': '/static/img/projects/eatCandies.png',
        'link': 'https://github.com/FYJen/eat-candies',
        'start_date': datetime(2013, 10, 15)
    }
}

PROJECTTASK_LIST = {
    'personal_webiste': [
        'Implemented RESTful API to serve internal requests',
        'Hosted on AWS and built with Python, Flask framework, SQLAlchemy, Jinja2 Template, Redis, SQLite, Bootstrap, HTML, CSS, Nginx and uWSGI'
    ],
    'youtube_playlist_curl': [
        'An application that will curl a given YouTube playlist and download individual songs by posting requests to youtube-mp3.org',
        'Built with Python and Google YouTube Data API (V3)'
    ],
    'eat_all_candy': [
        'An interactive game to collect candies and dodge obstacles dropping from the sky',
        'Built with Python and Pygame engine'
    ]
}

SCHOOL_LIST = {
    'school_1': {
        'id': 1,
        'name': 'University of Waterloo',
        'level': 'University/College',
        'degree': 'Bachelor of Computer Science',
        'major': 'Computer Science',
        'minor': 'Economics',
        'start_date': datetime(2010, 9, 10),
        'end_date': datetime(2015, 8, 31),
        'term': '4A',
        'address_id': ADDRESS_LIST['school_address']['id']
    }
}

TAGS_LIST = {
    'C++/C': 1,
    'Cloud': 2,
    'Database': 3,
    'Others': 4,
    'Python': 5,
    'Ruby': 6,
    'Server': 7,
    'Tools': 8
}

SKILLS_LIST = {
    'TOOLS': {
        'userId': USER_LIST['main_user']['id'],
        'tagId': TAGS_LIST['Tools'],
        'items': ['Git', 'Sublime Text 2', 'Vim', 'Linux (Ubuntu)', 'Windows',
                  'Macintosh']
    },
    'CLOUD': {
        'userId': USER_LIST['main_user']['id'],
        'tagId': TAGS_LIST['Cloud'],
        'items': ['AWS (EC2, S3, Route 53, EMR)', 'GCE', 'RackSpace', 'CloudStack',
                  'OpenStack']
    },
    'SERVER': {
        'userId': USER_LIST['main_user']['id'],
        'tagId': TAGS_LIST['Server'],
        'items': ['Apache', 'Nginx', 'DNS', 'HAproxy', 'Jenkins CI Server',
                  'Azkaban Server']
    },
    'DATABASE': {
        'userId': USER_LIST['main_user']['id'],
        'tagId': TAGS_LIST['Database'],
        'items': ['Redis', 'SQLite', 'MySQL', 'PostgreSQL']
    },
    'OTHERS': {
        'userId': USER_LIST['main_user']['id'],
        'tagId': TAGS_LIST['Others'],
        'items': ['C++', 'C', 'Bash', 'Docker', 'HTML', 'CSS', 'Bootstrap', 'JavaScript', 'Perl']
    },
    'C++/C': {
        'userId': USER_LIST['main_user']['id'],
        'tagId': TAGS_LIST['C++/C'],
        'items': ['A program with concurrency and synchronization using '
                  'Administrator model', 'An OS with file system, memory '
                  'management, threads and scheduling']
    },
    'PYTHON': {
        'userId': USER_LIST['main_user']['id'],
        'tagId': TAGS_LIST['Python'],
        'items': ['Feature implementations, APIs, performance optimizations and '
                  'bug fixes', 'A personal website powered by Flask and hosted on '
                  'AWS']
    },
    'RUBY': {
        'userId': USER_LIST['main_user']['id'],
        'tagId': TAGS_LIST['Ruby'],
        'items': ['Feature implementations, APIs, performance optimizations and bug fixes']
    }
}
