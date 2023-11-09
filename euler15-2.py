# Project Euler 15 - https://projecteuler.net/problem=15 - Lösung 137846528820
#Lattice Paths
#Starting in the top left corner of a 2x2 grid, and only being able to move to the (!)right and down(!), there are exactly  6 routes to the bottom right corner.
#how many such routes are there trough a 20x20 grid?
#  y
#  3
#  2
#  1
#  0  1  2  3  ...
#   x:      #ich setzte es gedanklich so um, dass man nur nach rechts und oben machen kann - sollte ja egal sein, sonst bekomm ich einen Knoten im Schädel

#Funktionen für Move-Right und Move-Up um Redundanzen zu vermeiden:

def fakultaet(x):  # Fakultätsberechnung von gegebener Zahl x
    result = 1
    for i in range(1, x+1):
        result = result * i
    return result

    
def gridmaze(n): #n=größe des gitters. 20 = 20x20 grid 
    result = fakultaet(n*2) / (fakultaet(n) * fakultaet(n) )     #ergoogelt wie soetwas zu berechnen ist
    return int(result)

print(gridmaze(20))  