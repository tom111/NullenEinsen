#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Zustand import Zustand

Z = Zustand(3)
while (1):
    folge = raw_input ("Bitte eine zufällige Null-Eins Folge eingeben: ")
    for zeichen in folge:
        if zeichen == '0' : Z.eingabe(0) # Zeichen is an int
        if zeichen == '1' : Z.eingabe(1)



