# ContaBk

## Description

A quick REST-based application for contact management. This started our as a project to prove my capabilities writing simple full-stack apps, so there are no bells and whistles involved. By all accounts, you could consider this your basic CRUD app.

Technologies used:

* Python
* Flask
* SQLAlchemy
* SQLite
* JavaScript
* React
* NodeJS

## How to run

You must run two terminals, one for the backend and one for the frontend. The backend must be running in order for the frontend to be able to fetch data.

### Frontend:

Navigate to the frontend directory in the terminal. If this is a fresh copy, run **`npm install`**.

Afterwards, you can start the frontend by typing **`npm start`**.

You will be able to connect at URL **http://localhost:3000/**

###  Backend:

If this is your first time running the server, first create a virtual environment:

`python3 -m venv NAME`

Then activate it:

`source PATH_TO_BACKEND/ENV_NAME/bin/activate`

Finally, run `pip install -r requirements.txt`

Now you should be all set.

=======================

The backend uses environment variables to initialize. Before running the server, run the following commands:

`export PYTHONPATH=~/ContaBk/backend`

`export DEV_DATABASE_URL=sqlite:///contacts.db`

Now you can open the server with

`flask run`

### Caution:

This application is made to run locally only and should not be considered deployment ready. The configuration you would be using is still the development configuration.





## License

Short answer: GNU GPLv3.

Long answer: See the LICENSE file.