import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = int(length_entry.get())
    include_special_chars = special_var.get()

    chars = string.ascii_letters + string.digits
    if include_special_chars:
        chars += string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    password_label.config(text=password)

def main():
    global length_entry, special_var, password_label

    root = tk.Tk()
    root.title("패스워드 생성기")
    root.geometry("300x200")

    length_label = tk.Label(root, text="패스워드 길이:")
    length_label.pack(pady=5)

    length_entry = tk.Entry(root)
    length_entry.pack(pady=5)

    special_chars_label = tk.Label(root, text="특수문자 포함:")
    special_chars_label.pack(pady=5)

    special_var = tk.BooleanVar()
    special_checkbox = tk.Checkbutton(root, variable=special_var)
    special_checkbox.pack(pady=5)

    generate_button = tk.Button(root, text="패스워드 생성", command=generate_password)
    generate_button.pack(pady=10)

    password_label = tk.Label(root, text="")
    password_label.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
