"""
To Ignore the Duplicates from a List and add only if not present already
"""
user_list = []
line = input("Enter a list: ")

while(line != ''):
	user_list.append(line)
	line = input()

print(user_list)

word = input("Enter next element , if present wont be added")
if word not in user_list:
    user_list.append(word)

print("Final list is ", user_list)