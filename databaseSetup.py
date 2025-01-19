import sqlite3 #For SQLite
from sqlite3 import Error

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
                                    estimated_playtime_per_session TEXT,
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


"""
 -- Insert statements for the games table 
INSERT INTO games (id, name, genre, estimated_playtime_per_session, difficulty, rating, image_path) 
VALUES ('Anthem', 'RPG, Action', 'Varies Greatly', 'Medium', 6.3, 'images/anthem.webp');

INSERT INTO games (id, name, genre, estimated_playtime_per_session, difficulty, rating, image_path) 
VALUES ('Assassins Creed Unity', 'Action, Adventure', 'Varies Greatly', 'Medium', 7.1, 'images/assassins_creed_unity.webp');

INSERT INTO games (id, name, genre, estimated_playtime_per_session, difficulty, rating, image_path) 
VALUES ('Balatro', 'Card Roguelike', 0.75, 'Easy', 4.8, 'images/balatro.webp');

INSERT INTO games (id, name, genre, estimated_playtime_per_session, difficulty, rating, image_path) 
VALUES ('Celeste', 'Platformer', 1.0, 'Medium', 8.7, 'images/celeste.webp');

INSERT INTO games (id, name, genre, estimated_playtime_per_session, difficulty, rating, image_path) 
VALUES ('Cuphead', 'Run & Gun, Platformer', 0.75, 'Hard', 9.0, 'images/cuphead.webp');

INSERT INTO games (id, name, genre, estimated_playtime_per_session, difficulty, rating, image_path) 
VALUES ('Cyberpunk 2077', 'RPG, Action', 'Varies Greatly', 'Medium', 8.2, 'images/cyberpunk_2077.webp');

INSERT INTO games (id, name, genre, estimated_playtime_per_session, difficulty, rating, image_path) 
VALUES ('Dead Cells', 'Roguelike', 1.0, 'Medium', 8.3, 'images/dead_cells.webp');

INSERT INTO games (id, name, genre, estimated_playtime_per_session, difficulty, rating, image_path) 
VALUES ('Dead Island', 'Action, Beat em Up', 'Varies Greatly', 'Medium', 7.1, 'images/dead_island.webp');

INSERT INTO games (id, name, genre, estimated_playtime_per_session, difficulty, rating, image_path) 
VALUES ('Fallout 76', 'RPG, Action', 'Varies Greatly', 'Medium', 6.0, 'images/fallout_76.webp');

INSERT INTO games (id, name, genre, estimated_playtime_per_session, difficulty, rating, image_path) 
VALUES ('Hades', 'Roguelike', 1.0, 'Hard', 9.1, 'images/hades.webp');

INSERT INTO games (id, name, genre, estimated_playtime_per_session, difficulty, rating, image_path) 
VALUES ('Hollow Knight', 'Metroidvania', 1.5, 'Hard', 9.2, 'images/hollow_knight.webp');

INSERT INTO games (id, name, genre, estimated_playtime_per_session, difficulty, rating, image_path) 
VALUES ('Mass Effect: Andromeda', 'RPG, Action', 'Varies Greatly', 'Medium', 7.1, 'images/mass_effect_andromeda.webp');

INSERT INTO games (id, name, genre, estimated_playtime_per_session, difficulty, rating, image_path) 
VALUES ('Minecraft', 'Sandbox, Survival', 'Varies Greatly', 'Easy', 8.1, 'images/minecraft.webp');

INSERT INTO games (id, name, genre, estimated_playtime_per_session, difficulty, rating, image_path) 
VALUES ('No Mans Sky', 'Exploration, Survival', 'Varies Greatly', 'Medium', 7.1, 'images/no_mans_sky.webp');

INSERT INTO games (id, name, genre, estimated_playtime_per_session, difficulty, rating, image_path) 
VALUES ('Ori and the Blind Forest', 'Metroidvania', 1.0, 'Medium', 8.7, 'images/ori_and_the_blind_forest.webp');

INSERT INTO games (id, name, genre, estimated_playtime_per_session, difficulty, rating, image_path) 
VALUES ('Portal 2', 'Puzzle, Platformer', 1.5, 'Medium', 9.2, 'images/portal_2.webp');

INSERT INTO games (id, name, genre, estimated_playtime_per_session, difficulty, rating, image_path) 
VALUES ('Red Dead Redemption 2', 'Shooter, RPG', 2.0, 'Medium', 9.3, 'images/red_dead_redemption_2.webp');

INSERT INTO games (id, name, genre, estimated_playtime_per_session, difficulty, rating, image_path) 
VALUES ('Slay the Spire', 'Card Roguelike', 1.0, 'Medium', 8.6, 'images/slay_the_spire.webp');

INSERT INTO games (id, name, genre, estimated_playtime_per_session, difficulty, rating, image_path) 
VALUES ('Sonic Generations', 'Platformer, Adventure', 1.0, 'Easy', 7.0, 'images/sonic_generations.webp');

INSERT INTO games (id, name, genre, estimated_playtime_per_session, difficulty, rating, image_path) 
VALUES ('Stardew Valley', 'RPG, Simulation', 1.5, 'Easy', 8.7, 'images/stardew_valley.webp');

INSERT INTO games (id, name, genre, estimated_playtime_per_session, difficulty, rating, image_path) 
VALUES ('Streets of Rage 4', 'Fighting, Beat em Up', 0.75, 'Medium', 8.1, 'images/streets_of_rage_4.webp');

INSERT INTO games (id, name, genre, estimated_playtime_per_session, difficulty, rating, image_path) 
VALUES ('Super Mario Odyssey', 'Platformer', 1.0, 'Easy', 8.9, 'images/super_mario_odyssey.webp');

INSERT INTO games (id, name, genre, estimated_playtime_per_session, difficulty, rating, image_path) 
VALUES ('Team Fortress 2', 'Shooter', 1.5, 'Easy', 8.3, 'images/team_fortress_2.webp');

INSERT INTO games (id, name, genre, estimated_playtime_per_session, difficulty, rating, image_path) 
VALUES ('Tetris Effect', 'Puzzle', 0.75, 'Easy', 8.7, 'images/tetris_effect.webp');

INSERT INTO games (id, name, genre, estimated_playtime_per_session, difficulty, rating, image_path) 
VALUES ('The Legend of Zelda: Breath of the Wild', 'Action-Adventure', 2.0, 'Medium', 9.3, 'images/the_legend_of_zelda_breath_of_the_wild.webp');

INSERT INTO games (id, name, genre, estimated_playtime_per_session, difficulty, rating, image_path) 
VALUES ('Uncharted 2', 'Shooter, Adventure', 2.0, 'Medium', 4.9, 'images/uncharted_2.webp');

INSERT INTO games (id, name, genre, estimated_playtime_per_session, difficulty, rating, image_path) 
VALUES ('Undertale', 'Puzzle, RPG', 1.5, 'Medium', 8.7, 'images/undertale.webp');

INSERT INTO games (id, name, genre, estimated_playtime_per_session, difficulty, rating, image_path) 
VALUES ('Unpacking', 'Puzzle, Simulation', 0.75, 'Easy', 7.3, 'images/unpacking.webp');

INSERT INTO games (id, name, genre, estimated_playtime_per_session, difficulty, rating, image_path) 
VALUES ('Yakuza 0', 'Action-Adventure', 1.5, 'Medium', 8.7, 'images/yakuza_0.webp');

INSERT INTO games (id, name, genre, estimated_playtime_per_session, difficulty, rating, image_path) 
VALUES ('Call of Duty Black Ops 6', 'Shooter', 1.5, 'Medium', 7.5, 'images/cod_black_ops_6.webp');
"""