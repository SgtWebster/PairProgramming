#  ProjectEuler Problem 03 - https://projecteuler.net/problem=3 - Answer 6857

def is_prime(x):   #Erster Schritt: Prüfen ob eine Zahl eine Primzahl ist
    if x < 2:
        return False

    for i in range(2, int(x ** 0.5) + 1):  #Überprüfe alle Zahlen von 2 bis zur Quadratwurzel von x (abgerundet) + 1
        if x % i == 0:     #Wenn x durch i ohne Rest teilbar ist, ist x keine Primzahl
            return False   #Gibt False zurück, wenn x keine Primzahl ist
    return True        #Wenn keine der Zahlen ein Teiler von x ist, gibt True zurück, um anzugeben, dass x eine Primzahl ist

def primefactor(x):
    highest_prime = 2       #Initialisiere die Variable highest_prime mit 2, da 2 die kleinste Primzahl ist

    for i in range(3, int(x ** 0.5) + 1, 2):
        while x % i == 0 and is_prime(i):    # Während x durch i teilbar ist und i eine Primzahl ist, aktualisiert den höchsten Primfaktor und teilt x durch i            
            highest_prime = i 
            x = x // i       # Teile x durch den gefundenen Primfaktor i

    if x > 2 and is_prime(x):    # Wenn x nach der obigen Schleife größer als 2 ist und eine Primzahl ist, dann ist x selbst der höchste Primfaktor von der ursprünglichen Zahl
        highest_prime = x

    return highest_prime

print (primefactor(600851475143))  #TEst