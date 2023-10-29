# Project Euler 06 - https://projecteuler.net/problem=6 - Lösung 25164150

def sumsquares(x):  ## Summe der Quadratwurzeln in der Reichweite von 1 bis x
    result = 0
    for i in range(1,x+1):
        result = result + i**2
        
    return result

# print(sumsquares(10)) test1

def squaresum(x):  ## Summe der natürlichen Zahlen von 1 bis x - diese Summe im Quadrat
    result = 0
    for i in range(1,x+1):
        result = result + i
    result = result ** 2
    return result

# print(squaresum(10))  test2

def squaresumdif(x):
    result = squaresum(x) - sumsquares(x)
    return result

print(squaresumdif(100))