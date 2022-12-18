##pysports_join_queries.py
##Module 9.2 Assignment - Working with Basic Table Joins
##Data/Database Security 
##Ahmed Bushra

##Requirement below-----
##create an INNER JOIN query to connect the player and team tables by team_id and display the results

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

    ##Query for Player Table for the following values: player_id, first_name, last_name, & team_id + INNER JOIN with team_id from team table
    ##Received Exception has occurred: Integrity Error 1052 (23000): Column 'team_id' in field list is ambiguous. Changed team_id from prior queries script to team_name
    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id;")

    ##Pulling results
    players = cursor.fetchall()

    ##Player records section output display
    print("-- DISPLAYING PLAYER RECORDS --")

    ##Fulfilling iteration over cursor to display results
    for player in players:
        print(" Player ID: {}\n First Name: {}\n Last Name: {}\n Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

finally:
    """Closing try block"""

##Input to end program
input(" Press any key to continue...")