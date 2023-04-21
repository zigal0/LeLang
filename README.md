# LeLang
## Description
### General
Web application dedicated to the study of languages.
### What can you do?
* SignUp, login & logout. 
* Add new terms. Currently, it supports 2 languages (en, ru).
* Browse your terms divided by languages in tables.
* Learning mode with cards.
## Run project
* Create new venv and activate it.

* Set up dependencies:
  * Type `make setup`;
  * Install docker with docker compose or postgres server.

* Make `.env` file with secrets in it. For help - example.env.

* Run project:
  * if you have docker - type `make run-full` in terminal
  * if you have postgres server:
    1. In `.env` file make PG_DB_PORT=5432;
    2. Type `make migrate` interminal; 
    3. Type `make run`.

If you want to know more how to run app - look at `Makefile`.


