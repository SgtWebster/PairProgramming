#  ProjectEuler Problem 01 - https://projecteuler.net/problem=1 - Answer 233168
def multiples(x):

    result = 0

    for x in range(1,x):
        if x % 3 == 0:
            result = result + x
        elif x % 5 == 0:
            result = result + x


    return result

print(multiples(1000))