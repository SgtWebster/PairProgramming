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
         

print(palindromic_number(3))    # Test