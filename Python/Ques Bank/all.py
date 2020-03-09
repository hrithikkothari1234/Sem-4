# Q1

def onehop(l):
    oh=[]

    for i in range(0, len(l)):
        for j in range(0, len(l)):
            if l[i][1]==l[j][0] and l[i][0]!=l[j][1]:
                oh += [(l[i][0], l[j][1])]

    myset=set(oh)
    return(sorted(myset))

print(onehop([(2,3),(1,2)]))
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
    
x = [3,2,1,2,3] # True
print(valley(x))
x = [3,3,2,1,2] # False
print(valley(x))

# Q3

def maxcount(l):
    maxfreq = 1

    for i in l:
        if maxfreq < l.count(i):
            maxfreq = l.count(i)

    print(maxfreq)

maxcount([1,17,31,17,22,17]) 
maxcount(["the", "higher", "you", "the", "you"]) 

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


print(sublist([3],[2,2,3,4,5]))

# Q5

user_str = input("Enter 2*n lines")
l1=[]
l2=[]

while user_str!='':
    l1.append(user_str)
    user_str=input()

if len(l1)%2!=0:
    print("Enter 2*n lines plis?")
else:
    for i in range(0, len(l1), 2):
        l2.append(l1[i])
        l1.remove(l1[i])

    l1.reverse()
    l2.reverse()

    for x,y in zip(l1, l2):
        print(x)
        print(y)

# Q6

def min3(x, y, z):
    if x<=y:
        if x<=z:
            min = x
        else:
            min = z
    else:
        if y<=z:
            min = y
        else:
            min = z
    
    return min

print(min3(5,12,9))

# Q7

def transpose(matr):
    result = [[0 for x in range(len(matr))] for y in range(len(matr[0]))] 

    for i in range(len(matr)):
        for j in range(len(matr[0])):
            result[j][i] = matr[i][j]
    
    return result

print(transpose([[1,4,9]])) 
print(transpose([[1,3,5],[2,4,6]]))
print(transpose([[1,1,1],[2,2,2],[3,3,3]]))

# Q8

def secondmax(l):
    (mymax,mysecondmax) = (0,0)
    mymax=max(l)
    for i in l: 
        if i < mymax and i>=mysecondmax:
            mysecondmax = i
    
    return mysecondmax
print(secondmax([4,1,5,9,10,13,6]))

# Q9

def myreverse(l):
    if l==[]:
        return(l)
    else:
        return [l[-1]] + myreverse(l[:-1])

l = ["a","b","c","d","e"]
print(myreverse(l))

# Q10

user_str = input("Enter ur sentence to calc uppercase and lowercase chars")
upper, lower = 0, 0

for i in range(0, len(user_str)):
    if user_str[i].isupper():
        upper+=1
    else:
        lower+=1

print("uppercase : ",upper)
print("lowercase : ",lower)

# Q11 A

### primefactors.py

# Q11 B

def printPascal(n): 
  
    arr = [[0 for x in range(n)]  
              for y in range(n)]  

    for line in range (0, n): 
        for i in range (0, line + 1): 
            if(i is 0 or i is line): 
                arr[line][i] = 1
                print(arr[line][i], end = " ")  
            else: 
                arr[line][i] = (arr[line - 1][i - 1] + 
                                arr[line - 1][i]) 
                print(arr[line][i], end = " ")              
        print("\n", end = "") 
  
n = 5
printPascal(n) 

# Q11 C

### perfectsquares.py

# Q12

def perfect(n):
    factors = []

    for i in range(2, n):
        if n%i == 0:
            factors.append(i)
    
    sum=1
    for i in factors:
        sum+=i
    
    if sum==n:
        return True
    else:
        return False

print(perfect(6))

# Q13

### Prac2

# Q14

def depth(eqn):

    list1 = []
    depth = []

    for i in range(0, len(eqn)):
        if eqn[i] == '(':
            list1.append(eqn[i])
            depth.append(len(list1))
        elif eqn[i] == ')':
            list1.pop()
    

    return max(depth)

print(depth('(a(a+b))(a-b)'))

# Q15

def count(l1):
    count=0
    for i in l1:
        if len(i)>=2 and i[0] == i[-1]:
            count=count+1
    return count

l1 = ["abca","world","abc","def","ded","hh","1231"]
print(count(l1))

# Q16

def front_x(x):
    temp1 = [] 
    for i in x:
        if i.startswith('x'):
            temp1.append(i)
            x.remove(i)
    x.sort()
    temp1.sort()
    return temp1+x

x=['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
print(front_x(x))

# Q17

def merge(l, r):
    result = []

    while l and r:
        if l[-1] > r[-1]:
            result.append(l.pop())
        else:
            result.append(r.pop())

    result+=(l+r)[::-1]
    result.reverse()
    return result

print(merge([1,2,6,7], [1,3,5,9]))

# Q18

def both_ends(s):
    if len(s)<2:
        return ""
    else:
        return s[0]+s[1]+s[-2]+s[-1]

print(both_ends("spring"))
    
# Q19

def fix_start(s):
    first_char = s[0]
    temp_str = s.replace(first_char, "*")
    return first_char + temp_str[1:]

print(fix_start("babble"))

# Q20

def mix_up(a, b):
    return b[0]+b[1]+a[2:]+" "+a[0]+a[1]+b[2:]

print(mix_up("dog", "dinner"))

# Q21

def not_bad(s):
    first_index = s.find('not')
    second_index = s.find('bad')

    if first_index != -1 and second_index != -1 and second_index > first_index:
        return s[0: first_index] + "good" + s[second_index+3: ]

print(not_bad('dinner is not that bad'))
