#  ProjectEuler Problem 05 - https://projecteuler.net/problem=5 - Lösung: 232792560
# dritter Versuch

# wir versuchen eine Funktion für den größten gemeinsamen Teiler (ggT) zu finden. z.B. 9 und 12 ist der ggT 3

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10  without any remainder.
# What is the smallest positiv number that is evenly divisble by all of the numbers from 1 to 20?

def ggT (x, y):
    result = 0
    for i in range (1, max(x, y)+1):
        if x % i == 0 and y % i == 0:
            result = i

    return result


# Und in diesem Zuge noch das kleinstes gemeinsames Vielfache

def kgV (x, y):
    result = (x * y) / ggT(x, y)
    return int(result)


print("ggt", ggT(18, 27))
print("kgV", kgV(18, 27))


def smallest_multiple(x):
    result = 1

    for i in range(1, x+1):  ###Das hier passt noch nicht
        result = kgV(i, result)
    
    return result

print("smallest_multiple", smallest_multiple(20))
