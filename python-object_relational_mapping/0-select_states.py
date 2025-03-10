#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Récupérer les arguments de ligne de commande
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connexion à MySQL
    db = MySQLdb.connect(host="localhost", port=3306, user="user_0d_1", passwd="password123", db=database)

    # Créer un curseur pour exécuter la requête
    cursor = db.cursor()

    # Exécuter la requête pour récupérer les états triés par ID
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Récupérer les résultats
    rows = cursor.fetchall()

    # Afficher les résultats
    for row in rows:
        print(row)

    # Fermer le curseur et la connexion
    cursor.close()
    db.close()
