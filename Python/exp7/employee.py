class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __mul__(self, a):
        return self.salary * a.workingdays

    def __eq__(self, a):
        return self.salary == a.salary

    def __add__(self, a):
        sum = self.salary
        for i in a:
            sum = sum + i.salary
        return sum


class attendance:
    def __init__(self, name, workingdays):
        self.name = name
        self.workingdays = workingdays

e1 = employee("Hritik", 1000)
a1 = attendance("Hritik", 50)
e2 = employee("Abc", 1001)
e3 = employee("Def", 5050)
l1 = [e2,e3]

print(e1 * a1)
print(e1 == e2)
print(e1 + l1)