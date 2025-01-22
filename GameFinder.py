from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/') #For the pages on the app 
def home():
    return render_template('home.html')

@app.route('/about') #For the about page
def about():
    return render_template("about.html")


@app.route('/recommendations', methods=['POST'])
def recommendations():
    data = request.json  # Get data from the POST request
    genre = data.get('genre')  # Extract genre from form data
    difficulty = data.get('difficulty')  # Extract difficulty from form data
    playtime = int(data.get('playtime'))  # Extract playtime and ensure it's an integer
    
    # Query the database for matching games
    games = query_games(genre, difficulty, playtime)
    
    # Return the games as a JSON response
    return jsonify(games)

def query_games(genre, difficulty, estimated_playtime_per_session):
    conn = sqlite3.connect('GameFinder.db')
    cursor = conn.cursor()
    query = """
        SELECT name, genre, difficulty, estimated_playtime_per_session, image_path
        FROM games
        WHERE genre LIKE '%' || ? || '%' 
          AND difficulty = ?
          AND estimated_playtime_per_session <= ?
        ORDER BY estimated_playtime_per_session ASC;
    """
    cursor.execute(query, (genre, difficulty, estimated_playtime_per_session))
    results = cursor.fetchall()
    conn.close()
    return results


if __name__ == '__main__':
    app.run(debug=True)

#This is, I believe a test file to set up flask, may make changes later