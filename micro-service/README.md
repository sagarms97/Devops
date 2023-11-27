# emart-app

### How we containerize a micro-service application
- We have 4 services are here (NGINX, ANGULAR, JAVA & NODEJS)
	- **NGINX**
		- It is the API gateway , which is the front end from where all the request comes.
		- And all the communication between micro-services happen through this API gateway.
		- This will be an nginx service which will listen for the request and route based on the headers / urls.
	- **ANGULAR**
		- If the request comes from the route , that is if you are just accessing the url , then its send to client micro-services.
	- **NODE-JS**
		- THE API serivce emart  API which is written in NODEJS & the url will be  /API 
		- Node-JS  application these api's will need database & here we are using mangoDB (no-SQL)
	- **JAVA**
		- Another service **BOOK API** which is written in java .
		- It uses my-sql data base & its url is /webapi 

- So this is an ecommerce application which has multiple micro-services.


### Build & Run micro-service app

- EC2
	- name: Docker-Engine
	- OS : ubuntu-server 20
	- type: t3.medium (2vcpu, 4gib memory)
	- key : docker -key
	- Network : allow ssh traffic from -myip
		- allow http traffic from the internet
	- storage : 20 Gb
	- Advance : Here we need docker-engine, docker compose & ubuntu user in the docker group

GIT
```bash
docker-compose --version
git clone <emart repo url>
ls
cd emart/
ls
docker-compose build
# 1st we build & then we run containers,becz build takes very long time

docker images
# now we have 3 images
# 1. client -> whicjh is our angular app hosted in NGINX container
# 2. webapi -> which is java hosted in jdk conatiners
# 3. api -> which is Nodejs running on a nodejs conatiner


# some images oer ther, doesn't have any names
# these are the build images

docker-compose up -d            # to run them together
# docker-engin ip :80

docker ps
docker compose down              # clean up


# once you are done sto 7 remove your docker engine
```

