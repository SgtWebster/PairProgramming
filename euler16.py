# Project Euler 16 - https://projecteuler.net/problem=16 - Lösung 1366
# Power Digit Sum
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26
# What is the sum of the digits auf the number 2^10000

def powerdigit(x): # x = exponent (also 2^x)
    result = 0
    calculation = int(2**x)

    for i in range(0, len(str(calculation))):
        result += int(str(calculation)[i])
    return result


print(powerdigit(1000))   #diese Aufgabe war wieder auserordentlich einfach

