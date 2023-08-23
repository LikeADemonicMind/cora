# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 11:32:17 2023

@author: Utilisateur
"""

import pyttsx3 # library to say the number

def tts(chiffre) : 
    engine = pyttsx3.init()
    engine.say(chiffre)
    engine.runAndWait()
    