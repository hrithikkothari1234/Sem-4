list_1 = list(range(1, 50))

front = int(input("enter first index: "))
end = int(input("enter last index: "))

print(list_1[front:end])

a = int(input("Enter a value to print numbers in the list_1 divisible by it"))

for i in list_1:
    if i%a==0:
        print(i)