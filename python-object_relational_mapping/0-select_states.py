#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Récupération des arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connexion à la base de données
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Création d'un curseur pour exécuter des requêtes SQL
    cur = db.cursor()

    # Exécuter la requête SQL pour récupérer les états triés par id
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Récupérer et afficher les résultats
    for row in cur.fetchall():
        print(row)

    # Fermeture du curseur et de la connexion
    cur.close()
    db.close()
