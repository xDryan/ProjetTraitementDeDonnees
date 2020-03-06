# -*- coding: utf-8 -*-
""" *************************************************************************** 
         ________    __  _______________________
        / ____/ /   / / / / ___/_  __/ ____/ __ \
       / /   / /   / / / /\__ \ / / / __/ / /_/ /
      / /___/ /___/ /_/ /___/ // / / /___/ _, _/
      \____/_____/\____//____//_/ /_____/_/ |_|
 
 Created on Thu Mar  5 14:32:55 2020
 
 @author: id1573
 
*************************************************************************** """


### Imports
from utilisateur import Utilisateur
from actions import *
from manager import *


### Définition de quelques variables

donnees = {"utilisateurCourant": None} # Pas d'utilisateur au départ
### Affichage du menu de départ

menuActuelle = start(donnees) # On charge le menu principal 
# Tant que l'utilisateur ne souhaite pas quitter l'application, le programme continuer de naviguer de menu en menu
while menuActuelle != None:
    # On affiche le menu suivant selon le choix de l'utilisateur
    menuActuelle = menuActuelle.afficher(donnees)



### Test pour creer un compte

"""
utilisateurCourant = listeUtilisateurs[0]
pseudo = "Antoine"
motDePasse = "ghijkl"
typeUtilisateur = "Administrateur"

utilisateurCourant.creerCompte(typeUtilisateur, pseudo, motDePasse)
"""