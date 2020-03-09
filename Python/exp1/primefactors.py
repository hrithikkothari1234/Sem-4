"""
Calc prime factors of a given number
"""

def check_prime( val ):
    """
    Check which factors are prime
    """
    for i in range(2, val):
        if(val%i == 0):
            return 0
    return 1

val = int(input("Enter number to find prime factors : "))
print(val)


factors = []
primefactors = []

for i in range(2, int(val/2)):
    if(val%i == 0):
        factors.append(i)


for i in range(0, len(factors)):
    if(check_prime(factors[i])):
        primefactors.append(factors[i])
        
print(primefactors)
