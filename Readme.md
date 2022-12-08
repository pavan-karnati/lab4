This API has two endpoints: /watchlist (used for both adding to and retrieving a watchlist) and /watchlist/<user> for retrieving a specific user's watchlist. To add a movie to a user's watchlist, you would make a POST request to the /watchlist endpoint with the user and movie in the request body. To retrieve a user's watchlist, you would make a GET request to the same endpoint, passing the user's name as a query parameter.

To run this program, you would need to have Python and Flask installed on your computer. You can check if you have Python installed by running the following command in your terminal:

```
python --version
```
If you don't have Python installed, you can download it from the Python website.

Once you have Python installed, you can install Flask by running the following command:

```
pip install Flask
```
After Flask is installed, you can run the program by saving the code to a file (e.g. watchlist_api.py) and running the following command:

```
FLASK_APP=watchlist_api.py flask run
```

This will start the Flask development server and make the API available at http://localhost:5000. You can then make requests to the endpoints using a tool like curl or by using a web browser. For example, to add a movie to a user's watchlist, you could run the following curl command:

```
curl -X POST --header 'Content-Type: application/json' 'http://127.0.0.1:5000/watchlist' -d '{"user": "johndoe","movie": "The Shawshank Redemption"}'
```

This would add the movie "The Shawshank Redemption" to the watchlist for the user "johndoe". To retrieve the user's watchlist, you could make a GET request to the same endpoint, passing the user's name as a query parameter:

```
curl http://localhost:5000/watchlist?user=johndoe
```

This would return the user's watchlist in JSON format.

### Dockerising the app

The Dockerfile uses the official Python image as the base image, copies the current directory into the container, installs Flask and other required dependencies, exposes port 5000, and runs the Flask development server when the container starts.

To build the Docker image, you can run the following command in the same directory as the Dockerfile:

```
docker build -t watchlist-api .
```

This will build a Docker image with the name watchlist-api. To run the image in a container, you can use the following command:

```
docker run -p 5000:5000 watchlist-api
```
This will run the container and make the Flask development server available at http://localhost:5000

### Using a database

To use Postgres as the database for the watchlist API, you would need to install the Postgres server and the psycopg2 Python driver. You can install the Postgres server by following the instructions on the Postgres website.

Once you have installed the Postgres server, you can create a new database and a user that has permission to access it. Here are the commands you would use to do this using the psql command-line interface:

```
# Connect to the "postgres" database as the "postgres" user
psql -U postgres

# Create a new database named "watchlists"
CREATE DATABASE watchlists;

# Create a new user named "watchlist_user" with the password "password"
CREATE USER watchlist_user WITH PASSWORD 'password';

# Grant the "watchlist_user" user permission to access the "watchlists" database
GRANT ALL PRIVILEGES ON DATABASE watchlists TO watchlist_user;
```
Once you have created the database and user, you can modify the code to use the psycopg2 driver to connect to the Postgres server and store the watchlists in the watchlists database.

### Using Docker compose to deploy both api and postgres as containers

This file defines two services: api and db. The api service is built using the Dockerfile in the current directory, exposes port 5000, and sets the DATABASE_URL environment variable to the connection string for the Postgres database. The db service uses the postgres:12 image, sets the POSTGRES_DB, POSTGRES_USER, and POSTGRES_PASSWORD environment variables to create the database and user, and exposes the default Postgres port (5432).
To deploy the services, you can run the following command in the same directory as the docker-compose.yml file:
```
docker-compose up
```
This will build the api service using the Dockerfile, start the db and api services, and make the watchlist API available at http://localhost:5000. You can then make requests to the API as described in the previous answers.

