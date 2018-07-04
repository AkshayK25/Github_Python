import tkinter as tk
from tkinter import *

#  Question 1::

window = tk.Tk()
window.geometry("300x200")
window.title("Welcome to Graphical user interface!!!")
var = StringVar()
label = Label(window, textvariable=var, relief=RAISED)
var.set('Hello world !!')
label.pack()
button = tk.Button(window, text='Exit', width='25', activeforeground='RED', command=window.destroy)
button.pack()
window.mainloop()

#  Question number 2::


def write_phrase():
    print("Tkinter is easy to use!")


aksk = tk.Tk()
aksk.geometry("300x200")
aksk.title("Welcome to Graphical user interface!!!")
frame = tk.Frame(aksk)
frame.pack()

button = tk.Button(frame, text="QUIT", fg="red", width='10', command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame, text="Hello", width='15', command=write_phrase)
slogan.pack(side=tk.LEFT)

aksk.mainloop()

#  Question 3 ::

root = Tk(className="<<<button_click_label GUI>>>")
root.geometry("300x200")

message = StringVar()
message.set('hi')

l1 = Label(root, text="HYE !!")


def press():
    l1.config(text="HELLO!! WELCOME TO ACADVIEw")


b1 = Button(root, text="click_here", command=press).pack(side=tk.RIGHT)
b2 = Button(root, text="EXIT", command=root.destroy).pack(side=tk.LEFT)
l1.pack()
root.mainloop()

# Question 4 ::


def print_text():
    global e
    string = e.get()
    print(string)


book = Tk()
book.geometry('300x200')
book.title('Name')

e = Entry(book)
e.pack()
e.focus_set()

b = Button(book, text='Submit', command=print_text)
b.pack(side='top')
bt = Button(book, text='exit', command=book.destroy).pack(side='top')
book.mainloop()
