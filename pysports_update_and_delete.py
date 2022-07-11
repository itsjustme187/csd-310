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

cursor.execute("INSERT INTO player(first_name, last_name, team_id) "
               "VALUES('Smeagol', 'Shire Folk', 1);")
db.commit()
cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON "
               "player.team_id = team.team_id;")

players = cursor.fetchall()

print("-- DISPLAYING PLAYER AFTER INSERT --")
for x in players:
    print("Player ID: {}".format(x[0]), "\nFirst Name: {}".format(x[1]), "\nLast Name: {}".format(x[2]),
          "\nTeam Name: {}".format(x[3]), "\n")
print("")
try:
    db = mysql.connector.connect(**config)
    cursor1 = db.cursor()

    cursor1.execute("UPDATE player SET first_name = 'Gollum', last_name = 'Ring Stealer', team_id = 2 "
                    "WHERE first_name = 'Smeagol' ;")

    db.commit()

    cursor1.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON "
                    "player.team_id = team.team_id;")

    players1 = cursor1.fetchall()

    print("-- DISPLAYING PLAYER AFTER UPDATE --")

    for x in players1:
        print("Player ID: {}".format(x[0]), "\nFirst Name: {}".format(x[1]), "\nLast Name: {}".format(x[2]),
              "\nTeam ID: {}".format(x[3]), "\n")

finally:
    print("")

try:
    db = mysql.connector.connect(**config)
    cursor2 = db.cursor()

    cursor2.execute("DELETE FROM player WHERE first_name = 'Gollum';")

    db.commit()

    cursor2.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON "
                    "player.team_id = team.team_id;")

    players2 = cursor2.fetchall()

    print("-- DISPLAYING PLAYER AFTER DELETE --")

    for x in players2:
        print("Player ID: {}".format(x[0]), "\nFirst Name: {}".format(x[1]), "\nLast Name: {}".format(x[2]),
              "\nTeam ID: {}".format(x[3]), "\n")

finally:
    print("")


input("Press any key to continue...")
