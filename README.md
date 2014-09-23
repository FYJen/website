#[Personal Website](http://www.arthur-jen.com)

This is a personal website that I built to exhibit my interests, projects and latest resume. In fact, this website is a by-product of RESTful API that I built underneath it. The website is hosted on AWS. Since I work most comfortably with Python, I choose Flask as my web framework and SQLAlchemy ORM as toolkit to interact with database. Nginx and Supervisor(uWSGI) are used to host web and API servers and keep them alive. I am currently working on Redis and Docker integration to make data retrieval faster and deployment smoother.

##RESTful API
The RESTful API is built around personal information on my resume. The API includes the following categories:

- `user`: A user is a single entity containing basic personal information.
- `skill`: A skill is a single technique.
- `work_place`: A work_place is a work location.
- `workplace_task`: A work_task is a task associated to a work_place.
- `project`: A project is any related work done in and out of the school.
- `project_task`: A project_task is a task associated to a project.
- `school`: A school is an education institution.
- `tag`: A tag is a category of skills.
- `address`: An address is a place where the user lives.

Currently I only open requests to `GET` method. All API support retrieving data through `index` and `find`.

- `index`: Supply resource id.
- `find`: Supply a list of query parameters.

In addition, each API has its own `deref` fields that can be added to the query string optionaly to return information in more detailed. To access the API, you can easily send `GET` request to [www.arthur-jen.com](http://www.arthur-jen.com).

More examples will be provied below. 

#### ```GET /api/user/```
Retrieve user information.

- `index`: /api/user/<`int:id`>
- `find`: /api/user/?<`string:email`; `string:firstName`; `string:lastName`; `int:phone`>
- `deref` fields: `address`, `skills`, `workPlaces`, `projects`, and `schools` 

Examples:

- /api/user/1
	
	```
	{
    	status: {
        	statusMsg: "OK",
        	statusDetails: {},
        	statusCode: "HTTPOk"
    	},
    	result: {
        	id: 1,
        	name: "Fei-Yang Jen",
        	email: "fjen@uwaterloo.ca",
        	alt_email: "fei.yang.jen@gmail.com",
        	phone: "(226) 972-0522",
        	skype: "arthur5110",
        	github: "https://github.com/FYJen",
        	linkedin: "https://www.linkedin.com/pub/arthur-jen/56/528/914"
    	}
	}
	```
- /api/user/?email=fjen@uwaterloo.ca&deref=address&deref=projects

	```
	{
    	status: {
        	statusMsg: "OK",
        	statusDetails: {},
        	statusCode: "HTTPOk"
    	},
    	result: [{
        	id: 1,
        	name: "Fei-Yang Jen",
        	email: "fjen@uwaterloo.ca",
        	alt_email: "fei.yang.jen@gmail.com",
        	phone: "(226) 972-0522",
        	skype: "arthur5110",
        	github: "https://github.com/FYJen",
        	linkedin: "https://www.linkedin.com/pub/arthur-jen/56/528/914",
        	address: [{
            	id: 1,
            	Apt / Suite / Floor: "Suite 302",
            	streetName: "321 Lester St.",
            	city: "Waterloo",
            	province / state: "ON",
            	country: "Canada",
            	postalCode / zip: "N2L 3W6",
            	active: true,
            	occupants: [],
            	stringnifyAddr: "Suite 302, 321 Lester St., Waterloo, ON, Canada, N2L 3W6"
        	}],
        	projects: [{
            	id: 1,
            	name: "Personal Website",
            	startDate: "7/2014",
            	endDate: null,
            	thumbnail: "/static/img/projects/personal_website.png",
            	link: "https://github.com/FYJen/website",
            	tasks: [
                	"Implemented RESTful API to serve internal requests",
                	"Hosted on AWS and built with Python, Flask framework, SQLAlchemy, Jinja2 Template, Redis, SQLite, Bootstrap, HTML, CSS, Nginx and uWSGI"
            	]
        	},
        		.....
        	]
    	}]
	}
	```

#### ```GET /api/workplace/```
Retrieve work places information.

- `index`: /api/workplace/<`int:id`>
- `find`: /api/workplace/?<`string:name`; `string:initial`; `string:positionTitle`>
- `deref` fields: `user`, `tasks`, and `address`

Examples:

- /api/workplace/2
	
	```
	{
    	status: {
        	statusMsg: "OK",
        	statusDetails: {},
        	statusCode: "HTTPOk"
    	},
    	result: {
        	id: 3,
        	name: "Ontario Institute for Cancer Research",
        	initial: "OICR",
        	positionTitle: "Cloud Computing Software Developer",
        	startDate: "1/2013",
        	endDate: "4/2013",
        	web_link: "http://www.oicr.on.ca"
    	}
	}
	```
- /api/workplace/?initial=OICR&deref=user&deref=tasks

	```
	{
    	status: {
        	statusMsg: "OK",
        	statusDetails: {},
        	statusCode: "HTTPOk"
    	},
    	result: [{
        	id: 3,
        	name: "Ontario Institute for Cancer Research",
        	initial: "OICR",
        	positionTitle: "Cloud Computing Software Developer",
        	startDate: "1/2013",
        	endDate: "4/2013",
        	web_link: "http://www.oicr.on.ca",
        	user: "fjen@uwaterloo.ca",
        	tasks: [
            	"Improved software Installation time by 80% using Bash",
            	"Built applications to deploy scalable SGE Cluster with NFS on GCE using Perl",
            	"Created generic application to launch scalable environments on AWS"
        	]
    	}]
	}
	```

#### ```GET /api/worktask/```
Retrieve work tasks information.

- `index`: /api/workplace/<`int:id`>
- `find`: /api/workplace/?<`string:workPlaceName`; `string:initial`>
- `deref` fields: `workplace`

Examples:

- /api/worktask/11
	
	```
	{
    	status: {
        	statusMsg: "OK",
        	statusDetails: {},
        	statusCode: "HTTPOk"
    	},
    	result: {
        	id: 11,
        	description: "Implemented load-balancer using HAproxy, Dstat and third-party libraries"
    	}
	}
	```
- /api/worktask/?initial=NCHC&deref=workplace

	```
	{
    	status: {
        	statusMsg: "OK",
        	statusDetails: {},
        	statusCode: "HTTPOk"
    	},
    	result: [{
        	id: 10,
        	description: "Configured DNS with geo-location feature to distribute client connections",
        	workPlace: "National Center for High-Performance Computing"
    	}, {
        	id: 11,
        	description: "Implemented load-balancer using HAproxy, Dstat and third-party libraries",
        	workPlace: "National Center for High-Performance Computing"
    	}, {
        	id: 12,
        	description: "Co-Developed nation-wide Cloud storage service",
        	workPlace: "National Center for High-Performance Computing"
    	}]
	}
	```

#### ```GET /api/address/```
Retrieve address information.

- `index`: /api/workplace/<`int:id`>
- `find`: /api/workplace/?<`boolean:active`; `string:country`; `string:postalCode`; `string:zipCode`; `boolean:stringnify`>
- `deref` fields: `occupants`

Examples:

- /api/address/1
	
	```
	{
    	status: {
        	statusMsg: "OK",
        	statusDetails: {},
        	statusCode: "HTTPOk"
    	},
    	result: {
        	id: 1,
        	Apt / Suite / Floor: "Suite 302",
        	streetName: "321 Lester St.",
        	city: "Waterloo",
        	province / state: "ON",
        	country: "Canada",
        	postalCode / zip: "N2L 3W6",
        	active: true,
        	occupants: []
    	}
	}
	```
- /api/address/?active=1&country=USA&deref=occupants&stringnify=true

	```
	{
    	status: {
        	statusMsg: "OK",
        	statusDetails: {},
        	statusCode: "HTTPOk"
    	},
    	result: [{
        	id: 3,
        	Apt / Suite / Floor: "4th Floor",
        	streetName: "153 Kearny St.",
        	city: "San Francisco",
        	province / state: "CA",
        	country: "USA",
        	postalCode / zip: "94108",
        	active: true,
        	occupants: [
            	"Inkling"
        	],
        	stringnifyAddr: "4th Floor, 153 Kearny St., San Francisco, CA, USA, 94108"
    	}]
	}
	```

#### ```GET /api/tag/```
Retrieve tag information.

- `index`: /api/tag/<`int:id`>
- `find`: /api/tag/?<`string:name`>
- `deref` fields: `skill`

Examples:

- /api/tag/5
	
	```
	{
    	status: {
        	statusMsg: "OK",
        	statusDetails: {},
        	statusCode: "HTTPOk"
    	},
    	result: [{
        	id: 5,
        	tagName: "Python"
    	}]
	}
	```
- /api/tag/?name=Server&deref=skill

	```
	{
    	status: {
        	statusMsg: "OK",
        	statusDetails: {},
        	statusCode: "HTTPOk"
    	},
    	result: [{
        	id: 7,
        	tagName: "Server",
        	skills: [{
            	id: 30,
            	description: "Apache"
        	}, {
            	id: 31,
            	description: "Nginx"
        	}, {
            	id: 32,
            	description: "DNS"
        	}, {
            	id: 33,
            	description: "HAproxy"
        	}, {
           		id: 34,
            	description: "Jenkins CI Server"a
        	}, {
            	id: 35,
            	description: "Azkaban Server"
        	}]
    	}]
	}
	```

#### ```GET /api/skill/```
Retrieve skill information.

- `index`: /api/skill/<`int:id`>
- `find`: /api/skill/?<`string:description`; `string:tag`; `int:userId`>
- `deref` fields: `user` and `tag`

Examples:

- /api/skill/5
	
	```
	{
    	status: {
        	statusMsg: "OK",
        	statusDetails: {},
        	statusCode: "HTTPOk"
    	},
    	result: [{
        	id: 5,
        	description: "MySQL"
    	}]
	}
	```
- /api/skill/?userId=1&deref=user&deref=tag

	```
	{
    	status: {
        	statusMsg: "OK",
        	statusDetails: {},
        	statusCode: "HTTPOk"
    	},
    	result: [{
          
          	....
      
    	}, {
        	id: 4,
        	description: "SQLite",
        	user: "fjen@uwaterloo.ca",
        	tag: "Database"
    	}, {
        	id: 5,
        	description: "MySQL",
        	user: "fjen@uwaterloo.ca",
        	tag: "Database"
    	}, {
        	id: 6,
        	description: "PostgreSQL",
        	user: "fjen@uwaterloo.ca",
        	tag: "Database"
    	}, {
        	id: 7,
        	description: "Feature implementations, APIs, performance optimizations and bug fixes",
        	user: "fjen@uwaterloo.ca",
        	tag: "Python"
    	}, {
    	
    		....
    
    	}]
	}
	```

#### ```GET /api/school/```
Retrieve school information.

- `index`: /api/school/<`int:id`>
- `find`: /api/school/?<`string:name`; `string:level`; `string:attending`>
- `deref` fields: `address` and `course` (currently not supported)

Examples:

- /api/school/1
	
	```
	{
    	status: {
        	statusMsg: "OK",
        	statusDetails: {},
        	statusCode: "HTTPOk"
    	},
    	result: [{
        	id: 1,
        	name: "University of Waterloo",
        	level: "University/College",
        	degree: "Bachelor of Computer Science",
        	major: "Computer Science",
        	minor: "Economics",
        	joint: null,
        	startDate: "9/2010",
        	endDate: "8/2015",
        	attending: true,
        	term: "4A"
    	}]
	}
	```
- /api/school/?attending=true&deref=address

	```
	{
    	status: {
        	statusMsg: "OK",
        	statusDetails: {},
        	statusCode: "HTTPOk"
    	},
    	result: [{
        	id: 1,
       		name: "University of Waterloo",
        	level: "University/College",
        	degree: "Bachelor of Computer Science",
        	major: "Computer Science",
        	minor: "Economics",
        	joint: null,
        	startDate: "9/2010",
        	endDate: "8/2015",
        	attending: true,
        	term: "4A",
        	address: [{
            	id: 2,
            	Apt / Suite / Floor: "",
            	streetName: "200 University Ave W.",
            	city: "Waterloo",
            	province / state: "ON",
            	country: "Canada",
            	postalCode / zip: "N2L 3G1",
            	active: true,
            	occupants: [],
            	stringnifyAddr: "200 University Ave W., Waterloo, ON, Canada, N2L 3G1"
        	}]
    	}]
	}
	```

#### ```GET /api/project/```
Retrieve project information.

- `index`: /api/project/<`int:id`>
- `find`: /api/project/?<`string:projectName`>
- `deref` fields: `user` and `tasks`

Examples:

- /api/project/1
	
	```
	{
    	status: {
        	statusMsg: "OK",
        	statusDetails: {},
        	statusCode: "HTTPOk"
    	},
    	result: {
        	id: 1,
        	name: "Personal Website",
        	startDate: "7/2014",
        	endDate: null,
        	thumbnail: "/static/img/projects/personal_website.png",
        	link: "https://github.com/FYJen/website"
    	}
	}
	```
- /api/school/?attending=true&deref=address

	```
	{
    	status: {
        	statusMsg: "OK",
        	statusDetails: {},
        	statusCode: "HTTPOk"
    	},
    	result: [{
        	id: 1,
        	name: "Personal Website",
        	startDate: "7/2014",
        	endDate: null,
        	thumbnail: "/static/img/projects/personal_website.png",
        	link: "https://github.com/FYJen/website",
        	tasks: [
            	"Implemented RESTful API to serve internal requests",
            	"Hosted on AWS and built with Python, Flask framework, SQLAlchemy, Jinja2 Template, Redis, SQLite, Bootstrap, HTML, CSS, Nginx and uWSGI"
        	]
    	}]
	}
	```

#### ```GET /api/projecttask/```
Retrieve project task information.

- `index`: /api/projecttask/<`int:id`>
- `find`: /api/projecttask/?<`string:projectName`>
- `deref` fields: `project`

Examples:

- /api/projecttask/1
	
	```
	{
    	status: {
        	statusMsg: "OK",
        	statusDetails: {},
        	statusCode: "HTTPOk"
    	},
    	result: {
        	id: 1,
        	description: "An application that will curl a given YouTube playlist and download individual songs by posting requests to youtube-mp3.org"
    	}
	}
	```
- /api/projecttask/?projectName=YouTube%20Playlist%20Curler&deref=project

	```
	{
    	status: {
        	statusMsg: "OK",
        	statusDetails: {},
        	statusCode: "HTTPOk"
    	},
    	result: [{
        	id: 1,
        	description: "An application that will curl a given YouTube playlist and download individual songs by posting requests to youtube-mp3.org",
        project: "YouTube Playlist Curler"
    	}, {
        	id: 2,
        	description: "Built with Python and Google YouTube Data API (V3)",
        	project: "YouTube Playlist Curler"
    	}]
	}
	```


##Database Model
Database model can be found in [dbmodels directory](./dbmodels/models.py). The file defines a list of models(tables) used to store information for the website. API will be accessing these data through the models defined there. I choose to use SQLite to remove overhead dealing with configuring MySQL and PostgreSQL. Also, for the project like this, which is relatively less data-intensive, SQLite is a good candidate.


##Deployment

#####Local Development
Simply open two terminals and execute `python run-api.py` and `python run-web.py` separately. This will bring up both web and API server. By default, web server will run on 127.0.0.1:8080 and API server will run on 127.0.0.1:5050

####Production
Nginx and Supersivor(uWSGI) are used to host web and API servers. The configurations for both Nginx and Supervisor can be found in [deploy directory](./deploy/). I used Supervisor to bring up two separate uWSGI processes: one for webpages and one for API. Nginx is the front web server which will route traffic to different endpoints depending on the URL path.

##TODO
There are a couple improvements that can be done to help out with deployment and overall user experience.

- Using memory database like Redis or Memcache
- Using Docker to deploy web server 
  