import random
from tkinter import *
from tkinter.messagebox import showinfo

# Функция для генерации пароля
def generate():
    characters = [] # Список для хранения возможных символов пароля
    # Добавление строчных букв
    if include_lowercase.get():
        characters += [chr(i) for i in range(ord('a'), ord('z') + 1)]
    # Добавление цифр
    if include_numbers.get():
        characters += [str(i) for i in range(10)]
    # Добавление специальных символов
    if include_special.get():
        characters += ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
    # Уведомление об ошибке
    if not characters:
        showinfo("Ошибка", "Пожалуйста, выберите хотя бы один вариант!")
        return
    # Генерация пароля из выбранных символов
    password = ''.join(random.choice(characters) for i in range(passlen.get()))
    passstr.set(password) # Установка сгенерированного пароля в текстовое поле
# Основное окно приложения
root = Tk()
root.geometry("400x400")
root.title("Генератор паролей")

# Переменные для хранения значений
passstr = StringVar() # Переменная для хранения сгенерированного пароля
passlen = IntVar() # длина
include_lowercase = BooleanVar(value=True)
include_numbers = BooleanVar(value=True)
include_special = BooleanVar(value=True)

Label(root, text="Генератор паролей", font="calibri 20 bold").pack(pady=10) # Заголовок

Label(root, text="Длина пароля:").pack(pady=3)  # Метка для длины пароля
Entry(root, textvariable=passlen, width=5).pack(pady=3) # Поле ввода длины пароля

Checkbutton(root, text="Включить нижний регистр (a-z)", variable=include_lowercase).pack(anchor=W)# Чекбокс
Checkbutton(root, text="Включить цифры (0-9)", variable=include_numbers).pack(anchor=W)# Чекбокс
Checkbutton(root, text="Включить спецсимволы (!@#$%)", variable=include_special).pack(anchor=W)# Чекбокс

Button(root, text="Сгенерировать пароль", command=generate).pack(pady=7) # Кнопка для генерации пароля
Entry(root, textvariable=passstr, width=30).pack(pady=3) # Поле для отображения сгенерированного пароля
 # Запуск
root.mainloop()
