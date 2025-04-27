#!/usr/bin/env python3
from optparse import OptionParser #pour les options en ligne de commandes
from random import randint #pour avoir du random
import sqlite3


# #pour avoir des options en ligne de commandes on utilise optparse.
# parser = OptionParser()
# # on ajoute notre option, soit -n suivi d'un nombre pour modifier le nombre de sortie. par default il y a un seul nom.
# parser.add_option("-n","--nombre", type="int", dest="num", help="NUM est egal au nombres de nom qu'on veut generer." )
# # l'option -d pour ne pas avoir de double nom de famille (ou noms de famille compose)
# parser.add_option("-d", "--nodblnames", action="store_false", dest="dblname", help="BOOL si on ne veut pas de noms de famille compose on ajoute l'option -d")
# (options, args) = parser.parse_args()
# dblnamevar = options.dblname 

#definition de variable

# dicnom = 'dictionnaires/nomFamille.txt'
# dicprenom = 'dictionnaires/prenom.txt'

basededonnee = "nom.db" #nom du fichier de base de donnée pour SQLITE3

#Fonction pour crée la base de données
def createInitialTable():
    cursor.execute("CREATE TABLE prenom(prenom, genre, nationalite)") #Table pour les prénoms
    cursor.execute("CREATE TABLE nom(nom, genre, nationalite)")       #Table pour les noms



#Fonction pour connecter a la DB
connection = sqlite3.connect(basededonnee) 
cursor = connection.cursor()

#Fonction pour fermer la DB

#Fonction pour ajouter une entrée
def insert(nom, entre, genre, nationalite):
    requete = "INSERT INTO" + nom + "VALUES ('" + entre + ", " + genre + ", " + nationalite + ")"
    res = cursor.execute(requete)

#Fonction pour retirer une entrée

#Fonction pour voir les données
def shownom():
    requete = "SELECT * FROM nom"
    res = cursor.execute(requete).fetchall()
    print(res)
def showprenom():
    requete = "SELECT * FROM prenom"
    res = cursor.execute(requete).fetchall()
    print(res)
#Fonction pour exporter les entrées dans un fichier

#Fonction pour obtenir un nom au hazard
def randomnom(nbnom=1):
    requete = "SELECT nom FROM nom ORDER BY random() LIMIT " + str(nbnom) + ""
    res = cursor.execute(requete).fetchone()
    result = ' '.join(res)
    return(result)

def randomprenom(nbprenom=1):
    requete = "SELECT prenom FROM prenom ORDER BY random() LIMIT " + str(nbprenom) + ""
    res = cursor.execute(requete).fetchone()
    result = ' '.join(res) 
    return(result)
#Fonction pour obtenir un prénom et nom de famille

print(randomprenom() + " " + randomnom())







# #Ancien code
# def readdic(dic):
#     "ceci ouvre le fichier dictionnaire si il est dans le bon sous-repertoire"
#     with open(dic) as fichier:
#         lignes = fichier.readlines()
#         lignes = [line.rstrip('\n') for line in open(dic)]
#         # determiner le plafond et le plancher pour la selection
#         # au hazard
#         plafond = len(lignes) #nombre de lignes total du fichier
#         plancher = int(plafond) - int(plafond) #le plancher c'est 0
#         plafond = plafond - 1 #l'index commence a 0 alors max - 1
#         hazard = randint(plancher,plafond)
#         sortie = lignes[hazard]
#     return sortie


# class prenomNom:

#     def __init__(self):
#         """ Assigne un prenom, un nom et un deuxieme nom. On tire a pile ou face et on decide celui quon montre"""
#         self.nom = self.genNom()
#         self.dblnom = self.genDblNom()
#         self.prenom = self.genPrenom()
#         self.dbl = self.prenom + " " + self.nom + " " + self.dblnom
#         self.single = self.prenom + " " + self.nom
#         hazard = randint(0,1)
#         if hazard == 1:
#             self.result = self.single
#         else:
#             if dblnamevar==0:
#                 self.result = self.single
#             else:
#                 self.result = self.dbl

#     def genPrenom(self):
#         """ Cette fonction genere des prenoms en allant chercher une ligne au hazard dans le fichier dictionnaire """
#         self.prenom = str(readdic(dicprenom))
#         return self.prenom #on retourne le resultat

#     def genNom(self):
#         """ Cette fonction genere des nom de famille en allant chercher une ligne au hazard dans le fichier dictionnaire """
#         self.nom = str(readdic(dicnom))
#         return self.nom
#     def genDblNom(self):
#         """ Cette fonction genere des nom de famille en allant chercher une ligne au hazard dans le fichier dictionnaire """
#         self.dblnom = str(readdic(dicnom))
#         return self.dblnom


# # def multipletime(nbtime):
# #     count = 0
# #     while (count < options.num):
# #         leNom = prenomNom()
# #         print(str(leNom.result))
# #         count = count + 1    
# #     return

    
# if options.num:
#     count = 0
#     while (count < options.num):
#         leNom = prenomNom()
#         print(str(leNom.result))
#         count = count + 1    
#     exit(0)


# leNom = prenomNom()
# print(str(leNom.result))


