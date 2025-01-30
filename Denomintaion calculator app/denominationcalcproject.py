import tkinter as tk
from tkinter import messagebox

def check_password_strength():
    password = entry.get()
    length = len(password)

    if length < 6:
        strength = "Weak"
    elif 6 <= length < 10:
        strength = "Moderate"
    else:
        strength = "Strong"

    messagebox.showinfo("Password Strength", f"Your password is: {strength}")

root = tk.Tk()
root.title("Password Strength Checker")

label = tk.Label(root, text="Enter your password:")
label.pack(pady=10)

entry = tk.Entry(root, show="*")
entry.pack(pady=10)

button = tk.Button(root, text="Check Strength", command=check_password_strength)
button.pack(pady=10)

root.mainloop()
