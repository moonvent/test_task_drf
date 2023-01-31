# Test task with Django Rest Framework (DRF)


## Test task

Will comming soon...


## Project quickstart
  Project use [Poetry](https://python-poetry.org/) package manager, dependencies dump in repo
  You can use docker for start the project, just run:
  `sudo docker compose up --build`
  And project start on url: `http:127.0.0.1:43202`


  Or, you can start project with local env, in this case do this:
  `poetry init`
  `poetry install`
  `python manage.py runserve 8000`


  If you don't have a poetry install it from [official site](https://python-poetry.org/)


## Work with tests
  Test are divided on tags, for start all tests use this command:
  `python manage.py test`

  Or use tags for test specify controller:
  `python manage.py test --tag=post_list`

  All tags:
    * Posts
      - post_list - test post list controller
      - post_create - test post creation controller


## Table with timetracking

Table will comming soon...
