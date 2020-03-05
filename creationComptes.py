# -*- coding: utf-8 -*-
""" *************************************************************************** 
         ________    __  _______________________
        / ____/ /   / / / / ___/_  __/ ____/ __ \
       / /   / /   / / / /\__ \ / / / __/ / /_/ /
      / /___/ /___/ /_/ /___/ // / / /___/ _, _/
      \____/_____/\____//____//_/ /_____/_/ |_|
 
 Created on Thu Mar  5 14:33:32 2020
 
 @author: id1573
 
*************************************************************************** """
### Imports
from utilisateur import Utilisateur
import json


### Création de quelques utilisateurs
user1 = Utilisateur("Administrateur", "Bryan", "abcdef")
user1_dict = user1.enregistrer()
# On les stocke dans un dictionnaire pour pouvoir les enregistrer au format json
users_dict = {
              user1.pseudo: user1_dict     
              }
# Enregistrement des utilisateurs au format json        
with open('donnees/utilisateurs.json', 'w') as json_file:
    json.dump(users_dict, json_file)