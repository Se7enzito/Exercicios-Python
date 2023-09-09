import tkinter as tk

# Create a Tkinter window
window = tk.Tk()

# Create a Label
label = tk.Label(window, text="Enter a number:")
label.pack()

# Create an Entry widget for numerical input
entry = tk.Entry(window, validate="key")
entry.pack()

# Function to validate input
def validate_input(P):
    if P.isdigit() or P == "":
        return True
    else:
        return False

# Apply the input validation function to the Entry widget
validate_func = window.register(validate_input)
entry.config(validate="key", validatecommand=(validate_func, "%P"))

# Start the Tkinter main loop
window.mainloop()