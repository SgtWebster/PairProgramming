#  ProjectEuler Problem 05 - https://projecteuler.net/problem=5 - Answer ?

def is_even_multiple(x, y):
    result = 0
    for i in range(1,y+1):   ##prüfen wie oft eine Zahl von in der Reichweite 1 bis y+1 durch alle Zahlen Restlos geteilt werden kann  
        if x % i == 0:
            result = result + 1
        else:
            return False
    
    if result == y:   #wenn in dier angegeben Reichweite (z.B. x = 10) alle Zahlen ohne Rest teilen konnte, dann erfolgreich (=True)
        return True

    return False


def multiple(x):  # x bedeutet Zahlen von 1 bis x
    result = 1
    multiple_range = x

    while is_even_multiple(result, multiple_range) == False:     #Beginnend mit 1, solange nicht eine Zahl mit allen Zahlen von 1 bis x restlos teilbar ist.
        result = result + 1
        print(result)
    return result

print(multiple(20))