import tkinter as tk
from tkinter import messagebox
import secrets
import string

def generate_password(length=16):
    """Generate a strong password with mixed case, digits, and symbols."""
    chars = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(secrets.choice(chars) for _ in range(length))
        # Check for at least one of each character type
        if (any(c.islower() for c in password) and
            any(c.isupper() for c in password) and
            any(c.isdigit() for c in password) and
            any(c in string.punctuation for c in password)):
            return password

def on_generate():
    """Handle password generation button click."""
    try:
        length = max(8, int(length_entry.get()))  # Ensure minimum length of 8
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")
        return
    
    password = generate_password(length)
    result_entry.delete(0, tk.END)
    result_entry.insert(0, password)
    
    try:
        import pyperclip
        pyperclip.copy(password)
        messagebox.showinfo("Success", "Password copied to clipboard!")
    except ImportError:
        pass  # Silently continue if pyperclip not available

# Set up the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x180")
root.resizable(False, False)

# Create and pack widgets
tk.Label(root, text="Password Length (min 8):").pack()
length_entry = tk.Entry(root)
length_entry.insert(0, "16")
length_entry.pack()

tk.Button(root, text="Generate Password", command=on_generate).pack(pady=10)

tk.Label(root, text="Generated Password:").pack()
result_entry = tk.Entry(root, width=40, font=('Courier', 10))
result_entry.pack()

tk.Label(root, text="(Auto copied to clipboard if possible)").pack()

root.mainloop()