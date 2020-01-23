"""
To Read a List of Words and Return the Length of the Longest One
"""

user_list = []
line = input("Enter a list: ")

while(line != ''):
	user_list.append(line)
	line = input()

print(user_list)

largest = user_list[0]

for i in user_list:
    if len(largest) <= len(i):
        largest = i
    else:
        pass

print(largest)