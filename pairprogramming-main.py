#  ProjectEuler Problem 01 - https://projecteuler.net/problem=1 - Answer 233168
def multiples(x):

    result = 0

    for x in range(1,x):
        if x % 3 == 0:
            result = result + x
        elif x % 5 == 0:
            result = result + x


    return result

# print(multiples(1000))  #Test
#GitTest

#---------------------------------------------------------------------------------------------
#  ProjectEuler Problem 02 - https://projecteuler.net/problem=2 - Answer 4613732

def fibonacci(x):
    
    result = 0
    a = 1
    b = 1
    fib = 0

    while fib < x:
        fib = a + b

        if fib % 2 == 0:
            result = result + fib

        a = b
        b = fib

    return result

# print(fibonacci(4000000))  #Test

#---------------------------------------------------------------------------------------------
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
        while x % i == 0 and is_prime(i):    # Während x durch i teilbar ist und i eine Primzahl ist, aktualisiert den höchsten Primfaktor und teilt x durch i            highest_prime = i 
            x = x // i       # Teile x durch den gefundenen Primfaktor i

    if x > 2 and is_prime(x):    # Wenn x nach der obigen Schleife größer als 2 ist und eine Primzahl ist, dann ist x selbst der höchste Primfaktor von der ursprünglichen Zahl
        highest_prime = x

    return highest_prime


# print (primefactor(600851475143))  #TEst

#---------------------------------------------------------------------------------------------
#  ProjectEuler Problem 04 - https://projecteuler.net/problem=4 - Answer 906609

def palindrome(x):
    return int(str(x)[::-1])    # String umdrehen   #Eigene Funktion dafür wirklich sinnvoll???  # Teile und herrsche :p 


def is_palindrome(x):
    return x == palindrome(x)   # Prüfen ob eingegebener String ein Palindrom ist


def palindromic_number(x):   # x ist die Anzahl der Ziffern - also 3 würde bedeuten, alles von 0 bis 999

    dezimal = (10 ** x) - 1
    result = 0

    for i in range(dezimal,1,-1):
        for l in range(i,1,-1):
            if (i * l) > result and is_palindrome(i * l):
                result = i * l
    
    return result
         

# print(palindromic_number(3))    # Test

#  ProjectEuler Problem 05 - https://projecteuler.net/problem=5 - Answer ?

def is_even_multiple(x, y):
    result = 0
    for i in range(1,y+1):   ##prüfen wie oft eine Zahl von in der Reichweite 1 bis y+1 durch alle Zahlen Restlos geteilt werden kann  
        if x % i == 0:
            result = result + 1
        else:
            return False
    
    if result == y:   #wenn in dier angegeben Reichweite (z.B. x = 10) alle Zahlen ohne Rest teilen konnte, dann erfolgreich (=True)
        return True

    return False


def multiple(x):  # x bedeutet Zahlen von 1 bis x
    result = 1
    multiple_range = x

    while is_even_multiple(result, multiple_range) == False:     #Beginnend mit 1, solange nicht eine Zahl mit allen Zahlen von 1 bis x restlos teilbar ist.
        result = result + 1
        print(result)
    return result

print(multiple(10))

#---------------------------------------------------------------------------------------------

