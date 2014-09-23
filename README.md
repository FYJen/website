#Personal Website

This is a personal website that I built to exhibit my interests, projects and latest resume. In fact, this website is a by-product of RESTful API that I built underneath it. The website is hosted on AWS. Since I work most comfortably with Python, I choose Flask as my web framework and SQLAlchemy ORM as toolkit to interact with database. Nginx and Supervisor(uWSGI) are used to host the web server and keep it alive. I am currently working on Redis and Docker integration to make data retrieval faster and deployment smoother.

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

In addition, each API has its own `deref` fields that can be added to the query string optionaly to return information in more details. More examples will be provied below. 

#### ```GET /api/user/```
=========================
Retrieve user information.

- `index`: /api/user/<`int:id`>
- `find`: /api/user/?<`string:email`; `string:firstName`; `string:lastName`; `string:phone`>
- `deref` fields: `address`, `skills`, `workPlaces`, `projects`, and `schools` 

Example:

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
        	}, {
            	id: 2,
            	name: "YouTube Playlist Curler",
            	startDate: "5/2014",
            	endDate: null,
            	thumbnail: "/static/img/projects/playlistCurler.png",
            	link: "https://github.com/FYJen/playlistCurler",
            	tasks: [
                	"An application that will curl a given YouTube playlist and download individual songs by posting requests to youtube-mp3.org",
                	"Built with Python and Google YouTube Data API (V3)"
            	]
        	}, {
            	id: 3,
            	name: "Eat Candies",
            	startDate: "10/2013",
            	endDate: null,
            	thumbnail: "/static/img/projects/eatCandies.png",
            	link: "https://github.com/FYJen/eat-candies",
            	tasks: [
                	"An interactive game to collect candies and dodge obstacles dropping from the sky",
                	"Built with Python and Pygame engine"
            	]
        	}]
    	}]
	}
	```

#### ```GET /api/workplace/```
=========================
Retrieve work places information.

- `index`: /api/workplace/<`int:id`>
- `find`: /api/workplace/?<`string:name`; `string:initial`; `string:positionTitle`>
- `deref` fields: `user`, `tasks`, and `address`

Example:

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
============================
Retrieve work tasks information.

- `index`: /api/workplace/<`int:id`>
- `find`: /api/workplace/?<`string:workPlaceName`; `string:initial`>
- `deref` fields: `workplace`

Example:

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
===========================
Retrieve address information.

- `index`: /api/workplace/<`int:id`>
- `find`: /api/workplace/?<`boolean:active`; `string:country`; `string:postalCode`; `string:zipCode`; `boolean:stringnify`>
- `deref` fields: `occupants`

Example:

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

#### ```GET /api/address/```
===========================
Retrieve address information.

- `index`: /api/workplace/<`int:id`>
- `find`: /api/workplace/?<`boolean:active`; `string:country`; `string:postalCode`; `string:zipCode`; `boolean:stringnify`>
- `deref` fields: `occupants`

Example:

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

##Database


##Deployment

  