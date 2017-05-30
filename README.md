## Technologies
- Python 3
- Falcon
- MySQL

## API Description
Api in development for the platform described above, includes the following methods: 

### User
|   URL             | VERB   | BODY    | EXAMPLE | RESULT              |
| ---               |  ---   |  ---    | ---     | ---                 |
| /user             | POST   | JSON    | {<br/>"name":"Example",<br/>"email":"example@example.com",<br/>"age":"21",<br/>"password":"123456"<br/>} |   Add a user |
| /user/{id}        | GET    | empty   | ---     |   Return a user by given id |
| /user/{id}        | DELETE | empty   | ---     |   Delete user by id |
| /user/{id}/interests  | GET    | empty   | ---     |   Return all interests of user = id |
| /user/{id}/skills  | GET    | empty   | ---     |   Return all skills of user = id |
| /user/email/{e-mail}    | GET    | empty   | --- |   Return a user by given email    |
| /user/info   			| POST    | JSON   | {"facebook": "http://www.facebook.com/example", "whatsapp": "84111111111", "id_user": "5"}     |   Insert user information by an user id |
| /user/info   			| PUT    | JSON   | {"facebook": "http://www.facebook.com/example", "whatsapp": "84111111111", "id_user": "5"}     |   Update user information by an user id |
| /user/info/{id}   | GET    | empty   | ---     |   Return an specific user information | 
| /user/info/{id}   | DELETE    | empty   | ---     |   Delete user info by an user id | 
| ---               |  ---   |  ---    | ---     | ---                 |
| /users            | GET    | empty   | ---     |   Return all users    |
| /users/infos      		| GET    | empty   | ---     |   Return all users information  |
| /users/interests     | GET    | empty   | ---     |   Return all pair user-interest |
| /users/interests      | POST    | JSON   |  {<br/> "id_user":"1", <br/>"id_skill":"2"<br/>}    |   Add a User-Interest relation |
| /users/skills      | GET    | empty   | ---     |   Return all pair user-skill |
| /users/skills      | POST    | JSON   |  {<br/> "id_user":"1", <br/>"id_skill":"2"<br/>}    |   Add a User-Skill relation |


### Picture
|   URL             | VERB   | BODY    | EXAMPLE | RESULT              |
| ---               |  ---   |  ---    | ---     | ---                 |
| /user/picture/{id_user}| GET    | empty   | ---     |   Return an url in format '/uploaded_pictures/filename.type' you might add server url before |
| /user/picture 			| POST   | JSON   | {<br/>"type": "imagetype (png OR jpg OR gif)", <br/>"bytecode": "imagebase64bytecode", <br/>"id_user": 1<br/>}     |   Upload an image on server to a given user |

### Login
|   URL             | VERB   | BODY    | EXAMPLE | RESULT              |
| ---               |  ---   |  ---    | ---     | ---                 |
| /login            | GET    | JSON   | {<br/>"email":"example@example.com",<br/>"password":"123456"<br/>}     |   Return a JSON with "logged" (if false something the user is not logged and if true the user is logged) |

### Skills
|   URL             | VERB   | BODY    | EXAMPLE | RESULT              |
| ---               |  ---   |  ---    | ---     | ---                 |
| /skill/        | GET    | empty   | ---     |   Return all skills | 
| /skill/{id}        | GET    | empty   | ---     |   Return a skill by given id | 
| /skill/autocomplete/{name}      | GET    | empty   |  ---    |   Return all skills that contains {name} |
| /skill/{id}/users  | GET    | empty   | ---     |   Return all users that has skill id  |
| /user/{id}/skills  | GET    | empty   | ---     |   Return all skills of user = id |
| /users/skills      | POST    | JSON   |  {<br/> "id_user":"1", <br/>"id_skill":"2"<br/>}    |   Add a User-Skill relation |

### Interest
|   URL             | VERB   | BODY    | EXAMPLE | RESULT              |
| ---               |  ---   |  ---    | ---     | ---                 |
| /interest/{id}/users  | GET    | empty   | ---     |   Return all users that has interest id  | 
| /user/{id}/interests  | GET    | empty   | ---     |   Return all interests of user = id |
| /users/interests      | POST    | JSON   |  {<br/> "id_user":"1", <br/>"id_skill":"2"<br/>}    |   Add a User-Interest relation |

### Match
|   URL             | VERB   | BODY    | EXAMPLE | RESULT              |
| ---               |  ---   |  ---    | ---     | ---                 |
| /matches  | GET    | empty   | ---     |   Return all matches  | 
| /matches/{id}  | GET    | empty   | ---     |   Return all matches for an giver user_id  | 
| /matches  | POST    | JSON   | {<br/>"id_user_not":"16", <br/>"id_user_has":"1ad8", <br/>"id_skill": "2"<br/>}     |   Insert a match  | 

## Getting Started
### Installing prerequisites
To use the api server you will need Python 3, Falcon and a WSGI Server (in our project we use gunicorn).

To run our api server you will need to do this following steps one time:

1. Install python-pip and mysql-server if you don't have it;
2. Install the mysql client lib if you don't have it: `sudo apt-get install libmysqlclient-dev`;
3. Install python mysql lib: `# pip install MySQL-python`;
4. Install falcon using pip: `# pip install falcon`;
5. Install gunicorn using pip: `# pip install gevent gunicorn`.

For easier management of pip packages, it's recommended to use [virtualenv](https://virtualenv.pypa.io/en/stable/). It creates isolated Python environments, and does not need superuser privileges to install packages. 

### Running
To run the api server do the following: 

1. Clone the project: `$ git clone git@github.com:Processos-de-software-2016-2/python-api.git`;
2. Run the server: `gunicorn main:app --bind 0.0.0.0:<desired_port>`;
3. Make a HTTP request on port 8000 to any of the URLs listed in API Description section.

# How to Contribute
1. Clone the project: `$ git clone git@github.com:Processos-de-software-2016-2/python-api.git`;
2. If you already have the project update it: `$ git pull origin master`;
3. Create a branch to start coding: `$ git checkout -b <branch_name>`;
4. Commit and push your changes: `$ git push origin <branch_name>`;
5. Create a pull request from your branch to master.

# Other Parts of this Project 

- [Android](https://github.com/Processos-de-software-2016-2/Android)
- [Infrastructure](https://github.com/Processos-de-software-2016-2/Infraestrutura) 
- [WebApp](https://github.com/Processos-de-software-2016-2/Web-App)
- [UX](https://github.com/Processos-de-software-2016-2/UX)
