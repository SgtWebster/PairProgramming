# Project Euler 09 - https://projecteuler.net/problem=9 - Lösung 31875000
# Special Pythagorean Triplet

# A Pythagorean triplet is a set of three natural numbers, a < b < c for which
# a² + b² = c²
# For example, 3² + 4² = 9 + 16 = 25 = 5²

# There exists exactly one Pythagorean triplet for which a + b + c = 1000
# Find the product abc.


def pythagorean_triple(x): #wobei x die gesuchte Zahl ist (z.B 1000)
    a_qa, b_qa, c_qa = 0, 0, 0
   
    for a in range(1, int(x/3)):
        a_qa = a**2
        for b in range(a+1, int(x-a)+1):
            b_qa = b**2

            c_qa = (a_qa+b_qa)
            c = c_qa**0.5
            if (c**0.5) % 2 == 0:
                c = int(c)

#            print("a ",a ,"b ", b,"c ", c, (a+b+c), (a*b*c))   # Test für Debugging

            if (a+b+c) == x and b != c:
                return int(a*b*c)

    return False

print(pythagorean_triple(1000))

