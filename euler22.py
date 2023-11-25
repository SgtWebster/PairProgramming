# Project Euler 22 - https://projecteuler.net/problem=22 - Lösung 871198282
# Names Score

alphabet = {
    "A" : 1,
    "B" : 2,
    "C" : 3,
    "D" : 4,
    "E" : 5,
    "F" : 6,
    "G" : 7,
    "H" : 8,
    "I" : 9,
    "J" : 10,
    "K" : 11,
    "L" : 12,
    "M" : 13,
    "N" : 14,
    "O" : 15,
    "P" : 16,
    "Q" : 17,
    "R" : 18,
    "S" : 19,
    "T" : 20,
    "U" : 21,
    "V" : 22,
    "W" : 23,
    "X" : 24,
    "Y" : 25,
    "Z" : 26
}

from os.path import dirname, join
names = open(join(dirname(__file__), "euler22_names.txt")).read().replace("\"", "").split(",")
names.sort()

def name_score(n):  #erwartet: Liste
    result = 0
    for name in n:
        namescore = 0
        for char in name:
            namescore += alphabet[char]    
        result += (namescore * (n.index(name)+1))
        
    return result

#print(names)
print(name_score(names))