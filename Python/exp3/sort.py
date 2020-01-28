"""
To Sort a List of Tuples by the Last Element in Each Tuple. 
"""

list_tups = []
sorted_list = []

line = input("Enter the list of tuples: ")
while(line != ''):
    list_tups.append(tuple(line.split()))
    line = input()
 
print(list_tups)

list_tups.sort(key = lambda x: x[-1])
print("Sorted list is:",list_tups)