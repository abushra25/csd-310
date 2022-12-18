##pysports_queries 
##Module 8.3 Assignment
##Data/Database Security
##Ahmed Bushra

##Requirements below-----

##Write two select queries, one for the team table and one for the player table.
#For Team Table: SELECT team_id, team_name, & mascot
#For Player Table: SELECT player_id, first_name, last_name, & team_id
##Use a for loop to iterate over cursor and display the results

##Imports##
import mysql.connector 
from mysql.connector import errorcode

##Database config object to access local DB with specified credentials##
config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

##Try block necessary otherwise "Press any key to continue..." is requested before displaying next block of player data.
try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    ##The select query for Team Table for the following values: team_id, team_name, & mascot
    cursor.execute("SELECT team_id, team_name, mascot FROM team")
    
    ##Pulling results
    teams = cursor.fetchall()

    ##Team records section output display
    print("-- DISPLAYING TEAM RECORDS -- ")

    ##Fulfilling iteration over cursor to display results. "Index 2 out of range for positional args tuple" received when running only
    # "team[1], team[2]". The format must match the number of arguments passed.
    for team in teams:
        print(" Team ID: {}\n Team Name: {}\n Mascot: {}\n".format(team[0], team[1], team[2]))

    ##The select query for Player Table for the following values: player_id, first_name, last_name, & team_id
    cursor.execute("SELECT player_id, first_name, last_name, team_id FROM player")

    ##Pulling results
    players = cursor.fetchall()

    ##Player records section output display
    print("-- DISPLAYING PLAYER RECORDS --")

    ##Fulfilling iteration over cursor to display results
    for player in players:
        print(" Player ID: {}\n First Name: {}\n Last Name: {}\n Team ID: {}\n".format(player[0], player[1], player[2], player[3]))

##Closing try block
finally:
    """Closing try block"""

##Input to end program
input(" Press any key to continue...")
