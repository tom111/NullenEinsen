#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import randint
from Zustand import Zustand

Z = Zustand(3)

anleitung = """
\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
Anleitung:

Bitte geben sie eine zufällige Folge aus Nullen und Einsen ein.  Nach
jeder Stelle wird der Computer versuchen ihre nächste Eingabe (ohne
Schummeln) vorherzusagen.  Sie können einzelne oder mehrere Bits
eingeben.

(n) Neustart
(z) Erzeuge 100 zufällige Bits als Eingabe.
(f) Zeige bisherige Folge an.
"""

print anleitung
while True:
    # Die folgende Logik verarbeitet die Eingabe von entweder Ziffern
    # oder den Steuerzeichen.  Jede nicht passende Eingabe wird
    # einfach ignoriert.
    try:
        folge = raw_input ("Bitte eine zufällige Null-Eins Folge eingeben: ")
    except (EOFError, KeyboardInterrupt):
        print "\n\n\nAuf Wiedersehen."
        exit (0);
    for zeichen in folge:
        if zeichen == '0' :
            # Eingabe Null weitergeben an die Logik
            Z.eingabe(0)
            print "Eingabe: 0"
            Z.quote()
        elif zeichen == '1':
            # Eingabe Eins weitergeben an die Logik
            Z.eingabe(1)
            print "Eingabe 1"
            Z.quote()
        elif zeichen == 'n':
            # Eingabe n -> Neustart
            print anleitung
            Z = Zustand(3)
        elif zeichen == 'z':
            # Eingabe z -> 100 Zufallszahlen an die Logik weitergeben
            for i in range (100):
                Z.eingabe (randint (0,1), still=True)
            Z.quote()
        elif zeichen == 'f':
            # Eingabe f -> Ausgabe der bisherigen Folge
            print Z.folge
