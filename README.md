# PlateSearch
Accepts valid German license plates, stores them in a database and provides an endpoint to retrieve all stored plates.

The APIs could be seen and tested on https://platesearch.herokuapp.com/docs

For running the repo locally:
Install requirements from requirements.txt
Add fuzzystrmatch to postgres using this command: CREATE EXTENSION fuzzystrmatch SCHEMA public;
For the deployment on Heroku use this one, since the public in unaccessible: CREATE EXTENSION fuzzystrmatch SCHEMA heroku_ext;

