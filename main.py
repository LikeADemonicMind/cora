# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 09:41:25 2023

@author: Utilisateur
"""

#Functions
from capture import capture
from preprocessing import preprocess
from ai import ai
from tts import tts

def main():
    # Step 1 : image capture
    capture()
    # Step 2 : preprocessing
    img = preprocess()
    print(img)
    # Step 3 : AI 
    chiffre = ai(img)
    # Step 4 : text-to-speech
    tts(chiffre)
    
if __name__ == "__main__":
    main()
    