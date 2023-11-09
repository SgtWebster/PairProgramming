# File zum herumprobieren... einfach überschreiben

def is_prime(x):   #von euler03 übernommen  #Überlegung: wenn x eien Primzahl ist, dann können wir diese getrost überspringen
    if x < 2:
        return False

    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def triaglenumbers(x): # Anzahl der gesuchten Divisoren - "mehr als" (Aufgabenstellung: "over five hundred")
    count = 0
    triangle = 0
   
    while True:
        count += 1
        triangle = int((count*(count+1))/2) 
        divisors = 0
        if not is_prime(triangle):
            for i in range(1,int((triangle+1)*0.5)):   #
                if triangle % i == 0:
                    divisors += 1
    
        if divisors > x:
            print("breakpoint: count", count, "triangle", triangle, "divisors", divisors)
            break
        print("count", count, "triangle", triangle, "divisors", divisors)  #debug
    return triangle


#print(triaglenumbers(6))   #furchtbare Laufzeit #Breakpoint bei 41040

print((2**142))