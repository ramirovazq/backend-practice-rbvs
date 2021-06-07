# backend-practice-rbvs

## Overview
This project implements to implement a delivery system like is described https://docs.google.com/document/d/1EB1BJjVLNdD-Ce67GKkqvK9AZbYaEdbCNXKT-KXx2dk/

### Pre-requisites
* [Poetry](https://python-poetry.org/docs/)
* [Redis](https://redis.io/)
* python 3.7.0


### First steps
From clone to runserver
```sh
$ git clone git@github.com:ramirovazq/backend-practice-rbvs.git
$ cd backend-practice-rbvs/
$ poetry shell
$ poetry install
$ cd mealdelivery/
$ python manage.py runserver
```

### Shell
The shell command spawns a shell, according to the $SHELL environment variable, within
the virtual environment.
```sh
$ poetry shell
```

### Installing dependencies
The install command creates a virtual environment, resolves the dependencies
and installs them.
```sh
(.venv)$ poetry install
```


## Running tests
```sh
(.venv)$ python manage.py tests
```

## Start redis 
```sh
$ redis-server
```

## Verify Redis working properly
```sh
$ redis-cli ping
```

## Celery worker
```sh
(.venv)$ celery --app mealdelivery worker -l info
```

## Some details
https://docs.google.com/document/d/1ASSYFKRqQSlhZOcgDeVvS7T8Q4lsExAu9QtS23a9LWY/edit?usp=sharing
