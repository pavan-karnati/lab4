import json
from flask import Flask, request

app = Flask(__name__)

# Store the watchlists in a dictionary where the key is the user's name
# and the value is a list of movies
watchlists = {}

@app.route('/watchlist', methods=['POST'])
def add_to_watchlist():
  # Print the request body to check its contents
  

  # Get the user and movie from the request body
  data = json.loads(request.data)
  print(data)
  user = data['user']
  movie = data['movie']


  # Add the movie to the user's watchlist
  if user in watchlists:
    watchlists[user].append(movie)
  else:
    watchlists[user] = [movie]

  # Return the updated watchlist
  return json.dumps({'watchlist': watchlists[user]})

@app.route('/watchlist', methods=['GET'])
def get_watchlist():
  # Get the user from the request query parameters
  user = request.args.get('user')

  # Return the user's watchlist
  return json.dumps({'watchlist': watchlists[user]})
