import random
from tkinter import *
from tkinter.messagebox import showinfo


def generate():
    characters = []
    if include_lowercase.get():
        characters += [chr(i) for i in range(ord('a'), ord('z') + 1)]
    if include_numbers.get():
        characters += [str(i) for i in range(10)]
    if include_special.get():
        characters += ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
    if not characters:
        showinfo("Ошибка", "Пожалуйста, выберите хотя бы один вариант!")
        return
    password = ''.join(random.choice(characters) for i in range(passlen.get()))
    passstr.set(password)

root = Tk()
root.geometry("400x400")
root.title("Генератор паролей")

passstr = StringVar()
passlen = IntVar()

include_lowercase = BooleanVar(value=True)
include_numbers = BooleanVar(value=True)
include_special = BooleanVar(value=True)

Label(root, text="Генератор паролей", font="calibri 20 bold").pack(pady=10)

Label(root, text="Длина пароля:").pack(pady=3)
Entry(root, textvariable=passlen, width=5).pack(pady=3)

Checkbutton(root, text="Включить нижний регистр (a-z)", variable=include_lowercase).pack(anchor=W)
Checkbutton(root, text="Включить цифры (0-9)", variable=include_numbers).pack(anchor=W)
Checkbutton(root, text="Включить спецсимволы (!@#$%)", variable=include_special).pack(anchor=W)

Button(root, text="Сгенерировать пароль", command=generate).pack(pady=7)
Entry(root, textvariable=passstr, width=30).pack(pady=3)

root.mainloop()