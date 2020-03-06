# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 15:22:28 2020

@author: bryan
"""

from actions import *

class Option():
    
    def __init__(self, libelle, action):
        self.libelle = libelle
        self.action = action
    
    def choix(self, donnees):
        return self.action(donnees)