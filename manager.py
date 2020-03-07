# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 15:26:59 2020

@author: bryan

Ce module sert à charger toutes les pages et tous les menus
"""

from menu import *
from utilisateur import *
from menuConnexion import *
from option import Option



def start(fenetre, donnees):
    """
        Fonction appelée au démarrage de l'application.
        Elle crée le menu principale et le renvoie
        parametres:
            donnees : dict
        sortie:
            menuPrincipal : Menu
    """
    options = [Option("Consultant", pageActions, donnees),
               Option("Professionnel", pageConnexion, donnees),
               Option("Quitter", quitter, donnees)]
    
    menuPrincipal = MenuFenetre(fenetre, options, "Quel est votre statut ?", donnees)
    
    return menuPrincipal
    

def pageActions(donnees):
    """
        Cette fonction commence par stocker une liste d'actions possibles
        qui dépend des droits de l'utilisateur.
        Elle renvoie ensuite un menu contenant toutes ces actions en options.
        parametres:
            donnees : dict
        sortie:
            menuActions : Menu
    """
    fenetre = donnees["fenetre"]
    # Si l'utilisateur ne s'est pas connecté, il est Consultant
    utilisateur = donnees["utilisateurCourant"]
    if utilisateur == None:
        utilisateur = Utilisateur("Consultant")
    # Doit contenir la liste des actions possibles pour cet utilisateur
    listeActions = [] 
    
    if utilisateur.droits[0]:
        listeActions.append(Option("Consulter un pays", pageRecherchePays, donnees))
    if utilisateur.droits[1]:
        listeActions.append(Option("Proposer une correction", pageProposerCorrection, donnees))
    if utilisateur.droits[2]:
        listeActions.append(Option("Voir les corrections proposées", pageVoirCorrections, donnees))
    if utilisateur.droits[3]:
        listeActions.append(Option("Edition de pays", pageEditionPays, donnees))
    if utilisateur.droits[6]:
        listeActions.append(Option("Ajouter un compte", pageCreerCompte, donnees))
        listeActions.append(Option("Supprimer un compte", pageSupprimerCompte, donnees))
    if utilisateur.droits[7]:
        listeActions.append(Option("Résumé d'informations", pageResumeInformations, donnees))
    if utilisateur.droits[5]:
        listeActions.append(Option("Déconnexion", pageDeconnexion, donnees))
    listeActions.append(Option("Quitter", quitter, donnees))
    
    menuActions = MenuFenetre(fenetre, listeActions, "Que souhaitez-vous faire ?", donnees)
    
    return menuActions
        
def pageConnexion(donnees):
    
    menuConnexion = MenuConnexion(donnees)
    
    return menuConnexion
        
        
                    
def quitter(donnees):
    print("A bientôt !")
    donnees["fenetre"].destroy()
    return None

def pageRecherchePays(donnees):
    print("Pas encore")
    return None

def pageProposerCorrection(donnees):
    print("Pas encore")
    return None

def pageVoirCorrections(donnees):
    print("Pas encore")
    return None

def pageEditionPays(donnees):
    print("Pas encore")
    return None

def pageCreerCompte(donnees):
    print("Pas encore")
    return None

def pageSupprimerCompte(donnees):
    print("Pas encore")
    return None

def pageResumeInformations(donnees):
    print("Pas encore")
    return None

def pageDeconnexion(donnees):
    print("Pas encore")
    return None            
            
            
    
    
    
