#!/usr/bin/env python
# coding: utf-8


#début définition
class Personne:
""" Classe Personne """
    #constructeur
    def __init__(self):
        #lister les champs
        self.nom = ""
        self.age = 0
        self.salaire = 0.0
    #fin constructeur

    #saisie des infos
    def saisie(self):
        self.nom = input("Nom : ")
        self.age = int(input("Age : "))
        self.salaire = float(input("Salaire : "))
    #fin saisie
    
    #affichage des infos
    def affichage(self):
        print("Son nom est ", self.nom)
        print("Son âge : ", self.age)
        print("Son salaire : ", self.salaire)
    #fin affichage
    
    #reste avant retraite
    def retraite(self, limite):
        reste = limite - self.age
        if (reste < 0):
            print("Vous êtes à la retraite")
        else:
            print("Il vous reste %s années" % (reste))
    #fin retraite

#fin définition

