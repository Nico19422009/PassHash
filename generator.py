import hashlib
import random
import string
import tkinter as tk
from tkinter import messagebox
import locale

def generate_password(length, complexity):
    chars = string.ascii_lowercase
    if complexity >= 2:
        chars += string.ascii_uppercase
    if complexity >= 3:
        chars += string.digits
    if complexity >= 4:
        chars += string.punctuation

    return "".join(random.choice(chars) for _ in range(length))

def hash_password(password, hash_type):
    if hash_type == "MD5":
        return hashlib.md5(password.encode()).hexdigest()
    elif hash_type == "SHA-256":
        return hashlib.sha256(password.encode()).hexdigest()
    elif hash_type == "SHA-512":
        return hashlib.sha512(password.encode()).hexdigest()
    else:
        return "Unsupported hash type!"

def save_hash_to_file(hash_value, mode):
    filename = "Shash1.txt" if mode == "selfmade" else "Chash.txt"
    with open(filename, "a") as file:
        file.write(hash_value + "\n")
    messagebox.showinfo("Info", f"Hash gespeichert in {filename} ✅")

def generate_and_hash():
    mode = mode_var.get()
    if mode == "selfmade":
        password = password_entry.get()
    else:
        length = int(length_entry.get())
        complexity = int(complexity_var.get())
        password = generate_password(length, complexity)

    hash_type = hash_type_var.get()
    hashed_pw = hash_password(password, hash_type)
    hashed_pw_label.config(text=f"Gehashtes Passwort ({hash_type}): {hashed_pw}")
    save_hash_to_file(hashed_pw, mode)

def toggle_fields():
    mode = mode_var.get()
    if mode == "selfmade":
        password_entry.grid()
        length_label.grid_remove()
        length_entry.grid_remove()
        complexity_label.grid_remove()
        complexity_spinbox.grid_remove()
    else:
        password_entry.grid_remove()
        length_label.grid()
        length_entry.grid()
        complexity_label.grid()
        complexity_spinbox.grid()

# GUI setup
root = tk.Tk()
root.title("Secure Password Hasher v1.0")
# Determine system language
system_lang = locale.getdefaultlocale()[0]

# Define translations
translations = {
    "en": {
        "mode_label": "Select Mode:",
        "selfmade": "SelfMade",
        "custom": "Custom",
        "password_label": "Enter your password:",
        "length_label": "Password length:",
        "complexity_label": "Complexity (1=Simple, 4=Max):",
        "hash_label": "Select Hash Algorithm:",
        "generate_button": "Generate and Hash",
        "info_message": "Hash saved in",
        "unsupported_hash": "Unsupported hash type!"
    },
    "de": {
        "mode_label": "Wähle Modus:",
        "selfmade": "SelfMade",
        "custom": "Custom",
        "password_label": "Gib dein Passwort ein:",
        "length_label": "Länge des Passworts:",
        "complexity_label": "Komplexität (1=Einfach, 4=Max):",
        "hash_label": "Wähle Hash-Algorithmus:",
        "generate_button": "Generieren und Hashen",
        "info_message": "Hash gespeichert in",
        "unsupported_hash": "Unsupported hash type!"
    }
}

# Select translation based on system language
lang = translations.get(system_lang[:2], translations["en"])

root.geometry("500x300")
root.configure(bg="black")

style = {
    "bg": "black",
    "fg": "white",
    "font": ("Helvetica", 12)
}

tk.Label(root, text=lang["mode_label"], **style).grid(row=0, column=0, sticky="w")
mode_var = tk.StringVar(value="selfmade")
tk.Radiobutton(root, text=lang["selfmade"], variable=mode_var, value="selfmade", command=toggle_fields, **style).grid(row=0, column=1, sticky="w")
tk.Radiobutton(root, text=lang["custom"], variable=mode_var, value="custom", command=toggle_fields, **style).grid(row=0, column=2, sticky="w")

tk.Label(root, text=lang["password_label"], **style).grid(row=1, column=0, sticky="w")
password_entry = tk.Entry(root, show="*", **style)
password_entry.grid(row=1, column=1, columnspan=2, sticky="w")

length_label = tk.Label(root, text=lang["length_label"], **style)
length_label.grid(row=2, column=0, sticky="w")
length_entry = tk.Entry(root, **style)
length_entry.grid(row=2, column=1, columnspan=2, sticky="w")

complexity_label = tk.Label(root, text=lang["complexity_label"], **style)
complexity_label.grid(row=3, column=0, sticky="w")
complexity_var = tk.IntVar(value=1)
complexity_spinbox = tk.Spinbox(root, from_=1, to=4, textvariable=complexity_var, **style)
complexity_spinbox.grid(row=3, column=1, columnspan=2, sticky="w")

tk.Label(root, text=lang["hash_label"], **style).grid(row=4, column=0, sticky="w")
hash_type_var = tk.StringVar(value="MD5")
tk.OptionMenu(root, hash_type_var, "MD5", "SHA-256", "SHA-512").grid(row=4, column=1, columnspan=2, sticky="w")

tk.Button(root, text=lang["generate_button"], command=generate_and_hash, **style).grid(row=5, column=0, columnspan=3)

hashed_pw_label = tk.Label(root, text="", **style)
hashed_pw_label.grid(row=6, column=0, columnspan=3)

toggle_fields()  # Initialize the fields based on the default mode

root.mainloop()
