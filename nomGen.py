#!/usr/bin/env python
from optparse import OptionParser
from random import randint

#pour avoir des options en ligne de commandes on utilise optparse.
parser = OptionParser()
parser.add_option("-n","--nombre", type="int", dest="num", help="NUM est egal au nombres de nom qu'on veut generer." )# on ajoute notre option, soit -n suivi d'un nombre pour modifier le nombre de sortie. par default il y a un seul nom.
parser.add_option("-d", "--nodblnames", action="store_false", dest="dblname", help="BOOL si on ne veut pas de noms de famille compose on ajoute l'option -d")
                  
(options, args) = parser.parse_args()
dblnamevar = options.dblname 

class prenomNom:

    def __init__(self):
        """ Assigne un prenom, un nom et un deuxieme nom. On tire a pile ou face et on decide celui quon montre"""
        self.nom = self.genNom()
        self.dblnom = self.genDblNom()
        self.prenom = self.genPrenom()
        self.dbl = self.prenom + " " + self.nom + " " + self.dblnom
        self.single = self.prenom + " " + self.nom
        hazard = randint(0,1)
        if hazard == 1:
            self.result = self.single
        else:
            if dblnamevar==0:
                self.result = self.single
            else:
                self.result = self.dbl

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
    def genDblNom(self):
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
        self.dblnom = sortie
        return self.dblnom
        
if options.num:
    count = 0
    while (count < options.num):
        leNom = prenomNom()
        print(str(leNom.result))
        count = count + 1    
    exit(0)


leNom = prenomNom()
print(str(leNom.result))


