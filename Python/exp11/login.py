from tkinter import *

def login_command(event=None):
    l1.config(text="Login successful for "+name_text.get())

window = Tk()
window.wm_title("Login Portal")
name_text = StringVar()
pw_text = StringVar()

# Labels

l1=Label(window, text="Hello!", font=("Helvetica", 20), anchor=W, justify=LEFT, bg="#51dacf")
l1.grid(row=0,column=0)

l2=Label(window, text="Enter name here", font=("Helvetica", 12), anchor=W, justify=LEFT)
l2.grid(row=2,column=0)

l3=Label(window, text="Enter password here", font=("Helvetica", 12), anchor=W, justify=LEFT)
l3.grid(row=4,column=0)

# Entry Fields

e1=Entry(window, textvariable=name_text, highlightthickness=1, highlightbackground="#111")
e1.grid(row=3,column=0)

e2=Entry(window, textvariable=pw_text, highlightthickness=1, show="*", highlightbackground="#111")
e2.grid(row=5,column=0)

# Buttons 

b1=Button(window, text="Login", bg="#51dacf", highlightthickness=2,
    highlightbackground="#111", width=12, command=login_command)
b1.grid(row=6, column=0)

window.bind('<Return>',login_command)
window.resizable(True, False)
window.grid_columnconfigure(0, weight=1)

window.mainloop()