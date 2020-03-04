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

for i in range(0, len(list_tups)):
        for j in range(0, len(list_tups)-1):
            if int(list_tups[j][-1]) > int(list_tups[j+1][-1]):
                list_tups[j], list_tups[j+1] = list_tups[j+1], list_tups[j]

print("Sorted list is:",list_tups)