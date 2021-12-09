import mysql.connector
from mysql.connector import errorcode

config = {
          "user": "reba0310",
          "password": "darlies10",
          "host": "127.0.0.1", 
          "database": "pysports",
          "raise_on_warnings": True
}
db = None
try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()
    cursor.execute("Select team_id, team_name, mascot from team")
    teams = cursor.fetchall()
    print("-- DISPLAYING TEAM RECORDS --")
    for team in teams:
        print("Team ID: {}\nTeam Name: {}\nMascot: {}\n".format(team[0], team[1], team[2]))

    cursor.execute("Select player_id, first_name, last_name, team_id from player")
    players = cursor.fetchall()
    print("-- DISPLAYING PLAYER RECORDS --")
    for player in players:
        print("PlayerID: {}\nFirst Name: {}\nLast Name: {}\nTeam ID: {}\n".format(player[0], player[1], player[2], player[3]))

    input ("\n\n Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specific database does not exist")
    else:
        print(err)
finally:
    if db is not None:
        db.close()
