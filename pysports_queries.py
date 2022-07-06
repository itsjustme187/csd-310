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
cursor.execute("SELECT team_id, team_name, mascot FROM team;")
teams = cursor.fetchall()
cursor2 = db.cursor()
cursor2.execute("SELECT player_id, first_name, last_name, team_id FROM player;")
players = cursor2.fetchall()
print("-- DISPLAYING TEAM RECORDS --")

for x in teams:
    print("Team ID: {}".format(x[0]), "\nTeam Name: {}".format(x[1]), "\nMascot: {}".format(x[2]), "\n")

print("")
print("-- DISPLAYING PLAYER RECORDS --")
for x in players:
    print("Player ID: {}".format(x[0]), "\nFirst Name: {}".format(x[1]), "\nLast Name: {}".format(x[2]), 
          "\nTeam ID: {}".format(x[3]), "\n")

print("")
input("End of program, press any key to continue...")
