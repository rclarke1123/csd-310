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

    cursor.execute("INSERT INTO player (first_name, last_name, team_id) " + 
                   "VALUES ('Bob', 'Coates', 1)")

    cursor.execute("SELECT player_id, first_name, last_name, team_name " + 
                   "FROM player INNER JOIN team " + 
                   "ON player.team_id = team.team_id;")
    playerRecords = cursor.fetchall()
    print("-- DISPLAYING PLAYERS AFTER INSERT --")
    for player in playerRecords:
        print("PlayerID: {}\nFirst Name: {}\nLast Name: {}\nTeam Name: {}\n".format(player[0], player[1], player[2], player[3]))

    cursor.execute("UPDATE player " + 
                   "SET team_id = 2 " +
                   "WHERE first_name = 'Bob' AND last_name = 'Coates'")

    cursor.execute("SELECT player_id, first_name, last_name, team_name " + 
                   "FROM player INNER JOIN team " + 
                   "ON player.team_id = team.team_id;")
    playerRecords = cursor.fetchall()
    print("-- DISPLAYING PLAYERS AFTER UPDATE --")
    for player in playerRecords:
        print("PlayerID: {}\nFirst Name: {}\nLast Name: {}\nTeam Name: {}\n".format(player[0], player[1], player[2], player[3]))


    cursor.execute("DELETE FROM player " + 
                   "WHERE first_name = 'Bob' AND last_name = 'Coates'")

    cursor.execute("SELECT player_id, first_name, last_name, team_name " + 
                   "FROM player INNER JOIN team " + 
                   "ON player.team_id = team.team_id;")
    playerRecords = cursor.fetchall()
    print("-- DISPLAYING PLAYERS AFTER DELETE --")
    for player in playerRecords:
        print("PlayerID: {}\nFirst Name: {}\nLast Name: {}\nTeam Name: {}\n".format(player[0], player[1], player[2], player[3]))

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
