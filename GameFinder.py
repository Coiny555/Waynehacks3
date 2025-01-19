from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask! Goodbye boi!"

if __name__ == '__main__':
    app.run(debug=True)

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

#This is, I believe a test file to set up flask, may make changes later