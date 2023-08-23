# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 09:41:25 2023

@author: Utilisateur
"""

# Librairies 
import matplotlib.pyplot as plt
import pyttsx3
import joblib

#Functions
from preprocessing.py import preprocessing

# AI
knn = joblib.load('knn_digits')

def main():
    # Step 1 : image capture
    
    # Step 2 : preprocessing
    img = preprocessing()
    print(img)
    # Step 3 : AI 
    
    # Step 4 : text-to-speech
  
    
if __name__ == "__main__":
    main()
    