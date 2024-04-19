
# Here's a tkinter GUI app with ttkbootstrap import Style that calculates the total number of seconds based on entered hours, minutes, and seconds:This code creates a window with labels and entry fields for hours, minutes, and seconds. It also includes a button that triggers the calculate_seconds function when clicked. This function retrieves the values from the entry fields, calculates the total seconds, and displays the result in a dedicated label. #

from ttkbootstrap import Style
from tkinter import Tk, Label, Entry, Button

def calculate_seconds():
    try:
        hours = int(hours_entry.get())
        minutes = int(minutes_entry.get())
        seconds = int(seconds_entry.get())
        total_seconds = hours * 3600 + minutes * 60 + seconds
        result_label.configure(text=f"Total Seconds: {total_seconds}s")
    except ValueError:
        result_label.configure(text="Invalid Input: Please enter numbers only.")

# Create a style object with a specific theme
style = Style(theme='superhero')

# Apply the style to the root Tk window
root = style.master
root.title("Calculates total number of seconds based on hours")
root.geometry("600x400")

hours_label = Label(root, text="Hours:")
hours_label.pack(pady=5)

hours_entry = Entry(root)
hours_entry.pack(pady=5)

minutes_label = Label(root, text="Minutes:")
minutes_label.pack(pady=5)

minutes_entry = Entry(root)
minutes_entry.pack(pady=5)

seconds_label = Label(root, text="Seconds:")
seconds_label.pack(pady=5)

seconds_entry = Entry(root)
seconds_entry.pack(pady=5)

calculate_button = Button(root, text="Calculate", command=calculate_seconds)
calculate_button.pack(pady=10)

result_label = Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
