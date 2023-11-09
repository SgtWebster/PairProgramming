# Project Euler 18 - https://projecteuler.net/problem=18 - Lösung ....
#  Maximum Path Sum I
#  Finde den maximalen Gesamtwert vom oberen zum unteren Ende des Dreiecks unten



triangle = [[75],
[95, 64],
[17, 47, 82],
[18, 35, 87, 10],
[20, 4, 82, 47, 65],
[19, 1, 23, 75, 3, 34],
[88, 2, 77, 73, 7, 63, 67],
[99, 65, 4, 28, 6, 16, 70, 92],
[41, 41, 26, 56, 83, 40, 80, 70, 33],
[41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
[63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
[4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]


def triangle_path(n): #anzahl der Ebenen -> im Beispiel sind es 15 ebenen
    x, y = 0, 0    #x und y Koordinaten (x = Index der Zahl in der Liste, y = Ebene der Pyramide (0 = Spitze, 14 = Boden))
    result = triangle[y][x]
    for i in range (0, n-3):
        if (triangle[i+2][x] + triangle[i+2][+1] >= triangle[i+2][x+1] + triangle[i+2][x+2]):
            if (triangle[i+2][x] + triangle[i+2][+1] >= triangle[i+2][x+1] + triangle[i+2][x+2]):
                break   #Hier hab ich mitn herumgewurstel aufgehört

            result = result + triangle[i+1][x]
        else:
            result = result + triangle[i+1][x+1]
        x = x+1
    





    if triangle[n-1][x] >= triangle[n-1][x+1]:
        result = result + triangle[n-1][x]
    else:
        result = result + triangle[n-1][x+1]        
    
    return result

print(triangle_path(15))

