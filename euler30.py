# Project Euler 30 - https://projecteuler.net/problem=30 - Lösung 443839
# Digit Fifth Powers

def create_digitpowerlist(pow): # x = input wie hoch die Potenz sein soll
    powerlist = {}
    for i in range(0,9+1):
        powerlist[i] = i**pow
    return powerlist

def get_digits(n):    # Int wird in einzelne Digits aufgeteilt
    digits = []
    for number in str(n):
        digits.append(int(number))
    return digits

def digitpower(x):    # x = input wie hoch die Potenz sein soll
    result = 0
    powerlist = create_digitpowerlist(x)
 
    for i in range(2, 1000000):   #<<< einfach auf Verdacht bis 1.000.000
        checknumber = get_digits(i)
        checksum = 0
        for number in checknumber:
            checksum += powerlist[number]
        if checksum == i:
            result += i
            print(i)
    return result


print(digitpower(5))