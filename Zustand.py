#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint

class Zustand:
    "Repräsentiert den Zustand des Programms"
    folge = ""  # Bisherige Eingaben
    statistik = {}  # Dictionary mit bisheriger Statistik.  Das
                    # Dictionary merkt sich zu jeder Kombination von
                    # 'tiefe' vielen Bits, wie oft diese Kombination
                    # in der gespeicherten Folge vorkam.
    treffer = 0 # Anzahl richtige Tipps
    tiefe = 3 # Suchtiefe für die Statistik, Default = 3
    
    def __init__ (self, suchtiefe):
        # Initialisiert das Programm mit 
        self.folge = "" # ... der leeren Folge
        self.tiefe = suchtiefe # ... der gegebenen Tiefe der Statistik
        self.treffer=0 # ... keinen bisherigen Treffern

        # Initialisiere das dictionary mit Nullen
        for i in range (2**suchtiefe):
            # Wandle die Ganzzahl in einen Bitstring...
            b = bin(i)[2:]
            # ... und fülle vorne Mit Nullen auf.
            b = "".join([str(0) for i in range(self.tiefe-len(b))]) + b
            # Setze den Wert zu dieser Bitfolge:
            self.statistik[ b ] = 0;

    def rate (self, still=False):
        # Diese Funktion rät die nächste Eingabe und hat natürlich
        # keine Argumente außer dem internen Zustand zur Verfügung.
        # Die Option "still" steuert ob informative Ausgaben erfolgen
        # sollen (Standard=nein).
        
        # Falls nicht genug Daten vorliegen da Folge zu kurz: Würfeln
        if len(self.folge) < self.tiefe:
            tipp = randint(0,1)
            if not still: print ("Tipp: " + str(tipp))
            return tipp

        # Falls die Folge lang genug ist, betrachte letzte tiefe-1
        # bits und vergleiche welches bit darauf häufiger folgte:
        lastbits = self.folge[ -(self.tiefe-1): ]
        if self.statistik[ lastbits + str(0) ] == self.statistik [ lastbits + str(1) ]:
            # Bei Gleichstand: Zufall
            tipp = randint(0,1)
            if not still: print ("Tipp: " + str(tipp))
            return tipp
        # Ansonsten: Wähle das häufigere nächste bit
        elif self.statistik[ lastbits + str(0) ] > self.statistik [ lastbits + str(1) ]:
            if not still: print "Tipp: 0"
            return 0
        else:
            if not still: print "Tipp: 1"
            return 1
    
    def eingabe (self, bit, still=False):
        # Diese Funktion verarbeitet eine Eingabe

        # Bestimme zunächst den Tipp
        tipp = self.rate(still);

        # Werte Tipp aus:
        if tipp == int(bit):
            self.treffer += 1;

        # Speichere neue Eingabe in der Folge
        self.folge += str(bit)
        # Und aktualisiere Statistik:
        if len(self.folge) >= self.tiefe:
            self.statistik [ self.folge[-self.tiefe:] ] += 1;

    def quote(self):
        # Diese Funktion gibt die aktuelle Quote aus
        print " ".join(["Aktuelle Quote:", str(self.treffer), "Treffer aus",
                        str(len(self.folge)), "Versuchen:", str(int(100*self.treffer / len(self.folge))),"%"])
        
