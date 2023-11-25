#Variante von Euler9 im Zuge der Klausurvorbereitung am 25.11.2023 durchgemacht

def pythagoreisches_triple():
    for a in range(1, 1001):
        for b in range(a, 1001):
            c = 1000 - (a+b)
            if a**2 + b**2 == c**2:
                return a*b*c

print(pythagoreisches_triple())
