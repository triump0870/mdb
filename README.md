# [Movie Task][2]
----------------

 Movie Task app is an implementation for movie searching APIs. It is built with [Python][0] using the [Django Web Framework][1] and the APIs are implemented using [Django Rest Framework]. This app is deployed in [Heroku][3].

This project has the following basic apps:

* API -- This app handles all the API requests and responses
* Movie -- This app represents all the Movie and Genre models
* Account -- This app handles the user logins and registrations
* Profile -- This app is for personalizing the user profile

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


API Documentation
------------------------
This is Fynd Movie Task API resource documatation. To test the APIs use these demo users

    username: temp@temp.com
    password: temp

  username: demo@demo.com
  password: demo

The API provides endpoints for movies and users. It can be accessed via a simple API call.

The API defines the following endpoints:

> * https://movie-task.herokuapp.com/users/
> * https://movie-task.herokuapp.com/movies/

In case of an user request like,

    curl -v -H 'X-application/json' GET https://movie-task.herokuapp.com/api/users/1/

The JSON object returned would look like:

    HTTP 200 OK
    Content-Type: application/json
    Vary: Accept
    Allow: GET, HEAD, OPTIONS
    {
     "url": "http://localhost:8000/api/users/1/"
     "name": "Rohan",
     "email": "b4you0870@gmail.com",
     "movies": "http://localhost:8000/api/movies/1/"
     }

To create a Movie instance a request from an authenticated user would be like:

    curl -H 'X-application/json'
    -X POST https://movie-task.herokuapp.com/api/movies/ -u temp@temp.com:PASSWORD
    -d "name=The Dark Night&director=Christopher Nolan&imdb_score=9&popularity=82&release=2008-07-18&genres=Drama&genres=Action&genres=Crime"

The returned response would be like:

    POST /api/movies/ HTTP/1.1
    HTTP/1.1 201 CREATED
    Host: movie-task.herokuapp.com
    Content-Length: 132
    Content-Type: application/json
    Location: http://movie-task.herokuapp.com/api/movies/21/
    Allow: GET, POST, HEAD, OPTIONS

    {"url":"http://movie-task.herokuapp.com/api/movies/20/","name":"The Dark Night","director":"Christopher Nolan","genres":["Drama","Crime","Action"],"release":"2008-07-18","imdb_score":9.0,"popularity":82,"owner":"temp@temp.com"}

If the user is unauthenticated then the response would be

    HTTP 403 Forbidden

    Content-Type: application/json
    Vary: Accept
    Allow: GET, POST, HEAD, OPTIONS

    {
        "detail": "Permission denied."
    }

Filter can be applied on the following parameters:

> **`name`** -- `https://movie-task.herokuapp.com/api/movies/?name="Toy Story"`
>
> **`director`** --`https://movie-task.herokuapp.com/api/movies/?director='John Lasseter'`
>
> **`genre`** -- `https://movie-task.herokuapp.com/api/movies/?genre=Animation`
>
> or
> For multiple filter on Genre elements
> **`genre`** -- `https://movie-task.herokuapp.com/api/movies/?genre=Animation,Comedy`
>
> **`min_imdb`** -- `https://movie-task.herokuapp.com/api/movies/?min_imdb=8`
>
> **`max_imdb`** -- `https://movie-task.herokuapp.com/api/movies/?max_imdb=8`

[0]: https://www.python.org/
[1]: https://www.djangoproject.com/
[2]: https://movie-task.herokuapp.com/
[3]: https://www.heroku.com/)(http://www.django-rest-framework.org/

