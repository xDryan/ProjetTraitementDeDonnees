# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 15:26:59 2020

@author: bryan

Ce module sert à charger toutes les pages et tous les menus
"""



from menu import Menu
from option import Option
from actions import *
from utilisateur import Utilisateur


def start(donnees):
    """
        Fonction appelée au démarrage de l'application.
        Elle crée le menu principale et le renvoie
        parametres:
            donnees : dict
        sortie:
            menuPrincipal : Menu
    """
    options = [Option("Consultant", pageActions),
               Option("Professionnel", pageConnexion),
               Option("Quitter", quitter)]
    
    menuPrincipal = Menu(options, "Quel est votre statut ?", donnees)
    
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
    # Si l'utilisateur ne s'est pas connecté, il est Consultant
    utilisateur = donnees["utilisateurCourant"]
    if utilisateur == None:
        utilisateur = Utilisateur("Consultant")
    # Doit contenir la liste des actions possibles pour cet utilisateur
    listeActions = [] 
    
    if utilisateur.droits[0]:
        listeActions.append(Option("Consulter un pays", pageRecherchePays))
    if utilisateur.droits[1]:
        listeActions.append(Option("Proposer une correction", pageProposerCorrection))
    if utilisateur.droits[2]:
        listeActions.append(Option("Voir les corrections proposées", pageVoirCorrections))
    if utilisateur.droits[3]:
        listeActions.append(Option("Edition de pays", pageEditionPays))
    if utilisateur.droits[6]:
        listeActions.append(Option("Ajouter un compte", pageCreerCompte))
        listeActions.append(Option("Supprimer un compte", pageSupprimerCompte))
    if utilisateur.droits[7]:
        listeActions.append(Option("Résumé d'informations", pageResumeInformations))
    if utilisateur.droits[5]:
        listeActions.append(Option("Déconnexion", pageDeconnexion))
    listeActions.append(Option("Quitter", quitter))
    
    menuActions = Menu(listeActions, "Que souhaitez-vous faire ?", donnees)
    
    return menuActions
    
        
    
    
def pageConnexion(donnees):
    """
        Cette fonction sert de page de connexion à l'utilisateur.
        Elle vérifie que ses identifiants sont corrects et le laisse
        accéder au menu d'actions si c'est le cas.
        parametres:
            donnees : dict
        sortie:
            menuActions : Menu
            ou
            menuPrincipal : Menu
    """
    termine = False
    while not termine:
    
        print("Veuillez entrer votre pseudo : \n")
        pseudo = input(">")
        
        print("Veuillez entrer votre mot de passe : \n")
        motDePasse = input(">")
        
        utilisateur = connexion(pseudo, motDePasse)
        if utilisateur != None:
            donnees["utilisateurCourant"] = utilisateur
            menuActions = pageActions(donnees)
            return menuActions
        else:
            reponseCorrecte = False
            while not reponseCorrecte:
                reponseCorrecte = True
                print("Voulez-vous réessayer ? (O/N)")
                reponse = input(">")
                
                if reponse != "O" and reponse != "N":
                    print("Vous devez répondre O pour Oui ou N pour Non")
                    reponseCorrecte = False
                elif reponse == "N":
                    termine = True
    menuPrincipal = start(donnees)
    return menuPrincipal
                    
def quitter(donnees):
    print("A bientôt !")
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
            
            
    
    
    
