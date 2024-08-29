import tkinter as tk

# Function to update the input field
def update_input(value):
    current_input = input_var.get()
    input_var.set(current_input + value)

# Function to calculate the result
def calculate():
    try:
        result = str(eval(input_var.get()))
        input_var.set(result)
    except:
        input_var.set("Error")

# Function to clear the input field
def clear():
    input_var.set("")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create a StringVar to store the input
input_var = tk.StringVar()

# Create the input field
input_field = tk.Entry(root, textvariable=input_var, font=("Arial", 18), bd=8, insertwidth=4, width=14, borderwidth=4)
input_field.grid(row=0, column=0, columnspan=4)

# Define the button layout
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

# Create buttons and add them to the grid
row = 1
col = 0
for button in buttons:
    if button == "=":
        btn = tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 18),
                        command=calculate)
    else:
        btn = tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 18),
                        command=lambda b=button: update_input(b))
    btn.grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Add the clear button
clear_button = tk.Button(root, text="Clear", padx=130, pady=10, font=("Arial", 10), command=clear)
clear_button.grid(row=row, column=0, columnspan=4)

# Run the main loop
root.mainloop()
