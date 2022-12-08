import json
import psycopg2
from flask import Flask, request

app = Flask(__name__)

# Connect to the Postgres server
conn = psycopg2.connect(
  host='db',
  port=5432,
  user='watchlist_user',
  password='password',
  database='watchlists'
)
db = conn.cursor()
# Create the watchlists table if it doesn't already exist
command = (
        """
        CREATE TABLE IF NOT EXISTS watchlists (
            user_id VARCHAR(255) NOT NULL,
            movie VARCHAR(255) NOT NULL
        )
        """)
db.execute(command)

@app.route('/watchlist', methods=['POST'])
def add_to_watchlist():
  # Get the user_idand movie from the request body
  data = json.loads(request.data)
  user_id= data['user']
  movie = data['movie']

  # Add the movie to the user's watchlist in the database
  db.execute('INSERT INTO watchlists (user_id, movie) VALUES (%s, %s)', (user_id, movie))
  db.commit()

  # Return the updated watchlist
  db.execute('SELECT movie FROM watchlists WHERE user_id= %s', (user_id,))
  watchlist = db.fetchall()
  return json.dumps({'watchlist': [row[0] for row in watchlist]})

@app.route('/watchlist', methods=['GET'])
def get_watchlist():
  # Get the user_idfrom the request query parameters
  user_id= request.args.get('user')

  # Get the user's watchlist from the database
  db.execute('SELECT movie FROM watchlists WHERE user_id= %s', (user_id,))
  watchlist = db.fetchall()

  # Return the user's watchlist
  return json.dumps({'watchlist': [row[0] for row in watchlist]})
