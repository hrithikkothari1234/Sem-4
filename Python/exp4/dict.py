
def generate_dict(n):
    d1 = dict()
    for i in range(1,n+1):
        d1[i]=i*i

    return d1

def merge_dict(d1,d2):
    d1.update(d2)
    print("After merging : \n",d1)

def sort_dict(d1):
    print("Sorted Dict \n",dict(sorted(d1.items())))

def remove_key(d1,k):
    d1.pop(k)
    print("After removing: \n", d1)

def unique_val(d1):
     print(set(d1.values()))
    
def highest_three(d1):
    print(sorted(d1.items(), reverse=True)[:3])

def count_freq(d1,user_str):
    word_list = list(user_str.split())
    freq_list = []
    for i in word_list:
        freq_list.append(word_list.count(i))
    count_dict = dict(zip(word_list, freq_list))
    print(count_dict)
        

n = int(input("Enter value of n"))
d1=generate_dict(n)
print(d1)

merge_dict(d1,{6:36,7:49,8:64})
sort_dict(d1)
remove_key(d1,5)
highest_three(d1)

user_str = input("Enter string to count freq of words")
count_freq(d1, user_str)