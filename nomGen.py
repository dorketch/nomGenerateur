#!/usr/bin/env python2
from optparse import OptionParser
from random import randint
#pour avoir des options en ligne de commandes on utilise optparse.
parser = OptionParser()
parser.add_option("-n","--nombre", type="int", dest="num", help="NUM est egal au nombres de nom qu'on veut generer." )# on ajoute notre option, soit -n suivi d'un nombre pour modifier le nombre de sortie. par default il y a un seul nom.
parser.add_option("-d", "--nodblnames", action="store_false", dest="dblname", help="BOOL si on ne veut pas de noms de famille compose on ajoute l'option -d")
                  
(options, args) = parser.parse_args()

class prenomNom:

    def __init__(self):
        """ on a un nom et un prenom. voila """
        self.nom = "nom"
        self.prenom = "prenom"
        
        
    def genPrenom(self):
        """ Cette fonction genere des prenoms en allant chercher une ligne au hazard dans le fichier dictionnaire """
        with open('dictionnaires/prenom.txt') as fichier: #on ouvre le fichier
            lignes = fichier.readlines() #on lit les lignes
            lignes = [line.rstrip('\n') for line in open('dictionnaires/prenom.txt')]#on enleve le charactere de nouvelle ligne
            # determiner le plafond et le plancher pour la selection
            # au hazard
            plafond = len(lignes) #nombre de lignes total du fichier
            plancher = int(plafond) - int(plafond) #le plancher c'est 0
            plafond = plafond - 1 #l'index commence a 0 alors max - 1
            hazard = randint(plancher,plafond)#on trouve un nombre au hazard
            sortie = lignes[hazard]#on va chercher le contenu de la ligne = au hazard
        self.prenom = sortie #on assigne le prenom a la ligne trouve
        return self.prenom #on retourne le resultat

    def genNom(self):
        """ Cette fonction genere des nom de famille en allant chercher une ligne au hazard dans le fichier dictionnaire """
        with open('dictionnaires/nomFamille.txt') as fichier:
            lignes = fichier.readlines()
            lignes = [line.rstrip('\n') for line in open('dictionnaires/nomFamille.txt')]
            # determiner le plafond et le plancher pour la selection
            # au hazard
            plafond = len(lignes) #nombre de lignes total du fichier
            plancher = int(plafond) - int(plafond) #le plancher c'est 0
            plafond = plafond - 1 #l'index commence a 0 alors max - 1
            hazard = randint(plancher,plafond)
            sortie = lignes[hazard]
        self.nom = sortie
        return self.nom

def shownom():
    """ des fois il y a deux noms de familles, alors on fait pile ou face  et ensuite on genere 1 ou 2 nom + resultat selon les besoins"""
    hazard = randint(0,1)
    if hazard == 1:
        a = prenomNom()
        a.nom = str(a.genNom())
        a.prenom = str(a.genPrenom())
        result = a.prenom + " " + a.nom
    else:
        if options.dblname==0:
            a = prenomNom()
            a.nom = str(a.genNom())
            a.prenom = str(a.genPrenom())
            result = a.prenom + " " + a.nom
        else:
            a = prenomNom()
            b = prenomNom()
            a.prenom = str(a.genPrenom())
            a.nom = str(a.genNom())
            b.nom = str(b.genNom())
            result = a.prenom + " " + a.nom + " " + b.nom

    return result


if options.num:
    count = 0
    while (count < options.num):
        a = shownom()
        print(str(a))
        count = count + 1    
    exit(0)

a = shownom()
print(str(a))

