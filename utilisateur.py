# -*- coding: utf-8 -*-
""" *************************************************************************** 
         ________    __  _______________________
        / ____/ /   / / / / ___/_  __/ ____/ __ \
       / /   / /   / / / /\__ \ / / / __/ / /_/ /
      / /___/ /___/ /_/ /___/ // / / /___/ _, _/
      \____/_____/\____//____//_/ /_____/_/ |_|
 
 Created on Thu Mar  5 14:12:51 2020
 
 @author: id1573
 
*************************************************************************** """
import json

class Utilisateur():
    
    def __init__(self, typeUtilisateur, pseudo = None, motDePasse = None):
        """
            Cette classe représente les utilisateurs.
            typeUtilisateur : str (Consultant, Geographe, DataScientist ou Administrateur) / Définit les droits de l'utilisateur
            pseudo : str / utile à la connexion, pas utile pour les consultants
            motDePasse : str / utile à la connexion, pas utile pour les consultants
        """
        self.typeUtilisateur = typeUtilisateur
        # On attribue des droits à l'utilisateur en fonction de son type.
        if self.typeUtilisateur == "Consultant":
            self.droits  = [True, True] + [False] * 8
        elif self.typeUtilisateur == "Geographe":
            self.droits = [True, False, True, True, False, True, False, False, False, False]
        elif self.typeUtilisateur == "DataScientist":
            self.droits  = [True, True, False, False, False, True, False, True, True, True]
        elif self.typeUtilisateur == "Administrateur":
            self.droits = [True, False] + [True] * 8
        else:
            self.droits = [False] * 10
        self.pseudo = str(pseudo)
        self.motDePasse = str(motDePasse)
        
    def afficherPays(self):
        print("J'affiche un pays")
    
    def toDict(self):
        """
            Crée un dictionnaire contenant les informations de l'utilisateur afin de pouvoir les stocker au format json.
        """
        user_dict = {
                     'motDePasse': self.motDePasse,
                     'typeUtilisateur': self.typeUtilisateur
                     }
                     
        return user_dict
    
    def __str__(self):
        return "Status: {}, Pseudo: {}".format(self.typeUtilisateur, self.pseudo)
    
def get_listeUtilisateurs():
    """
        Fonction qui retourne un dictionnaire contenant tous les utilisateurs enregistrés.
        Chaque clé est le pseudo de l'utilisateur
    """
    # Récupération de la liste des utilisateurs dans le fichier json sous la forme d'un dictionnaire
    with open("donnees/utilisateurs.json") as json_file: 
        listeUtilisateurs = json.load(json_file)
    
        for cle in listeUtilisateurs:
            infos = listeUtilisateurs[cle]
            listeUtilisateurs[cle] = Utilisateur(infos["typeUtilisateur"], cle, infos["motDePasse"])
    return listeUtilisateurs

def get_dictUtilisateurs():
    """
        Fonction qui retourne un dictionnaire contenant tous les utilisateurs enregistrés.
        Chaque clé est le pseudo de l'utilisateur
    """
    # Récupération de la liste des utilisateurs dans le fichier json sous la forme d'un dictionnaire
    with open("donnees/utilisateurs.json") as json_file: 
        dictUtilisateurs = json.load(json_file)
    
        return dictUtilisateurs
        