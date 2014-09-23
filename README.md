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

- `index`: Supply index id.
- `find`: Supply a list of query parameters.

In addition, each API has its own `deref` fields that can be added to the query string optionaly to return information in more details. More examples will be provied below. 

### ```GET /api/user/```
Retrieve user information.

- `index`: /api/user/<`int:id`>
- `find`: /api/user/?<`string:email`; `string:firstName`; `string:lastName`; `string:phone`>
- `deref` fields: `address`, `skills`, `workPlaces`, `projects`, and `schools` 

Example:

- `/api/user/1`
	
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
- `/api/user/?email=fjen@uwaterloo.ca&deref=address&deref=projects`

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
- `/api/user/2`

	```
	{
    	status: {
        	statusMsg: "No user found with Id - 2",
        	statusDetails: {},
        	statusCode: "ResourceNotFound"
    	},
    	result: {}
	}
	```

### ```GET /api/workplace/```
Retrieve work place information.

- `index`: /api/workplace/<`int:id`>
- `find`: /api/workplace/?<`string:name`; `string:initial`; `string:positionTitle`>
- `deref` fields: `user`, `tasks`, and `address`




##Databas


##Deployment

  