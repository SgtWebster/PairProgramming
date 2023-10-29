#  ProjectEuler Problem 05 - https://projecteuler.net/problem=5 - Answer 232792560
# Zweiter Versuch, da der erste eine viel zu lange Laufzeit hatte   #Versuch mittels Hilfe ChatGPT

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10  without any remainder.
# What is the smallest positiv number that is evenly divisble by all of the numbers from 1 to 20?


def gcd(a, b):
    # Berechnet den größten gemeinsamen Teiler (ggT) von a und b.
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    # Berechnet das kleinste gemeinsame Vielfache (kgV) von a und b.
    return a * b // gcd(a, b)

def smallest_multiple(n):
    # Berechnet das kgV von allen Zahlen von 1 bis n.
    result = 1
    for i in range(1, n + 1):
        result = lcm(result, i)
    return result

# Kleinste Zahl, die durch alle Zahlen von 1 bis 20 teilbar ist
print(smallest_multiple(20))

