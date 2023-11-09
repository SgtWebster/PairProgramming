# Project Euler 14 - https://projecteuler.net/problem=14 - Lösung 837799
# Longest Collatz Sequence

#The following iterative sequence is defined for the set of positive integers:
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1.
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.


# Prüfen ob eine Zahl gerade (even) ist:
#def is_even(x):
#    if x % 2 == 0:
#        return True
#    return False

#def collatz_even(n):  #Collatz Regel, wenn gerade ist
#    return int(n/2)

#def collatz_odd(n):   #Collatz REgel, wenn ungerade ist
#    return int((3 * n) + 1)
#### Die "Unterfunktionen" brauchen zu viel Laufzeit, daher direkt in den Hauptcode implementiert

#und nun das eigentliche Problem

def collatz_problem(x):   # x = Maximale Startnummer  (im Beispiel: 1.000.000)
    result, resultcount = 0, 0
    for i in range(x, 0, -1):   #beginnt bei maximaler Startnummer und arbeitet sich nach unten durch
        print(i)
        calculation = i    
        count = 0
        while calculation > 1: 
            if calculation % 2 == 0:   #prüfen ob gerade
                calculation = int(calculation/2)
            else:
                calculation = int((3 * calculation) + 1)
            count += 1    #wie lange ist die bisherige Zahlenreihe
            if count > resultcount:   #ist die derzeitige Zahlenreihe schon größer als die bisher größte?
                result = i
                resultcount = count
    return result, resultcount

print(collatz_problem(1000000)) # Mal wieder eine Schweinslaufzeit, aber das Ergebnis ist richtig

