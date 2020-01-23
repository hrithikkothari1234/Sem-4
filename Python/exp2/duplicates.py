"""
To find duplicate characters in a given string. 
"""
user_str = input("Enter a string")

list_1 = [] #Og list
list_2 = [] #Duplicates

for char in user_str:
    if char not in list_1:
        list_1.append(char)
    else:
        list_2.append(char)
        
print("List 1: ",list_1)
print("List 2: ",list_2)