#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Zustand:
    "Repräsentiert den Zustand des Programms"
    folge = []  # Bisherige Eingaben
    statistik = {}  # Hash mit bisheriger Statistik
    tiefe = 3 # Suchtiefe für die Statistik
    
    def __init__ (self, suchtiefe):
        folge = []
        tiefe = suchtiefe;

        # Generate all strings of length tiefe
        for i in range (2**suchtiefe):
            b = bin(i)[2:]
            statistik[ b ] = 0;
        
    
    def rate (self, eingabe):
        "Rate die nächste Eingabe"
        tipp = 
        folge += [eingabe]
        if len(folge) >= self.tiefe: 
            statistik [ folge[-self.tiefe] ] += 1;
        
        return 0;
    
