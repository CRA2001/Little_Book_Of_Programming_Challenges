'''
Create a two-dimensional array of integers 10 by 10.
Fill the array with random numbers in the range 0 to 15
Display the array on the screen showing the numbers
Display the array on the screen as spaces whose BackColor property 
has been set to the number in this position of the array. 
'''
import random

import tkinter as tk

def generate_random_array(rows, cols):
    return [[random.randint(0, 15) for _ in range(cols)] for _ in range(rows)]

def display_array_on_screen(array):
    for i, row in enumerate(array):
        for j, num in enumerate(row):
            label = tk.Label(root, text=str(num), width=2, height=1, relief="solid", borderwidth=1)
            label.grid(row=i, column=j, padx=2, pady=2, sticky="nsew")
            label.config(bg=get_color(num))

def get_color(number):
    # You can define your color scheme based on the number
    # For simplicity, I'll use a basic color for demonstration
    colors = ["white", "lightblue", "lightgreen", "lightyellow", "lightcoral"]
    return colors[number % len(colors)]

# Create a Tkinter window
root = tk.Tk()
root.title("Array Display")

# Generate a random 10x10 array
array_10x10 = generate_random_array(10, 10)

# Display the array on the screen with different background colors
display_array_on_screen(array_10x10)

# Run the Tkinter main loop
root.mainloop()