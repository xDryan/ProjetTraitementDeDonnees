# -*- coding: utf-8 -*-
"""
Created on Sat March  7 10:07:15 2020

@author: antoine
"""

from tkinter import *
from utilisateur import *
from actions import *
from actionsGUI import *

class FenetreConnexion(Frame):
    """
        Classe qui définie la fenetre de connexion et qui permet la connexion en tant que simple consultant
        ou en tant qu'utilisateur ayant un compte
    """

    def __init__(self, fenetre, donnees, **kwargs):
        Frame.__init__(self, fenetre, width=500, height=500, **kwargs)
        self.pack()
        self.donnees = donnees

        widgets = []

        self.titreFrame = LabelFrame(self, text="Fenetre de connexion")
        widgets.append(self.titreFrame)

        # widgets relatifs à la connexion
        self.labelPseudo = Label(self, text="Pseudo\n")
        widgets.append(self.labelPseudo)
        Identifiant = StringVar()
        self.champId = Entry(self, textvariable=Identifiant)
        widgets.append(self.champId)

        self.labelMdp = Label(self, text="Mot de passe\n")
        widgets.append(self.labelMdp)
        motDePasse = StringVar()
        self.champMdp = Entry(self, textvariable=motDePasse)
        widgets.append(self.champMdp)

        self.boutonValiderLog = Button(self, text="Valider", command=self.valider_log)
        widgets.append(self.boutonValiderLog)

        # widgets relatifs à la connexion d'un consultant
        self.labelConsultant = Label(self, text="Se connecter en tant que consultant")
        widgets.append(self.labelConsultant)
        self.boutonConsultant = Button(self, text="Entrer", command=self.afficher_fenetre_menu)
        widgets.append(self.boutonConsultant)

        for wid in widgets:
            wid.pack()

    def valider_log(self):
        """
            verifie les informations de connexion
        :return:si les informations sont correctes, affiche la fenetre de menu principal
                sinon renvoie une erreur
        """
        idEntre = self.champId.get()
        mdpEntre = self.champMdp.get()
        if isinstance(connexion(idEntre, mdpEntre)):
            return afficher_fenetre_menu()
        else:
            fenetreErreur = Tk()
            Label(fenetreErreur, text="Identifiant ou mot de passe invalide").pack()

    def afficher_fenetre_menu(self):
        """
            affiche le menu principal
        :return: fenetre de menu principal
        """
        return MenuPrincipal(self, self.donnees, self.champId, self.champMdp)



class MenuPrincipal(Toplevel):
    """
        Classe qui definie la fenetre de menu principal avec les options possibles pour les differents utilisateurs
   """

    def __init__(self, fenetre, donnees, champId, champMdp, **kwargs):
        Toplevel.__init__(self, fenetre, width=1500, height=500, **kwargs)
        self.fenetre = fenetre
        self.donnees= donnees
        self.champId = champId
        self.champMdp = champMdp

        self.titreFrame = LabelFrame(self, text="Menu Principal")
        self.titreFrame.pack()

        # widgets relatifs aux options selon les types d'utilisateurs
        if connexion(self.champId.get(), self.champMdp.get()) == None:
            self.boutonAfficherPays = Button(self, text="Afficher pays", command=self.afficher_pays)
            self.boutonAfficherPays.pack()
            self.boutonPropositionCorrection = Button(self, text="Proposer une correction",
                                                      command=self.proposer_correction)
            self.boutonPropositionCorrection.pack()
            self.boutonQuitter = Button(self, text="Quitter", command=self.quit)
            self.boutonQuitter.pack()

        elif connexion(self.champId.get(), self.champMdp.get()).typeUtilisateur == "Administrateur":
            # bouton des options
            self.boutonAfficherPays = Button(self, text="Afficher pays", command=self.afficher_pays)
            self.boutonAfficherPays.pack()
            self.boutonPropositionCorrection = Button(self, text="Proposer une correction", command=self.proposer_correction,
                                                      state=DISABLED)
            self.boutonPropositionCorrection.pack()
            self.boutonCorrectionInfo = Button(self, text="Corriger une information", command=self.corriger_information)
            self.boutonCorrectionInfo.pack()
            self.boutonAjouterPays = Button(self, text="Ajouter un pays", command=self.ajouter_pays)
            self.boutonAjouterPays.pack()
            self.boutonSupprimerPays = Button(self, text="Supprimer un pays", command=self.supprimer_pays)
            self.boutonSupprimerPays.pack()
            self.boutonModifierPays = Button(self, text="Modifier un pays", command=self.modifier_pays)
            self.boutonModifierPays.pack()
            self.boutonResumeInfo = Button(self, text="Resumer d'information", command=self.resumer_infos)
            self.boutonResumeInfo.pack()
            self.boutonGraphique = Button(self, text="Graphiques", command=self.graphique)
            self.boutonGraphique.pack()
            self.boutonGestionCompteEmployeur = Button(self, text="Gérer les comptes employeur", command=self.gestion_compte_emp)
            self.boutonGestionCompteEmployeur.pack()
            self.boutonDeconnexion = Button(self, text="Deconnexion", command=self.deconnexion)
            self.boutonDeconnexion.pack()

        elif connexion(self.champId.get(), self.champMdp.get()).typeUtilisateur == "DataScientist":
            self.boutonAfficherPays = Button(self, text="Afficher pays", command=self.afficher_pays)
            self.boutonAfficherPays.pack()
            self.boutonPropositionCorrection = Button(self, text="Proposer une correction", command=self.proposer_correction)
            self.boutonPropositionCorrection.pack()
            self.boutonCorrectionInfo = Button(self, text="Corriger une information", command=self.corriger_information,
                                               state=DISABLED)
            self.boutonCorrectionInfo.pack()
            self.boutonAjouterPays = Button(self, text="Ajouter un pays", command=self.ajouter_pays, state=DISABLED)
            self.boutonAjouterPays.pack()
            self.boutonSupprimerPays = Button(self, text="Supprimer un pays", command=self.supprimer_pays, state=DISABLED)
            self.boutonSupprimerPays.pack()
            self.boutonModifierPays = Button(self, text="Modifier un pays", command=self.modifier_pays, state=DISABLED)
            self.boutonModifierPays.pack()
            self.boutonResumeInfo = Button(self, text="Resumer d'information", command=self.resumer_infos)
            self.boutonResumeInfo.pack()
            self.boutonGraphique = Button(self, text="Graphiques", command=self.graphique)
            self.boutonGraphique.pack()
            self.boutonGestionCompteEmployeur = Button(self, text="Gérer les comptes employeur", command=self.gestion_compte_emp,
                                                       sate=DISABLED)
            self.boutonGestionCompteEmployeur.pack()
            self.boutonDeconnexion = Button(self, text="Deconnexion", command=self.deconnexion)
            self.boutonDeconnexion.pack()

        elif connexion(self.champId.get(), self.champMdp.get()).typeUtilisateur == "Geographe":
            self.boutonAfficherPays = Button(self, text="Afficher pays", command=self.afficher_pays)
            self.boutonAfficherPays.pack()
            self.boutonPropositionCorrection = Button(self, text="Proposer une correction", command=self.proposer_correction,
                                                      state=DISABLED)
            self.boutonPropositionCorrection.pack()
            self.boutonCorrectionInfo = Button(self, text="Corriger une information", command=self.corriger_information)
            self.boutonCorrectionInfo.pack()
            self.boutonAjouterPays = Button(self, text="Ajouter un pays", command=self.ajouter_pays)
            self.boutonAjouterPays.pack()
            self.boutonSupprimerPays = Button(self, text="Supprimer un pays", command=self.supprimer_pays, state=DISABLED)
            self.boutonSupprimerPays.pack()
            self.boutonModifierPays = Button(self, text="Modifier un pays", command=self.modifier_pays)
            self.boutonModifierPays.pack()
            self.boutonResumeInfo = Button(self, text="Resumer d'information", command=self.resumer_infos, state=DISABLED)
            self.boutonResumeInfo.pack()
            self.boutonGraphique = Button(self, text="Graphiques", command=self.graphique, state=DISABLED)
            self.boutonGraphique.pack()
            self.boutonGestionCompteEmployeur = Button(self, text="Gérer les comptes employeur",
                                                       command=self.gestion_compte_emp, state=DISABLED)
            self.boutonGestionCompteEmployeur.pack()
            self.boutonDeconnexion = Button(self, text="Deconnexion", command=self.deconnexion)
            self.boutonDeconnexion.pack()



    def afficher_pays(self):
        return afficherPays(self.donnees)

    def proposer_correction(self):
        return propositionCorrection(self.donnees)

    def corriger_information(self):
        return correctionInfos(self.donnees)

    def ajouter_pays(self):
        return ajouterPays(self.donnees)

    def supprimer_pays(self):
        return supprimerPays(self.donnees)

    def modifier_pays(self):
        return modifierPays(self.donnees)

    def resumer_infos(self):
        return resumerInformations(self.donnees)

    def graphique(self):
        return graphiqueGUI(self.donnees)

    def gestion_compte_emp(self):
        return gestionCompteEmp(self.donnees)

    def deconnexion(self):
        return deconnexionGUI(self.fenetre)





if __name__ == "__main__":
    donnees = get_listeUtilisateurs()
    fenetreConnexion = FenetreConnexion(Tk(), donnees)
    fenetreConnexion.mainloop()



