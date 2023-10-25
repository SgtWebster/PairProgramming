#  ProjectEuler Problem 02 - https://projecteuler.net/problem=2 - Answer 4613732

def fibonacci(x):
    
    result = 0
    a = 1
    b = 1
    fib = 0

    while fib < x:
        fib = a + b

        if fib % 2 == 0:
            result = result + fib

        a = b
        b = fib

    return result

print(fibonacci(4000000))  #Test