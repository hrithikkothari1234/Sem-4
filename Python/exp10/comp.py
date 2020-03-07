# Validating Credit Card Numbers

# Link to the problem : https://www.hackerrank.com/challenges/validating-credit-card-number/problem

"""
You and Fredrick are good friends. Yesterday, Fredrick received  credit cards from ABCD Bank. He wants to verify whether his credit card numbers are valid or not. You happen to be great at regex so he is asking for your help!

A valid credit card from ABCD Bank has the following characteristics:

► It must start with a 4,5 or 6.
► It must contain exactly 16 digits.
► It must only consist of digits (0-9).
► It may have digits in groups of 4, separated by one hyphen "-".
► It must NOT use any other separator like ' ' , '_', etc.
► It must NOT have 4 or more consecutive repeated digits.

Valid Credit Card Numbers :
    4253625879615786
    4424424424442444
    5122-2368-7954-3214

Invalid Credit Card Numbers :
    42536258796157867       #17 digits in card number → Invalid 
    4424444424442444        #Consecutive digits are repeating 4 or more times → Invalid
    5122-2368-7954 - 3214   #Separators other than '-' are used → Invalid
    44244x4424442444        #Contains non digit characters → Invalid
    0525362587961578        #Doesn't start with 4, 5 or 6 → Invalid
"""

def validate_cred(cred=" "):
    valid = False

    if len(cred)!=16 and len(cred)!=19:
        return valid
    
    if cred[0]!='4' and cred[0]!='5' and cred[0]!='6':
        return valid

    for i in range(0, len(cred)-3):
        if cred[i] == cred[i+1] == cred[i+2] == cred[i+3]:
            return valid

    if(len(cred)==19):
        for i in range(0, len(cred)-5, 5):
            i=i+4
            if cred[i]!='-':
                return valid
    
    for i in range(0, len(cred)):
        if cred[i]!='-':
            try:
                x = int(cred[i])
            except ValueError:
                return valid

    valid = True
    return valid

line = input("Enter credit card numbers")

l1 = []

while(line!=''):
    l1.append(line)
    line=input()

for i in l1:
    if validate_cred(i):
        print(i,"Valid")
    else:
        print(i,"Invalid")