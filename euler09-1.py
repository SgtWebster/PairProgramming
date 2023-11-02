# Project Euler 09 - https://projecteuler.net/problem=9 -
# Special Pythagorean Triplet

# A Pythagorean triplet is a set of three natural numbers, a < b < c for which
# a² + b² = c²
# For example, 3² + 4² = 9 + 16 = 25 = 5²

# There exists exactly one Pythagorean triplet for which a + b + c = 1000
# Find the product abc.


def pythagorean_triple(x): #wobei x die gesuchte Zahl ist (z.B 1000)
    a, b, c, result = 0, 0, 0, 0
    
    for i in range(1, int(x/3)):
        a = i**2
        for l in range(i+1, int(x-a)+1):
            b = l**2

            c = (i+l)**2
            print("a ",i ,"b ", l,"c", (i+l), "Wurzel c ", c**0.5)
            if (c**0.5) % 2 == 0:
                break
            if ((i+l)*2) == x:
                result = i*l*(i+l)
                break

    return result

print(pythagorean_triple(50))

# schreckliche Laufzeit
# fehlerhaftes Ergebnis - neuer Versuch in neuer Datei