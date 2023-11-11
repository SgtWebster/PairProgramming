# Project Euler 18 - https://projecteuler.net/problem=18 - Lösung ....
#  Maximum Path Sum I
#  Finde den maximalen Gesamtwert vom oberen zum unteren Ende des Dreiecks unten


triangle = [  [75],                                         #00 Index
             [95, 64],                                      #01
            [17, 47, 82],                                   #02
           [18, 35, 87, 10],                                #03
          [20, 4, 82, 47, 65],                              #04
         [19, 1, 23, 75, 3, 34],                            #05
        [88, 2, 77, 73, 7, 63, 67],                         #06
       [99, 65, 4, 28, 6, 16, 70, 92],                      #07
      [41, 41, 26, 56, 83, 40, 80, 70, 33],                 #08
     [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],              #09
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],           #10
   [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],        #11
  [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],     #12
 [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],   #13
[4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]  #14

triangle2 = [[3],
           [7, 4,],
         [2, 4, 6,],
        [8, 5, 9, 3]]



def triangle_path(tri):   #Array mit Triangle übergeben
    result = tri[0][0]
    max_row = len(tri)-1
    serching_index = 0

    for row in range(0,max_row):
        if tri[row+1][serching_index] > tri[row+1][serching_index+1]:
            result += tri[row+1][serching_index]
        else:
            result += tri[row+1][serching_index+1]
            serching_index += 1


    return result


print(triangle_path(triangle))   

