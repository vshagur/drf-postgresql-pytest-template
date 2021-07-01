## Install


#### Install Docker

You need to install Docker. Follow the instructions: [Install Docker](https://docs.docker.com/engine/installation/)

#### Install docker-compose

Follow the instructions - [Install Docker Compose](https://docs.docker.com/compose/install/#install-compose).

#### Configure Docker Management as a Non-Root User.

```
$ sudo groupadd docker
$ sudo gpasswd -a ${USER} docker
$ sudo service docker restart
$ sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
```
[More details.](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user)

#### Clone a project from the repository. 

```
$ git clone https://github.com/vshagur/wallet-rest-api.git
$ cd wallet-rest-api/
```
#### Configuration. 

Configuration. Replace the default settings with your own. If you are deploying a project for development, 
then leave the settings as they are

#### Build and initialize the project

###### Using Makefile: 
```
$ make init
```
Make sure the build was successful and run your tests.

```
$ make test
```
----------

###### Alternative way (using docker):

Build a container:

```
$ docker-compose build web
```

Check that the container with the database is not running:
```
$ docker-compose ps
```

If the container with the database is running, stop it:
```
$ docker-compose stop db
```

Apply migrations:
```
$ docker-compose run --rm web python manage.py migrate
```

Create superuser. Answer a few questions. For answers, use the data from the .env file:
```
$ docker-compose run --rm web python manage.py createsuperuser
```

Make sure the build was successful and run your tests.
```
$ docker-compose run --rm web pytest tests/
```
--------

#### Start up.

```
$ make run
```
or

```
$ docker-compose up
```
