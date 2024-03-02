from tkinter import *

def addition():
    try:
        number_1 = int(entry_1.get())
        number_2 = int(entry_2.get())

        addition_process = number_1 + number_2
        answer_label.config(text=addition_process)
        return addition_process
    except ValueError:
        answer_label.config(text="Please enter valid number")

def extraction():
    try:
        number_1 = int(entry_1.get())
        number_2 = int(entry_2.get())

        extraction_process = number_1 - number_2
        answer_label.config(text=extraction_process)
        return extraction_process
    except ValueError:
        answer_label.config(text="Please enter valid number")

def multiplication():
    try:
        number_1 = int(entry_1.get())
        number_2 = int(entry_2.get())

        multiplication_process = number_1 * number_2
        answer_label.config(text=multiplication_process)
        return multiplication_process
    except ValueError:
        answer_label.config(text="Please enter valid number")

def division():
    try:
        number_1 = int(entry_1.get())
        number_2 = int(entry_2.get())

        division_process = number_1 / number_2
        answer_label.config(text=division_process)
        return division_process
    except ValueError:
        answer_label.config(text="Please enter valid number")

window = Tk()
window.config(padx=75,pady=75)
window.title("Calculator")

label_1 = Label()
label_1.config(width=30,text="Enter the number 1")
label_1.pack()

entry_1 = Entry()
entry_1.config(width=30)
entry_1.pack()

label_2 = Label()
label_2.config(width=30,text="Enter the number 2")
label_2.pack()

entry_2 = Entry()
entry_2.config(width=30)
entry_2.pack()

button_1 = Button()
button_1.config(width=20,text="addition",command=addition)
button_1.pack()

button_2 = Button()
button_2.config(width=20,text="extraction",command=extraction)
button_2.pack()

button_3 = Button()
button_3.config(width=20,text="multiplication",command=multiplication)
button_3.pack()

button_4 = Button()
button_4.config(width=20,text="division",command=division)
button_4.pack()

answer_label = Label()
answer_label.pack()

window.mainloop()