# Project Euler 20 - https://projecteuler.net/problem=20 - Lösung 
# Factorial Digit Sum


def fakultaet(x): # x = zahl für Fakultät-Berechnung
    result = 1
    for number in range(1,x+1):
        result *= number
    return result

def sum_digits(n):
    result = 0
    for digit in str(n):
        result += int(digit)
    return result

#print(fakultaet(10))   #debug

print(sum_digits(fakultaet(100)))



