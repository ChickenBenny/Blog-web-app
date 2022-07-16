# Social Network Web App
### Quick start
1. Create a directory for this project
```
$ mkdir web_app
$ cd web_app
$ git clone git@github.com:ChickenBenny/Social-network-web-app.git
```
2. Run the serviceby docker-compose up
```
$ docker-compose up
```
3. Architecture of this project
```
.
├─nginx
└─social_app
    └─app
        ├─errors
        ├─main
        ├─posts
        ├─static
        │  └─profile_pics
        ├─templates
        │  └─errors
        └─users
```
### About this project
This project is which I use to learn how to buil a website from zero to one. And in this project I use Flask as backend framework, Nginx as proxy server and Docker as Container.

##### Language and tools
<img src="https://www.vectorlogo.zone/logos/python/python-icon.svg" />
<img src="https://www.vectorlogo.zone/logos/pocoo_flask/pocoo_flask-icon.svg" />
<img src="https://www.vectorlogo.zone/logos/w3_html5/w3_html5-icon.svg" />
<img src="https://www.vectorlogo.zone/logos/w3_css/w3_css-icon.svg" />
<img src="https://www.vectorlogo.zone/logos/pocoo_jinja/pocoo_jinja-icon.svg" />
<img src="https://www.vectorlogo.zone/logos/sqlite/sqlite-icon.svg" />
<img src="https://www.vectorlogo.zone/logos/docker/docker-icon.svg" />

##### Try to learn
1. How to write Restful API
2. CRUD operation
3. Authentication with ID token
4. Connect the server with database
6. How to write a dockerfile and use the container
7. How to build a frontend page