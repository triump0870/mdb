# movie_task

movie_task is a _short description_. It is built with [Python][0] using the [Django Web Framework][1].

This project has the following basic apps:

* API
* Movie
* Account
* Profile

## Installation

### Quick start

To set up a development environment quickly, first install Python 3. It
comes with virtualenv built-in. So create a virtual env by:

1. `$ python3 -m venv movie_task`
2. `$ . movie_task/bin/activate`

Install all dependencies:

pip install -r requirements.txt

Run migrations:

python manage.py migrate

### Detailed instructions

Take a look at the docs for more information.


## API Documentation
==============
This is Fynd Movie Task API resource documatation.

The API provides endpoints for movies and users. It can be accessed via a simple API call.

The API defines the following endpoints:

* https://movie-task.herokuapp.com/users/
* https://movie-task.herokuapp.com/movies/

In case of a successful users request like,

* https://movie-task.herokuapp.com/api/users/1/

the JSON object returned looks like:

{
"url": "http://localhost:8000/api/users/1/"
"name": "Rohan",
"email": "b4you0870@gmail.com",
"movies": "http://localhost:8000/api/movies/1/"
}

In case of a successful movies request like,
https://movie-task.herokuapp.com/api/movies/1/

the JSON object returned looks like,

{
"url": "http://movie-task.herokuapp.com/api/movies/1/",
"name": "Toy Story",
"director": "John Lasseter",
"genres": [
"Adventure",
"Comedy",
"Animation"
],
"release": "2016-02-01",
"imdb_score": 8.3,
"popularity": 99.0,
"owner": "b4you0870@gmail.com"
}

If an unauthenticated / Anonymous user tries to create a Movie instance the following response will be generated

HTTP 403 Forbidden
Content-Type: application/json
Vary: Accept
Allow: GET, POST, HEAD, OPTIONS

{
    "detail": "Permission denied."
}


Filter can be applied on the following parameters:

**`name`** -- `https://movie-task.herokuapp.com/api/movies/?name="Toy Story"`

**`director`** --`https://movie-task.herokuapp.com/api/movies/?director='John Lasseter'`

**`genre`** -- `https://movie-task.herokuapp.com/api/movies/?genre=Animation`

or

**`genre`** -- `https://movie-task.herokuapp.com/api/movies/?genre=Animation,Comedy`

[0]: https://www.python.org/
[1]: https://www.djangoproject.com/
