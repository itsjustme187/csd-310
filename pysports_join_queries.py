import mysql.connector

config = {
    "user": 'pysports_user',
    "password": "1qaz@WSX",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

db = mysql.connector.connect(**config)
cursor = db.cursor()
cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON "
               "player.team_id = team.team_id;")
players = cursor.fetchall()
print("-- DISPLAYING PLAYER RECORDS --")

for x in players:
    print("Player ID: {}".format(x[0]), "\nFirst Name: {}".format(x[1]), "\nLast Name: {}".format(x[2]),
          "\nTeam ID: {}".format(x[3]), "\n")

print("")

input("Press any key to continue...")
