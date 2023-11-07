import sys
from tkinter import *

def calculate_area():
    width = float(width_entry.get())
    height = float(height_entry.get())
    total = width * height
    result_label.configure(text=f'Area of rectangle is = {total:.2f}')

root = Tk()
root.title("Area Calculator")
root.geometry('350x200')

width_label = Label(root, text="Enter width:")
width_label.grid(row=0, column=0)

width_entry = Entry(root)
width_entry.grid(row=0, column=1)

height_label = Label(root, text="Enter height:")
height_label.grid(row=1, column=0)

height_entry = Entry(root)
height_entry.grid(row=1, column=1)

calculate_button = Button(root, text="Calculate Area", command=calculate_area)
calculate_button.grid(row=2, column=0, columnspan=2)

result_label = Label(root, text="")
result_label.grid(row=3, column=0, columnspan=2)

root.mainloop()