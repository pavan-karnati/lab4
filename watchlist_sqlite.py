import json
import sqlite3
from flask import Flask, request

app = Flask(__name__)

# Connect to the SQLite database
db = sqlite3.connect('watchlists.db')

# Create the watchlists table if it doesn't already exist
db.execute('CREATE TABLE IF NOT EXISTS watchlists (user text, movie text)')

@app.route('/watchlist', methods=['POST'])
def add_to_watchlist():
  # Get the user and movie from the request body
  data = json.loads(request.data)
  user = data['user']
  movie = data['movie']

  # Add the movie to the user's watchlist in the database
  db.execute('INSERT INTO watchlists (user, movie) VALUES (?, ?)', (user, movie))
  db.commit()

  # Return the updated watchlist
  watchlist = db.execute('SELECT movie FROM watchlists WHERE user = ?', (user,)).fetchall()
  return json.dumps({'watchlist': [row[0] for row in watchlist]})

@app.route('/watchlist', methods=['GET'])
def get_watchlist():
  # Get the user from the request query parameters
  user = request.args.get('user')

  # Get the user's watchlist from the database
  watchlist = db.execute('SELECT movie FROM watchlists WHERE user = ?', (user,)).fetchall()

  # Return the user's watchlist
  return json.dumps({'watchlist': [row[0] for row in watchlist]})
