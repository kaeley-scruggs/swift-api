# This is a sample Python script.
import mysql.connector
import database
import re

# Create the database and cursor
db_name = "Taylor_Swift"
mydb = mysql.connector.connect(
    host="localhost",
    port=3306,
    user=database.username,
    password=database.password,
    database=db_name
)
mycursor = mydb.cursor()
#----------------VARIABLES-------------------
# All album data song length is given in seconds
all_albums = [("Taylor Swift", "2006"),
#              ("Fearless", "2008"),
              ("Speak Now", "2010"),
#              ("Red", "2012"),
              ("1989", "2014"),
              ("Reputation", "2017"),
              ("Lover", "2019"),
              ("Folklore", "2020"),
              ("Evermore", "2020"),
#              ("Midnights", "2022"),
              ("THE TORTURED POETS DEPARTMENT", "2024"),
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
midnights_data = [("Lavender Haze", "202"),
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
                  ]


# -------------BEGIN FUNCTIONS------------------
def seconds_song_time(time):
    minutes = time // 60
    seconds = time % 60
    song_time = str(minutes) + ":" + str(seconds)
    return song_time


def song_time_to_seconds(time):
    minute_pattern = "(\d*):(\d*)"
    minute_matches = re.findall(minute_pattern, test_time)
    total = (int(minute_matches[0][0]) * 60) + int(minute_matches[0][1])
    return total


# ------------- DATABASE FUNCTIONS----------------
def show_database(cursor):
    mycursor.execute("SHOW DATABASES")
    for db in cursor:
        print(db)

def show_tables(cursor):
    mycursor.execute("SHOW TABLES")
    for tb in cursor:
        print(tb)



# use the following function ONCE with the all_albums variable -- it will create the tables for you
def create_tables_for_albums(list):
    for album in list:
        create_table = "CREATE TABLE " + album[0] + " (Track VARCHAR(255), Length INT(4))"
        mycursor.execute(create_table)
        print(create_table)
        mydb.commit()
# mycursor.execute("CREATE TABLE Albums (Name VARCHAR(255), Year INT(4))")
# mycursor.execute("CREATE TABLE Fearless (Track VARCHAR(255), Length INT(4))")
# mycursor.execute("SHOW TABLES")
# show_database(mycursor)
show_tables(mycursor)
print("==============")
mycursor.execute("SELECT * FROM Albums")
myresult = mycursor.fetchall()
for column in myresult:
    pass
    # print(column)
sqlFormual_add_albums = "INSERT INTO Albums (Name, Year) Values (%s, %s)"

sqlFormula_add_songs = "INSERT INTO Fearless (Track, Length) VALUES (%s, %s)"

def add_album_data():
    pass
# for item in fearless_data:
#    mycursor.execute(sqlFormula_add_songs, item)
# mydb.commit()


create_tables_for_albums(all_albums)
print("nothing")