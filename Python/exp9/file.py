## Q1

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

## Q2
import pickle

lines = open("cities_and_times.txt").readlines()
lines.sort()

cities = []
for line  in lines:
    *city, day, time = line.split()
    hours, minutes = time.split(":")
    cities.append((" ".join(city), day, (int(hours), int(minutes)) ))

print("\n",cities)
fh = open("cities_and_times.pkl", "bw")
pickle.dump(cities, fh)