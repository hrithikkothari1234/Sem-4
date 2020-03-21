
# exp 6-14 , assignment 2 , tutorial 1

# Q6

class Time:

    def __init__(self, hours, mins):
        self.hours = hours
        self.mins = mins
    
    def addTime(self, timeobj):
        self.hours = self.hours + timeobj.hours
        self.mins = self.mins + timeobj.mins

        if self.mins>=60:
            self.hours+=1
            self.mins-=60
    
    def displayTime(self):
        print(str(self.hours)+' hours '+str(self.mins) +' mins ')
        
    def displayMinute(self):
        hours = self.hours
        mins = self.mins
        while hours!=0:
            hours-=1
            mins+=60

        print(str(mins) +' mins ')

t1 = Time(3,40)
t2 = Time(2,50)

t1.displayTime()
t1.displayMinute()

t1.addTime(t2)
t1.displayTime()
t1.displayMinute()

# Q10

class AgeError(Exception):

    def __init__(self, age):
        if age <= 20:
            print("Too Young Exception")
        else:
            print("Too old Exception")

try:
    no = int(input("Enter the no of aspirants"))

    for i in range(no):
        age = int(input("Enter the age of aspirant"))
        
        if age <=20 or age>=50:
            raise AgeError(age)
        
except AgeError:
    pass

# Q12

class Polygon:
    
    def __init__(self, sides):
        self.sides = sides
        self.mag = []
    
    def inputSides(self):
        print("Enter the magnitude of the sides")
        for i in range(self.sides):
            mag = int(input())
            self.mag.append(mag)
    
    def dispSides(self):
        print(self.mag)

class Triangle(Polygon):
    
    def __init__(self):
        Polygon.__init__(self, 3)

    def findArea(self):
        # Using herons formula i.e. s = a+b+c/2 and area = s(s-a)(s-b)(s-c)**1/2
        s = sum(self.mag)/2
        area = (s*(s-self.mag[0])*(s-self.mag[1])*(s-self.mag[2]))**(1/2)
        print("Area is",area)

t = Triangle()
t.inputSides()
t.dispSides()
t.findArea()


# Q13

from tkinter import *

window = Tk()
window.wm_title("Registration Form")

### Labels

form_label = Label(window, font=("Helvetica", 20), text="Registration form")
form_label.place(x=150, y=30)

name_label = Label(window, text="Fullname")
name_label.place(x=100, y=100)

email_label = Label(window, text="Email")
email_label.place(x=100, y=150)

gender_label = Label(window, text="Gender")
gender_label.place(x=100, y=200)

country_label = Label(window, text="Country")
country_label.place(x=100, y=250)

programming_label = Label(window, text="Programming")
programming_label.place(x=100, y=300)

### Entries

name_entry = Entry(window)
name_entry.place(x=250, y=100)

email_entry = Entry(window)
email_entry.place(x=250, y=150)

### Radio buttons

male_rad = Radiobutton(window, text="Male", value=1)
female_rad = Radiobutton(window, text="Female", value=2)

male_rad.place(x=250, y=200)
female_rad.place(x=300, y=200)

### Dropdowns

countries = ["Australia", "America", "India", "China", "Russia"]
variable = StringVar(window)
variable.set("Select your country")
dropdown = OptionMenu(window, variable, *countries)
dropdown.place(x=240, y=250)

### Checkbuttons

java_butt = Checkbutton(window, text="Java")
py_butt = Checkbutton(window, text="Python")

java_butt.place(x=250, y=300)
py_butt.place(x=300, y=300)

### Button

submit_button = Button(window, text="Submit", bg="red", width="20", fg="white")
submit_button.place(x=180, y=350)

window.geometry("500x500")
window.resizable(False, False)
window.mainloop()


# Q14

class ApplicantError(Exception):

    def __init__(self, gender, language):

        if gender != "female" and language != "english":
            print("GenderException and LanguageException")
        elif gender != "female":
            print("GenderException")
        elif language != "english":
            print("LanguageException")

try:
    no = int(input("Enter the no of applicants"))

    for i in range(no):
        name = input("Enter name ")
        gender = input("Enter gender ")
        language = input("Enter langauge ")

        if gender != "female" or language != "english":
            raise ApplicantError(gender, language)
        
except ApplicantError:
    pass