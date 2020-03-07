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
from manager import *
from tkinter import *


### Définition de quelques variables

donnees = {"utilisateurCourant": None,
           "fenetre": Tk()} # Pas d'utilisateur au départ
### Affichage du menu de départ
fenetre = donnees["fenetre"]
menuActuel = start(fenetre, donnees) # On charge le menu principal 
menuActuel.afficher()
fenetre.destroy()
"""
# Tant que l'utilisateur ne souhaite pas quitter l'application, le programme continuer de naviguer de menu en menu
while menuActuelle != None:
    # On affiche le menu suivant selon le choix de l'utilisateur
    menuActuelle = menuActuelle.afficher(donnees)
"""

