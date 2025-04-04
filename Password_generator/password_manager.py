import random
import tkinter as tk
from tkinter import simpledialog
import json
import os

# Path to the data file
DATA_FILE = 'passwords.json'

# Dictionary for password symbols
pass_symbols = {
    0/68: "a", 1/68: "A", 2/68: "b", 3/68: "B", 4/68: "c", 5/68: "C", 6/68: "D", 7/68: "d",
    8/68: "e", 9/68: "E", 10/68: "f", 11/68: "F", 12/68: "G", 13/68: "g", 14/68: "h", 15/68: "H",
    16/68: "I", 17/68: "i", 18/68: "j", 19/68: "J", 20/68: "K", 21/68: "k", 22/68: "L", 23/68: "l",
    24/68: "M", 25/68: "m", 26/68: "N", 27/68: "n", 28/68: "o", 29/68: "O", 30/68: "p", 31/68: "P",
    32/68: "Q", 33/68: "q", 34/68: "r", 35/68: "R", 36/68: "S", 37/68: "s", 38/68: "T", 39/68: "t",
    40/68: "u", 41/68: "U", 42/68: "v", 43/68: "V", 44/68: "w", 45/68: "W", 46/68: "X", 47/68: "x",
    48/68: "Y", 49/68: "y", 50/68: "z", 51/68: "Z", 52/68: "1", 53/68: "2", 54/68: "3", 55/68: "4",
    56/68: "5", 57/68: "6", 58/68: "7", 59/68: "8", 60/68: "9", 61/68: "!", 62/68: "@", 63/68: "#",
    64/68: "$", 65/68: "%", 66/68: "^", 67/68: "&", 68/68: "?"
}

# Load passwords from file
def load_passwords():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return {}

# Save passwords to file
def save_passwords():
    with open(DATA_FILE, 'w') as file:
        json.dump(passwords_storage, file, indent=4)

# Dictionary to store passwords with names
passwords_storage = load_passwords()

def generate_password():
    length = simpledialog.askinteger("Password Length", "Enter password length:", parent=root, minvalue=1, maxvalue=20)
    if not length:
        return

    result = []
    for _ in range(length):
        rand_value = random.uniform(0, 1)
        closest_key = min(pass_symbols.keys(), key=lambda k: abs(k - rand_value))
        result.append(pass_symbols[closest_key])
    
    password_str = ''.join(result)
    print(f'Generated password: {password_str}')
    
    # Store the generated password
    name = simpledialog.askstring("Password Name", "Enter a name for this password:", parent=root)
    if name:
        passwords_storage[name] = password_str
        save_passwords()
        update_password_list()

def update_password_list():
    # Clear the existing list
    for widget in password_list_frame.winfo_children():
        widget.destroy()
    
    for name, password in passwords_storage.items():
        row = tk.Frame(password_list_frame)
        row.pack(fill='x', pady=5)
        
        tk.Label(row, text=f"{name}:", anchor="w", width=25).pack(side='left', padx=5)
        tk.Label(row, text=password, anchor="w", width=25, bg='lightgray').pack(side='left', fill='x', padx=5)
        
        copy_button = tk.Button(row, text="Copy", command=lambda p=password: copy_to_clipboard(p))
        copy_button.pack(side='right', padx=5)

def copy_to_clipboard(password):
    root.clipboard_clear()
    root.clipboard_append(password)
    root.update()  # Ensure the clipboard is updated
    print("Password copied to clipboard.")

root = tk.Tk()
root.title("Password Manager")
root.geometry("400x400")  # Set a default window size
root.iconphoto(True, tk.PhotoImage(file='padlock.png'))

# Create and pack the buttons
generate_button = tk.Button(root, text="Generate Password", command=generate_password, width=20)
generate_button.pack(padx=20, pady=10)

password_list_frame = tk.Frame(root)
password_list_frame.pack(padx=20, pady=10, fill='both', expand=True)

update_password_list()  # Load existing passwords

root.mainloop()
