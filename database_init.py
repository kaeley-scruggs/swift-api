# This is a sample Python script.
import sqlite3
import secrets
import re
# plugin - SimpleSqliteBrowser

def _connect():
    return sqlite3.connect(secrets.db_path)
def table_validation(table):
    approved = False
    allow_tb_list = ["Albums",
                     "Taylor Swift",
                     "Fearless",
                     "Speak Now",
                     "Red",
                     "1989",
                     "Reputation",
                     "Lover",
                     "Folklore",
                     "Evermore",
                     "Midnights",
                     "THE TORTURED POETS DEPARTMENT",
                     ""
                     ]
    illegal_char = ["\\", "/", "LIKE", "like"]
    for char in illegal_char:
        if char in table:
            return approved
        if table in allow_tb_list:
            approved = True
    return approved


#----------------VARIABLES-------------------
# All album data song length is given in seconds
all_albums = [("Taylor Swift", "2006", "Green"),
              ("Fearless", "2008", "Yellow"),
              ("Speak Now", "2010", "Purple"),
              ("Red", "2012", "Red"),
              ("1989", "2014", "Light Blue"),
              ("Reputation", "2017", "Black"),
              ("Lover", "2019", "Pink"),
              ("Folklore", "2020", "Grey"),
              ("Evermore", "2020", "Orange"),
              ("Midnights", "2022", "Navy Blue"),
              ("THE TORTURED POETS DEPARTMENT", "2024", "White"),
              ]

fearless_data = [
                ("Fearless", "241"),
                ("Fifteen", "294"),
                ("Love Story", "235"),
                ("Hey Stephen", "254"),
                ("White Horse", "234"),
                ("You Belong With Me", "231"),
                ("Breathe", "263"),
                ("Tell Me Why", "200"),
                ("You're Not Sorry", "261"),
                ("The Way I Loved You", "244"),
                ("Forever & Always", "225"),
                ("The Best Day", "245"),
                ("Change", "280"),
                ]
red_data = [
            ("State of Grace", "295"),
            ("Red", "220"),
            ("Treacherous", "240"),
            ("I Knew You Were Trouble.", "217"),
            ("All Too Well", "327"),
            ("22", "230"),
            ("I Almost Do", "242"),
            ("We Are Never Ever Getting Back Together", "191"),
            ("Stay Stay Stay", "204"),
            ("The Last Time", "298"),
            ("Holy Ground", "201"),
            ("Sand Beautiful Tragic", "283"),
            ("The Lucky One", "240"),
            ("Everything Has Changed", "243"),
            ("Starlight", "217"),
            ("Begin Again", "237"),
            ]
midnights_data1 = {
    "album_name": "Midnights",
    "song_list": [("Lavender Haze", "202"),
                  ("Maroon", "218"),
                  ("Anti-Hero", "200"),
                  ("Snow On the Beach (feat. Lana Del Rey", "256"),
                  ("You're On Your Own, Kid", "194"),
                  ("Midnight Rain", "174"),
                  ("Quesiton...?", "219"),
                  ("Vigilante Shit", "164"),
                  ("Bejewled", "194"),
                  ("Labyrinth", "247"),
                  ("Karma", "204"),
                  ("Sweet Nothing", "188"),
                  ("Mastermind", "191"),
                  ],
    }


# -------------BEGIN FUNCTIONS------------------
def seconds_song_time(time):
    minutes = time // 60
    seconds = time % 60
    song_time = str(minutes) + ":" + str(seconds)
    return song_time


def song_time_to_seconds(time):
    minute_pattern = "(\d*):(\d*)"
    minute_matches = re.findall(minute_pattern, time)
    total = (int(minute_matches[0][0]) * 60) + int(minute_matches[0][1])
    return total


# ------------- DATABASE FUNCTIONS----------------
def create_populate_album_table():
    sqlformula_add_albums = "INSERT INTO Albums (Name, Year, Color) Values (%, %, %)"
    with _connect() as conn:
        my_cursor = conn.cursor()
        my_cursor.execute("""CREATE TABLE 'Albums' (
                              al_id INTEGER PRIMARY KEY,
                              Name text,
                              Year INTEGER,
                              Color text,
                              """)
        for db in my_cursor:
            print(db)
        for name in all_albums:
            print(name[0])
            my_cursor.execute(sqlformula_add_albums, (name[0], name[0], name[0]))


create_populate_album_table()
def show_database():
    with _connect() as conn:
        my_cursor = conn.cursor()
        my_cursor.execute("SHOW DATABASES")
        for db in my_cursor:
            print(db)


def show_tables():
    with _connect() as conn:
        my_cursor = conn.cursor()
        my_cursor.execute("SHOW TABLES")
    for tb in my_cursor:
        print(tb)


# use the following function ONCE with the all_albums variable -- it will create the tables for you
def create_tables_for_all_albums(album_list):
    for album in album_list:
        if table_validation(album) is True:
            with _connect() as conn:
                my_cursor = conn.cursor()
                create_table = "CREATE TABLE " + album[0] + " (Track VARCHAR(255), Length INT(4))"
                my_cursor.execute(create_table)
                print(create_table)
        else:
            print(album[0] + " is not a valid table")

midnights_data = {
    "album_name": "Midnights",
    "song_list": [("Lavender Haze", "202"),
                  ("Maroon", "218"),
                  ("Anti-Hero", "200"),
                  ("Snow On the Beach (feat. Lana Del Rey", "256"),
                  ("You're On Your Own, Kid", "194"),
                  ("Midnight Rain", "174"),
                  ("Quesiton...?", "219"),
                  ("Vigilante Shit", "164"),
                  ("Bejewled", "194"),
                  ("Labyrinth", "247"),
                  ("Karma", "204"),
                  ("Sweet Nothing", "188"),
                  ("Mastermind", "191"),
                  ],
    }
def populate_album_tables(album_data):
    with _connect() as conn:
        my_cursor = conn.cursor()
        sqlformula_add_songs = "INSERT INTO " + album_data["album_name"] + " (Track, Length) VALUES (?, ?)"
        for song in album_data[1]:
            print("formula:", sqlformula_add_songs)
            print("+++++++++++++++++++++++++++++++++++++")
            print("data:", (song[0], song[1]))

populate_album_tables(midnights_data)