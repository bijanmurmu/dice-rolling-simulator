import random
import tkinter as tk
from tkinter import messagebox

def roll_dice():
    """Handles dice rolling based on user input from the GUI."""
    user_input = entry.get().strip().lower()

    # Validate input format like "1d6" or "2d20"
    if 'd' in user_input and user_input.replace('d', '').isdigit():
        try:
            count, sides = map(int, user_input.split('d'))
            if count > 0 and sides > 0:
                rolls = [random.randint(1, sides) for _ in range(count)]
                result_text = f"You rolled: {rolls}\nTotal: {sum(rolls)}"
                result_label.config(text=result_text, fg="blue")
            else:
                raise ValueError("Dice count and sides must be positive numbers.")
        except ValueError:
            messagebox.showerror("Error", "Invalid format. Use numbers like '2d6' or '1d20'.")
    else:
        messagebox.showerror("Error", "Invalid input. Use formats like '1d6' or '2d20'.")

def bind_enter_key(event):
    """Bind Enter key to roll_dice."""
    roll_dice()

# Create the main application window
app = tk.Tk()
app.title("Dice Rolling Simulator")
app.geometry("400x300")

# Heading
heading_label = tk.Label(app, text="Dice Rolling Simulator", font=("Arial", 18))
heading_label.pack(pady=10)

# Input instructions
instructions_label = tk.Label(app, text="Enter dice in the format 'NdS':\nN = number of dice, S = sides (e.g., '1d6', '2d20')", font=("Arial", 12))
instructions_label.pack(pady=5)

# Input field
entry = tk.Entry(app, font=("Arial", 14), width=20)
entry.pack(pady=5)

# Bind Enter key to the entry widget
entry.bind("<Return>", bind_enter_key)

# Roll button
roll_button = tk.Button(app, text="Roll Dice", font=("Arial", 14), command=roll_dice)
roll_button.pack(pady=10)

# Result display
result_label = tk.Label(app, text="", font=("Arial", 14), fg="blue")
result_label.pack(pady=10)

# Start the application
app.mainloop()