
def generate_dict(n):
    """
    Generate dict n:n*2
    """
    for i in range(1,n+1):
        user_dict[i]=i*i

    print(user_dict)

def merge_dict():
    """
    Merging two dicts
    """
    user_dict2 = dict()
    nt = int(input("Enter value of n for second dict"))

    for i in range(n,nt+1):
        user_dict2[i]=i*i
        
    user_dict.update(user_dict2)
    print("After merging : \n",user_dict)


def sort_dict():
    """
    Sorting a dict
    """
    random_dict={1:1, 9:3, 16:4, 20:2, 55:5, 0:0}
    print("Sorted Dict \n",dict(sorted(random_dict.items())))

def remove_key(k):
    """
    Remove a key from the dict
    """
    user_dict.pop(k)
    print("After removing: \n", user_dict)

def unique_val():
    """
    Convert dict values to a set to get unique values
    """
    temp_set = set(user_dict.values())
    print("Unique values \n", temp_set)
    
def highest_three():
    """
    Get highest 3 vals in the dict
    """
    print("Highest 3 vals are \n",sorted(user_dict.items(), reverse=True)[:3])

def count_freq(user_str):
    word_list = list(user_str.split())
    freq_list = []
    for i in word_list:
        freq_list.append(word_list.count(i))
    count_dict = dict(zip(word_list, freq_list))
    print(count_dict)
        
user_dict = dict()

n = int(input("Enter value of n"))
generate_dict(n)

merge_dict()
sort_dict()
remove_key(5)
highest_three()

user_str = input("Enter string to count freq of words")
count_freq(user_str)