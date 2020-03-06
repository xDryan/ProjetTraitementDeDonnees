# -*- coding: utf-8 -*-
""" *************************************************************************** 
         ________    __  _______________________
        / ____/ /   / / / / ___/_  __/ ____/ __ \
       / /   / /   / / / /\__ \ / / / __/ / /_/ /
      / /___/ /___/ /_/ /___/ // / / /___/ _, _/
      \____/_____/\____//____//_/ /_____/_/ |_|
 
 Created on Thu Mar  5 16:18:28 2020
 
 @author: id1573
 
*************************************************************************** """
from utilisateur import Utilisateur
from utilisateur import get_listeUtilisateurs
from utilisateur import get_dictUtilisateurs
import json


def creerCompte(utilisateurCourant, typeUtilisateur, pseudo, motDePasse):
    """
        Uniquement disponible pour les administrateurs.
        Crée et enregistre un nouvel utilisateur à l'aide des informations données.
    """
    if utilisateurCourant.droits[6]: # On vérifie que c'est un utilisateur qui en a le droit qui crée un compte
        dictUtilisateurs = get_dictUtilisateurs()
        utilisateur = Utilisateur(typeUtilisateur, pseudo, motDePasse) # Création d'un nouvel utilisateur
        dictUtilisateurs[pseudo] = utilisateur.toDict() # Enregistrement du nouvel utilisateur
        with open('donnees/utilisateurs.json', 'w') as json_file:
            json.dump(dictUtilisateurs, json_file)          
    else:
        print("Vous n'avez pas les droits pour faire cette action.")
            
def connexion(pseudo, motDePasse):
    """
        Tentative de connexion.
        Renvoie un objet de type utilisateur si les identifiants sont corrects, None sinon.
    """
    listeUtilisateurs = get_listeUtilisateurs()
    try:  
        utilisateur = listeUtilisateurs[pseudo]
        if utilisateur.motDePasse == motDePasse:
            print("Connexion réussie !")
            return utilisateur
    except:
        print("Aucun utilisateur ne possède ces identifiants.")
    return None

def supprimerCompte(utilisateurCourant, pseudo):
    """
        Supprime le compte d'un utilisateur
    """
    listeUtilisateurs = get_dictUtilisateurs()
    del listeUtilisateurs[pseudo]
    with open('donnees/utilisateurs.json') as json_file:
        json.dump(listeUtilisateurs, json_file)
      

def verifierAction(utilisateurCourant):
    """
        Demande le mdp d'un utilisateur pour vérifier son identité
        avant de faire une action importante
    """
    print("Entrer votre mot de passe:\n")
    mdp = str(input())
    if mdp == utilisateurCourant.motDePasse:
        return True
    return False
    
    
    
    
    
    