# -*- coding: utf-8 -*-
"""
Created on Sat March  7 12:50 2020

@author: antoine
"""

"""
    Gere le lancement des fenetres
"""

from menuGUI import *

def startGUI(donnees):
    """
        Fonction appelée au démarrage de l'application.
        Elle crée le menu principale et le renvoie
        parametres:
            donnees : dict
        sortie:
            fenetreDeConnexion : FennetreConnexion
    """

    fenetreDeConnexion = FenetreConnexion(donnees)

    return fenetreDeConnexion

