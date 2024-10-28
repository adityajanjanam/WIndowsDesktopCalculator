import tkinter as tk

# Function to handle button click
def on_click(button_value):
    if button_value == "C":
        entry_var.set("")
    elif button_value == "=":
        try:
            result = str(eval(entry_var.get()))
            entry_var.set(result)
        except:
            entry_var.set("Error")
    else:
        current_text = entry_var.get()
        entry_var.set(current_text + button_value)

# Create main window
root = tk.Tk()
root.title("Simple Calculator")

# Create a variable to hold the entry text
entry_var = tk.StringVar()

# Create an entry widget to display the current equation
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 20), bd=10, insertwidth=2, width=14, borderwidth=4)
entry.grid(row=0, column=0, columnspan=4)

# Calculator buttons
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

# Add buttons to the window
for (text, row, col) in buttons:
    button = tk.Button(root, text=text, padx=20, pady=20, font=("Arial", 20), command=lambda t=text: on_click(t))
    button.grid(row=row, column=col)

# Start the main event loop
root.mainloop()
