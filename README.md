# Test task with Django Rest Framework (DRF)


## Test task

1. Create a two model:
  * Post
    - title
    - text
    - views amount
    - creation date
  * Comment (depend from post)
    - text
    - creation date
2. Added functional of creation post and admin throught from admin panel
3. Write the api for getting all posts and check specify post:
  * API list of Post:
    - in element make output last comment;
  * API detail of Post:
    - after every post detail query, add one view;
    - out all post comments;

My initiate create a custom auth system for test manually, write the tests and add docker support =)

## Project quickstart
  Project use [Poetry](https://python-poetry.org/) package manager, dependencies dump in repo
  You can use docker for start the project, just run:
  `sudo docker compose up --build`
  And project start on url: `http://127.0.0.1:43202/docs/`


  Or, you can start project with local env, in this case do this:
  `poetry init`
  `poetry install`
  `python manage.py runserve 8000`
  In this case, you can find project on url `http://127.0.0.1:8000/docs/`


  If you don't have a poetry install it from [official site](https://python-poetry.org/)


## Work with tests
  Test are divided on tags, for start all tests use this command:
  `python manage.py test`

  Or use tags for test specify controller:
  `python manage.py test --tag=post_list`

  All tags:
    * Posts (tag: post) specify:
      - post_list - test post list controller
      - post_create - test post creation controller
      - post_detail - test post detail view (retrieve, update, delete) controller
    * Comments:
      - maybe will comming...
    * Custom Auth (tag: custom_auth) specify:
      - login - test login controller
      - logout - test logout contoller


## Table with timetracking

| Time             	| Action                                                                       	|
|------------------	|------------------------------------------------------------------------------	|
| 2023-01-30 10:49 	| Initializate project                                                         	|
| 12:08            	| AFK                                                                          	|
| 12:27            	| Create a posts app, post app models                                          	|
| 12:41            	| Added work with posts models in admin panel                                  	|
| 13:24            	| Create a first posts views, added output list of posts and creation of post  	|
| 14:00            	| Added permissions and complete work with post controllers                    	|
| 14:51            	| AFK                                                                          	|
| 15:23            	| Added self generated docs (swagger)                                          	|
| 16:08            	| Added simple auth system, added services folder and a little refactor routes 	|
| 17:23            	| Added last comment to posts output                                           	|
| 18:17            	| Work with add all comments to post detail                                    	|
| 21:47            	| AFK                                                                          	|
| 21:48            	| Complete output all comments in post detail                                  	|
| 21:56            	| Complete view add functional                                                 	|
| 23:37            	| Start write the tests, install additional dependencies for tests             	|
| 09:45            	| AFK                                                                          	|
| 10:37            	| Completed post list tests; Refactor post list and post create routes         	|
| 11:55            	| Completed post create route test, start fill readme.md                       	|
| 12:16            	| AFK                                                                          	|
| 12:52            	| Start write post detail tests                                                	|
| 15:02            	| AFK                                                                          	|
| 16:15            	| Complete tests with post entity                                              	|
| 17:56            	| Complete tests for custom auth                                               	|
