# Q1

def onehop(l):
    oh=[]

    for i in range(0, len(l)):
        for j in range(0, len(l)):
            if l[i][1]==l[j][0] and l[i][0]!=l[j][1]:
                oh += [(l[i][0], l[j][1])]

    myset=set(oh)
    return(sorted(myset))

# Test cases

print(onehop([(2,3),(1,2)]))

print(onehop([(2,3),(1,2),(3,1),(1,3),(3,2),(2,4),(4,1)]))

print(onehop([(1,2),(3,4),(5,6)]))

# Q2

def valley(x):
    
    for i in range(0, len(x)):
        if x[i] != x[len(x)-i-1]:
            #if not palindrome
            return False
 
    #if palindrome
    for i in range(0, int(len(x)/2)):
        if x[i] <= x[i+1]:
            #if first half not in decr order
            return False
  
    #if first half in decr order
    return True
    
# Test cases

x = [3,2,1,2,3]
print(valley(x))

x = [3,3,2,1,2] 
print(valley(x))

# Q3

def maxcount(l):
    maxfreq = 1

    for i in l:
        if maxfreq < l.count(i):
            maxfreq = l.count(i)

    return maxfreq

# Test cases

print(maxcount(["the","higher","you","climb","the","further","you","fall"]))

print(maxcount(["the","higher","you","climb","the","further","you","fall","you","climb","the",
"further","you","fall"]))

# Q4

def sublist(l1, l2):
    if l1==[]:
        return True
    elif l2==[]:
        return False
    else:
        for i in range(0, len(l2)):
            if l2[i] == l1[0]:
                f = 0
                for j in range(0, len(l1)):
                    if l1[j] != l2[i+j]:
                        f = 1
                        break
                if f==0:
                    break
        
        if f==0:
            return True
        else:
            return False

# Test cases

print(sublist([2,2,3],[2,2,3,4,5]))

print(sublist([2,2,4],[2,2,3,4,5]))

print(sublist([2,2,3],[2,2,3,4,5]))

print(sublist([2,2,4],[2,2,3,4,5]))

# Q5

user_str = input("Enter 2*n lines")
l=[]

while user_str!='':
    l.append(user_str)
    user_str=input()

if len(l)%2!=0:
    print("Enter 2*n lines plis?")
else:
    n=len(l)  #Taking length of input list
    a=n//2  #divide this list in two parts
    l1=l[a:]
    l2=l[:a]
    for i in l1:   #printing the list
        print(i)
    for i in l2:
        print(i)

# Q6

for i in range(101):
    if i%3==0 and i%5!=0:
        print('fizz')
    elif i%5==0 and i%3!=0:
        print('buzz')
    elif i%3==0 and i%5==0:
        print('fizzbuzz')
    else:
        print(i)


# Shorter fizzbuzz: 56 Characters.
for i in range(101):
	print("Fizz"[i%3*4:]+"Buzz"[i%5*4:] or i)