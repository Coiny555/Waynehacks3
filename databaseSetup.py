import sqlite3 #For SQLite
From sqlite3 import ERROR

db_file = "GameFinder.db"
  

def create_connection(db_file):

    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn



def main():

    database = "GameFinder.db"
    conn = create_connection(database)
    
    if conn is not None:
        sql_create_games_table = """ CREATE TABLE IF NOT EXISTS games (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    name TEXT NOT NULL,
                                    genre TEXT,
                                    estimated_playtime_per_session REAL, 
                                    difficulty TEXT,
                                    rating REAL,
                                    image_path TEXT 
                                ); """
        try:
            c = conn.cursor()
            c.execute(sql_create_games_table)
        except Error as e:
            print(f"Error creating table: {e}")
        conn.close()
    else:
        print("Error! cannot create the database connection.")

if __name__ == '__main__':
  main()