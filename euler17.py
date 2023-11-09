# Project Euler 17 - https://projecteuler.net/problem=17 - Lösung 21124 


one_digit_dic = {0: "", 1 : "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
two_digit_dic = {0: "", 1: "ten", 2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 6: one_digit_dic[6]+"ty", 7: one_digit_dic[7]+"ty", 8: one_digit_dic[8]+"y", 9: one_digit_dic[9]+"ty"}
three_digit_dic = {0: "", 1: one_digit_dic[1]+"hundred", 2: one_digit_dic[2]+"hundred", 3: one_digit_dic[3]+"hundred", 4: one_digit_dic[4]+"hundred", 5: one_digit_dic[5]+"hundred", 6: one_digit_dic[6]+"hundred", 7: one_digit_dic[7]+"hundred", 8: one_digit_dic[8]+"hundred", 9: one_digit_dic[9]+"hundred"} 
special_digit_dic = {"00": "", "10": "ten", "11": "eleven", "12": "twelve", "13": "thirteen", "14": "fourteen", "15": "fifteen", "16": one_digit_dic[6]+"teen", "17": one_digit_dic[7]+"teen", "18": one_digit_dic[8]+"een", "19": one_digit_dic[9]+"teen"}

def number_letters(n): # welche Zahl soll in Buchstaben umgerechnet werden... z.B x = 451 => fourhundredfiftyone
    digit_one, digit_two, digit_three, digit_four = "", "", "", ""
    number_one, number_two, number_twoone, number_three, number_four = 0, 0, 0, 0, 0

    number_one = int(str(n)[len(str(n))-1])
    if n >= 10:
        number_two = int(str(n)[len(str(n))-2])
        number_twoone = (int(str(n)[len(str(n))-2])*10) + int(str(n)[len(str(n))-1])
    if n >= 100:
        number_three = int(str(n)[len(str(n))-3])

    if n > 0:
        digit_one = one_digit_dic[number_one]
        if number_twoone >= 10 and number_twoone <20 :
            if (number_one + number_two) == 0:
                digit_two = ""
            else:
                digit_two = special_digit_dic[str(n)[len(str(n))-2] + str(n)[len(str(n))-1]]
                digit_one = ""
        if n >= 20 and number_twoone >= 20:
            digit_two = two_digit_dic[number_two]
            
        if n >= 100:
            digit_three = three_digit_dic[number_three]
            if number_twoone > 0:
                digit_three = digit_three + "and"
            if n >= 1000:
                digit_four = "onethousand"
                if n >= 2000:
                    return False

    result = digit_four + digit_three + digit_two + digit_one

    return result

#print(number_letters(115))    #debug
#print(len(number_letters(115)))   #debug

def letter_counts(x): #bis zu welcher Nummer (x = 5 = 1+2+3+4+5)
    result = 0
    for i in range (0,x+1):
        print(i, number_letters(i))    #debug
        result = result + int(len(number_letters(i)))
    return result

print(letter_counts(1000))   