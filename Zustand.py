#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint

class Zustand:
    "Repräsentiert den Zustand des Programms"
    folge = ""  # Bisherige Eingaben
    statistik = {}  # Hash mit bisheriger Statistik
    treffer = 0 # Anzahl richtige Tipps
    tiefe = 3 # Suchtiefe für die Statistik
    
    def __init__ (self, suchtiefe):
        self.folge = ""
        self.tiefe = suchtiefe
        self.treffer=0

        # Initialisiere dictionary mit Nullen
        for i in range (2**suchtiefe):
            # Ganzzahl in Bitstring:
            b = bin(i)[2:]
            # vorne Mit Nullen auffüllen
            b = "".join([str(0) for i in range(self.tiefe-len(b))]) + b
            self.statistik[ b ] = 0;

    def rate (self, still=False):
        "Diese Funktion rät die nächste Eingabe und hat natürlich keine Argumente außer dem internen Zustand zur Verfügung."
        # Falls nicht genug Daten: Zufall
        if len(self.folge) < self.tiefe:
            tipp = randint(0,1)
            if not still: print ("Tipp: " + str(tipp))
            return tipp
        lastbits = self.folge[ -(self.tiefe-1): ]
        # print "lastbits:"
        # print lastbits
        # Wähle das häufigere nächste bit
        if self.statistik[ lastbits + str(0) ] > self.statistik [ lastbits + str(1) ]:
            if not still: print "Tipp: 0"
            return 0
        else:
            if not still: print "Tipp: 1"
            return 1
    
    def eingabe (self, bit, still=False):
        "Rate die nächste Eingabe"
        tipp = self.rate(still);
        if tipp == int(bit):
            self.treffer += 1;
        self.folge += str(bit)
        if len(self.folge) >= self.tiefe:
            self.statistik [ self.folge[-self.tiefe:] ] += 1;

        # print "Folge:"
        # print self.folge
        # print "Statistik:"
        # print self.statistik

    def quote(self):
        print " ".join(["Aktuelle Quote:", str(self.treffer), "Treffer aus",
                        str(len(self.folge)), "Versuchen:", str(int(100*self.treffer / len(self.folge))),"%"])
