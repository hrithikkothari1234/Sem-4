"""
Calc occurence of a word in a given string
"""
string = input(" Enter the string ")
user_word = input(" Enter word to calc its occurence ")
count = 0

list_string = string.split(' ')

for word in list_string:
    if word == user_word:
       count = count+1

print("Occurence is :",count)