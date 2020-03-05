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


### Définition de quelques variables

utilisateurCourant = None # Pas d'utilisateur au départ

### Affichage du menu de départ




### Test de connexion
pseudo = "Bryan"
motDePasse = "abcdef"
typeUtilisateur = "Administrateur"
tentativeConnexion = connexion(pseudo, motDePasse, typeUtilisateur)
if tentativeConnexion != None:
    utilisateurCourant = tentativeConnexion
    print("Bienvenue %s !" % utilisateurCourant.pseudo)


### Test pour creer un compte

"""
utilisateurCourant = listeUtilisateurs[0]
pseudo = "Antoine"
motDePasse = "ghijkl"
typeUtilisateur = "Administrateur"

utilisateurCourant.creerCompte(typeUtilisateur, pseudo, motDePasse)
"""