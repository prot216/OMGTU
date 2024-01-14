import math
N = int(input('Enter N: '))

def razvedka(n):
    if n == 3:
        return 1
    elif n < 3:
        return 0
    elif n > 3:
        group1 = math.floor(n/2)
        group2 = math.floor(n/2) + (n%2)
        return razvedka(group1) + razvedka(group2)
        
print(razvedka(N))