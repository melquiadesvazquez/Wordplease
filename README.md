# Wordplease

[![MIT License][license-image]][license-url]

Website similar to https://medium.com (blogging platform) built with Python, Django and Django REST Framework.

Live demo available on https://melwordplease.herokuapp.com

## Prerequisites

You need to install the following software on your machine before running this project:

1. Python  &ndash; <https://www.python.org/>
2. pip (Python package manager)  &ndash; <https://pip.pypa.io/en/latest/installing/>

To continue the installation you can follow this tutorial  <https://docs.djangoproject.com/en/2.1/intro/install/>

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

Download the repository from GitHub

```shell
git clone https://github.com/melquiadesvazquez/Wordplease.git
cd Wordplease
```

Setup the virtual env for Linux

```
python -m venv env
source env/bin/activate
```

Setup the virtual env for Windows

```
python -m venv env
.\env\Scripts\activate
```

Install de project with pip

```shell
cd Wordplease
pip install -r requirements.txt
```

Copy .env.example to .env and review the values to match your preferences.

```shell
mv .env.example .env
```

Create database

```shell
python manage.py migrate
```

Create superuser

```shell
python manage.py createsuperuser
```

Import the sample database

```shell
python manage.py loaddata db.json
```

Get a development environment running
```shell
python manage.py runserver
```

## Testing website

Open your browser and go to:

+ Website &ndash; http://127.0.0.1:8000
+ Alternatively, check the live demo [here](https://melwordplease.herokuapp.com/)

![Melpress homepage](https://raw.githubusercontent.com/melquiadesvazquez/MelPress/master/src/assets/web1.jpg)

![Melpress post page](https://raw.githubusercontent.com/melquiadesvazquez/MelPress/master/src/assets/web2.jpg)

## RESTful API services

The following endpoints are available (end slash is mandatory):

### Users API

+ `POST /api/v1/users/<id>/` Any user can register using:

```json
{
	"first_name": "test",
	"last_name": "test",
	"username": "test",
	"email": "test@test.com",
	"password": "test"
}
```

+ `GET /api/v1/users/<id>/` Only admin and authenticated users will be able to display their own account's detail.
+ `PUT /api/v1/users/<id>/` Only admin and authenticated users will be able to update their own account.
+ `DELETE /api/v1/users/<id>/` Only admin and authenticated users will be able to delete their own account.

### Blogs API

+ `GET /api/v1/blogs/` Any user can display a list of urls from the blogs available in the platform. 
+ `GET /api/v1/blogs/?search=test&ordering=title&owner_username=test` Standard parameters are available for searching, ordering and filtering 


### Posts API

+ `GET /api/v1/posts/` Any user can display the published posts and the owned unpublished when authenticated
+ `GET /api/v1/posts/?search=test&ordering=pub_date&status=PUB` Standard parameters are available for searching, ordering and filtering 
+ `POST /api/v1/posts/` Admin and authenticated users will be able to publish posts on their own blogs. If the parameter blog is not present, the post will be assigned to one of the blogs of the user
```json
{
    "title": "this is the title",
    "description": "this is the description",
    "content": "this is the content",
    "video": "https://www.youtube.com/embed/1CRihg1X89A",
    "status": "PUB"
}
```

+ `GET /api/v1/posts/<id>/` Any user will be able to display a post's detail as long as it's published.
+ `PUT /api/v1/posts/<id>/` Only admin and authenticated users will be able to update their own post.
+ `DELETE /api/v1/posts/<id>/` Only admin and authenticated users will be able to delete their own account.

### Files API

+ `GET /api/v1/files/`  Only admin and authenticated users will be able to display the files 
+ `POST /api/v1/files/` Only admin and authenticated users will be able to upload files 

## Built with

+ [Nodejs](https://nodejs.org/) - JavaScript run-time environment
+ [Webpack](https://webpack.js.org/) - JavaScript module bundler
+ [JSON server](https://github.com/typicode/json-server) - REST API with CRUD operations based on a json file
+ [SASS](https://sass-lang.com/) - CSS preprocessor scripting language

## Restrictions

+ The live demo is connected with a third party JSON server on https://my-json-server.typicode.com, due to this, database updates are not allowed and new comments won't be created. However, that functionality should work on local.

## License

[MIT][license-url]


[license-image]: http://img.shields.io/badge/license-MIT-blue.svg?style=flat
[license-url]: LICENSE
