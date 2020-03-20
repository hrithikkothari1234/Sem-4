#Q1

'''
    tkinter is python's standerd GUI package.
    The layout managers used to place components in GUI are also called Geometry Managers. These are used to place and align components.
    There are 3 types of Geometry Managers in tkinter:
    1)pack:
        This geometry manager organizes widgets in blocks before placing them in the parent widget.
        Syntax:
            widget.pack( pack_options )
            expand − When set to true, widget expands to fill any space not otherwise used in widget's parent.
            fill − Determines whether widget fills any extra space allocated to it by the packer, or keeps its own minimal
             dimensions: NONE (default), X (fill only horizontally), Y (fill only vertically), or BOTH (fill both horizontally 
             and vertically).
            side − Determines which side of the parent widget packs against: TOP (default), BOTTOM, LEFT, or RIGHT.
        e.g.:
            redbutton = Button(frame, text="Red", fg="red")
            redbutton.pack( side = LEFT)
    2)Grid:
        This geometry manager organizes widgets in a table-like structure in the parent widget.
        Syntax:
            widget.grid( grid_options )
            column − The column to put widget in; default 0 (leftmost column).
            columnspan − How many columns widgetoccupies; default 1.
            ipadx, ipady − How many pixels to pad widget, horizontally and vertically, inside widget's borders.
            padx, pady − How many pixels to pad widget, horizontally and vertically, outside v's borders.
            row − The row to put widget in; default the first row that is still empty.
            rowspan − How many rowswidget occupies; default 1.
            sticky − What to do if the cell is larger than widget. By default, with sticky='', widget is centered in its cell. sticky may be the string concatenation of zero or more of N, E, S, W, NE, NW, SE, and SW, compass directions indicating the sides and corners of the cell to which widget sticks.
        e.g.:
            Tkinter.Label(root, text='R%s/C%s'%(r,c),borderwidth=1 ).grid(row=r,column=c)
    3)place:
        This geometry manager organizes widgets by placing them in a specific position in the parent widget
        Syntax:
            widget.place( place_options )
            anchor − The exact spot of widget other options refer to: may be N, E, S, W, NE, NW, SE, or SW, compass directions indicating the corners and sides of widget; default is NW (the upper left corner of widget)
            bordermode − INSIDE (the default) to indicate that other options refer to the parent's inside (ignoring the parent's border); OUTSIDE otherwise.
            height, width − Height and width in pixels.
            relheight, relwidth − Height and width as a float between 0.0 and 1.0, as a fraction of the height and width of the parent widget.
            relx, rely − Horizontal and vertical offset as a float between 0.0 and 1.0, as a fraction of the height and width of the parent widget.
            x, y − Horizontal and vertical offset in pixels.
        e.g.:
            B = Tkinter.Button(top, text ="Hello", command = helloCallBack)
            B.place(bordermode=OUTSIDE, height=100, width=100)
'''
#Q2 

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

#Q3

import MySQLdb
from numpy.random import randint 

try:
    con=MySQLdb.connect('localhost','root','agent viper','socialapp')

    c=con.cursor()
    sql = "CREATE TABLE IF NOT EXISTS FIFA (scores int)"
    c.execute(sql)
    for i in range(1,100000):
        r=randint(low=10,high=30)
        c.execute('INSERT INTO FIFA VALUES(%s)',(r))

    con.close()

except:
    print("Error connecting db")


#--- 6.4126 seconds --- to save 100000 records in Database

from numpy.random import randint
f=open("events.txt","w+")
for i in range(1,100000):
    r=str(randint(low=10,high=30))
    f.write(r)

f.close()

#--- 1.0710008144378662 seconds --- to save 100000 records in text file

#Q4
# sender.py

import socket

s = socket.socket()
host = socket.gethostname() 

s.bind((host, 60000)) 
s.listen(5)

print('Server listening....')

while True:
    conn, addr = s.accept()
    print ('Got connection from', addr)

    data = conn.recv(1024)
    print('Server received', repr(data))

    filename='events.txt'
    f = open(filename,'rb')
    l = f.read(1024)

    while (l):
       conn.send(l)
       print('Sent ',repr(l))
       l = f.read(1024)

    f.close()
    print('File sent')
    conn.send(b'Thank you for connecting')
    conn.close()


#receiver.py

import socket

s = socket.socket()
host = socket.gethostname()

s.connect((host, 60000))
s.send(b'Hello server!')

with open('Received.txt', 'wb') as f:
    print('file opened')

    while True:

        print('receiving data...')
        data = s.recv(1024)
        print((data))
        f.write(data)

        if not data:
            break

f.close()
print('Successfully got the file')
s.close()
