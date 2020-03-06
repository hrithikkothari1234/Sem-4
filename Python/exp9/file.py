try:
    f = open("test.txt")
    file_contents = f.read()
    (spaces, tabs, newlines) = (0, 0, 0)
    for character in file_contents:
        if character == " ":
            spaces +=1
        elif character == '\t': 
            tabs += 1
        elif character == '\n': 
            newlines += 1
    print("Spaces : ",spaces)
    print("Tabs : ",tabs)
    print("Newlines : ",newlines)
    f.close()

except IOError:
    pass