"""
To Find all Numbers in a Range which are Perfect Squares and 
Sum of all Digits in the Number is Less than 10
"""
def perfect_square(val):
    return int(val**(1/2)) ** 2 == val
    
def sum_lessthan_10(val):
    sum = 0
    while(val > 0):
        i = val % 10
        sum = sum + i
        val = int(val / 10)
    return sum<10

upper = int(input("Enter upper range :"))
lower = int(input("Enter lower range :"))

list_req = []

for i in range(lower, upper):
    if(perfect_square(i) and sum_lessthan_10(i)):
        list_req.append(i)

print(list_req)