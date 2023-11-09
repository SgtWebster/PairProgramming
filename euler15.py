# Project Euler 15 - https://projecteuler.net/problem=15 - Lösung 
#Lattice Paths
#Starting in the top left corner of a 2x2 grid, and only being able to move to the (!)right and down(!), there are exactly  6 routes to the bottom right corner.
#how many such routes are there trough a 20x20 grid?
#  y
#  3
#  2
#  1
#  0  1  2  3  ...
#   x:      #ich setzte es gedanklich so um, dass man nur nach rechts und oben machen kann - sollte ja egal sein, sonst bekomm ich einen Knoten im Schädel
from random import *



def gridmaze(n): #n=größe des gitters. 20 = 20x20 grid
    result, count = 0, 0
#     gridX, gridY = [], []
#     grid = [gridY, gridY]
    paths = []   #enthält strings mit gegangen Paden. U = Up & R= Right 

#    for i in range(0,n+1):   #Navigationspunkte für das Gitter erstellen (einer mehr, da man sich immer an den Ausenecken des Gitters bewegt)
#        gridX.append(i)
#        gridY.append(i)                #Gitter wurde doch nicht benötigt

    while count < 100:   #Puffer um Überlauf zu vermeiden (sollte am Ende ersetzt werden)
        x, y = 0, 0
        path = ""

        while not x == n and not y == n:
            if randint(0,1) == 0:
                if y != n:
                    y += 1  #move up
                    path = path + "U"
            else:
                if x != n:
                    x += 1  #rove right
                    path = path + "R"
        
        print(path)  #debug
        if not path in paths:
            paths.append(path)
            print(paths)  #debug
            result += 1 
        count += 1

    return result  # result = Anzahl der möglichen Wege.

print(gridmaze(20))  #schon wieder grausliche Laufzeit... wir versuchen statt Zufallsrouten nochmal neu mit konzipierten routen