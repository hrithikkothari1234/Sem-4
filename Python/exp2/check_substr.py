"""
To Check if a Substring is Present in a Given String
"""

user_str = input("Enter a string")
user_substr = input("Enter a substring")

# Prints index at which substr was found ( if found else -1)
print(user_str.find(user_substr))