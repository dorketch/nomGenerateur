#!/usr/bin/env python3
from optparse import OptionParser
import sqlite3

#(derelict)Fonction pour crée la base de données
#Cette fonction ne doit plus être utlisé, la bd a été remplis
# def createInitialTable():p
#     cursor.executescript("""
#     BEGIN;
#     CREATE TABLE prenom(prenom, genre);
#     CREATE TABLE nom(nom, nationalite);
#     COMMIT;
# """)

 #pour avoir des options en ligne de commandes on utilise optparse.
parser = OptionParser()
parser.add_option("-n","--nombre", type="int", dest="num", help="NUM est egal au nombres de nom qu'on veut generer." )
(options, args) = parser.parse_args()

basededonnee = "nom.db" #nom du fichier de base de donnée pour SQLITE3
connection = sqlite3.connect(basededonnee) #Pour connecter a la Base de données
cursor = connection.cursor()#chaques commandes doit être executé par un objet curseur

#fonctions pour vérifier ce qui se trouve dans la base de donnée SQlite
def readall():

    res = cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    print("Tout les tableaux qui ont été crée")
    print(res.fetchall())


def readallnom():

    res = cursor.execute("SELECT * FROM nom")
    print("Tout les noms dans la BD")
    print(res.fetchall())


def readallprenom():

    res = cursor.execute("SELECT * FROM prenom")
    print("Tout les prénoms dans la BD")
    print(res.fetchall())


def debug():
    """Fonction pour imprimé tout ce qui est dans la Base de donnée"""
    readall()
    readallnom()
    readallprenom()

def randomprenom(nbprenom=1):
    res = cursor.execute("select prenom from prenom order by random() limit " + str(nbprenom))
    for resultat in res.fetchall():
        return resultat
    
#Fonction pour obtenir un nom au hazard
def randomnom(nbnom=1):
    """Retourne une liste"""
    res = cursor.execute("select nom from nom order by random() limit " + str(nbnom))
    for resultat in res.fetchall():
        return resultat

#Fonction pour obtenir un prénom et nom de famille
#Fonction pour fabriquer des nom complet dans le format prenom + nom.
def randomfull():
    """ 
    Fonction pour génerer un nom fomplet dans le format Prénom + nom.
    la fonction utilise les deux autres fonctions aléatoire et une boucle
    while pour fabriquer le nombre de noms voulu. Sans arguments la fonction
    donne seulement 1 nom.
    """
    resultat = randomprenom(nb)+" "+randomnom(nb)
    
    return resultat

#Fonction pour ajouter une entrée
def insertNom(nom, genre, nationalite):

    data = (
        {"nom": nom, "nationalite": nationalite},
        )
    cursor.executemany("INSERT INTO nom VALUES(:nom, :nationalite)", data)

def insertPrenom(prenom, genre):

    data = (
        {"prenom": prenom, "genre": genre},
        )
    cursor.executemany("INSERT INTO prenom VALUES(:prenom, :genre)", data)


#Fonction pour retirer une entrée

#Fonction pour voir les données

#Fonction pour exporter les entrées dans un fichier

#Fonction pour fermer la DB
def closedb():
    cursor.close()

if options.num is None:
    print(randomfull())
else:
    i = 0
    while i < options.num:
        print(str(i+1) + " " + randomfull())
        i += 1
