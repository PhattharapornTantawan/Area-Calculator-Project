import sys
from tkinter import *
from tkinter import simpledialog, messagebox

# Function to calculate the area
def calculate_area():
    try:
        width = float(width_entry.get())
        height = float(height_entry.get())
        
        # Calculate the area
        total = width * height
        
        # Display the result in a message box
        result = f'Area of the rectangle is {total:.2f}'
        messagebox.showinfo('Result', result)
        
        # Check if the user wants to continue
        answer = simpledialog.askstring('Continue', 'Do you want to try again? (y/n): ')
        
        if answer == 'n':
            messagebox.showinfo('Thanks', 'Thank you for playing!')
            root.destroy()
            sys.exit()
    except ValueError:
        # Handle invalid input
        result_label.configure(text='Invalid input. Please enter valid numbers.')

# Function for the "OK" button
def ok():
    # Implement the desired behavior when the "OK" button is clicked
    result_label.configure(text='')

# Function for the "Cancel" button
def cancel():
    # Implement the desired behavior when the "Cancel" button is clicked
    width_entry.delete(0, END)
    height_entry.delete(0, END)

# Create the main application window
root = Tk()
root.title("Area Calculator")
root.geometry('350x200')

# Create labels and entry fields for width and height
width_label = Label(root, text="Width:")
width_label.pack()
width_entry = Entry(root)
width_entry.pack()

height_label = Label(root, text="Height:")
height_label.pack()
height_entry = Entry(root)
height_entry.pack()

# Create "OK" and "Cancel" buttons
calculate_button = Button(root, text="OK", command=calculate_area)
calculate_button.pack()

cancel_button = Button(root, text="Cancel", command=cancel)
cancel_button.pack()

# Create a label to display the result
result_label = Label(root, text="")
result_label.pack()

# Start the main event loop
root.mainloop()
