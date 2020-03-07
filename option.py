# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 15:22:28 2020

@author: bryan
"""

from actions import *

class Option():
    
    def __init__(self, libelle, action, donnees):
        self.libelle = libelle
        self.action = action
        self.donnees = donnees
    
    def choix(self):
        return self.action(self.donnees)