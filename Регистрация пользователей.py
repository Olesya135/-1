import sqlite3
from tkinter import *
from tkinter import messagebox

# Инициализация базы данных
def init_db():
    # Подключение к базе данных
    conn = sqlite3.connect('users.db') # Подключение к базе данных
    # Создание курсора для выполнения SQL-запросов
    cursor = conn.cursor()
    # Создание таблицы пользователей, если она не существует
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)''')
    # Сохранение изменений
    conn.commit()
    # Закрытие соединения с базой данных
    conn.close()
# Регистрация нового пользователя
def register(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    conn.commit()
    try:
        # Вставка нового пользователя
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        # Уведомление об успешной регистрации
        messagebox.showinfo("Успех", "Пользователь зарегистрирован!")
    # Обработка ошибки, если пользователь с таким логином уже 
    except sqlite3.IntegrityError:
        messagebox.showerror("Ошибка", "Пользователь с таким логином уже существует.")
    # Закрытие соединения
    conn.close()
# Аутентификация пользователя
def authenticater(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    # Проверка существования пользователя
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    # Получение данных пользователя
    user = cursor.fetchone()
    conn.close()
    # Возвращение True, если пользователь найден
    return user is not None

# Открытие окна регистрации
def open_registration():
    reg = Toplevel(root) # Создание нового окна
    reg.title("Регистрация")  # Заголовок окна
    reg.geometry("250x250") # Размер окна
    main_label = Label(reg, text='Регистрация', font=f, justify=CENTER, **h) # Заголовок формы регистрации
    main_label.pack()

    Label(reg, text="Логин:").pack(m) # Метка для логина
    reg_username = Entry(reg) # Поле ввода логина
    reg_username.pack(m)

    Label(reg, text="Пароль:").pack(m) # Метка для пароля
    reg_password = Entry(reg, show='*') # Поле ввода пароля
    reg_password.pack(m)

    # Кнопка регистрации
    Button(reg, text="Зарегистрироваться", command=lambda: register(reg_username.get(), reg_password.get())).pack(pady=10)
# Попытка входа в систему
def attempt_login():
    username = username_entry.get() # Получение логина
    password = password_entry.get() # Получение пароля
    # Проверка аутентификации
    if authenticater(username, password):
        messagebox.showinfo("Успех", "Вы успешно авторизованы!") # Уведомление об успехе
    else:
        messagebox.showerror("Ошибка", "Неверный логин или пароль.") # Уведомление об ошибке
# Основное окно приложения
root = Tk()
root.title("Авторизация")
root.geometry("300x300")
f = ('Arial', 15)
m = {'pady':5}
h = {'padx': 10, 'pady': 12}
labe = Label(root, text='Авторизация', font=f, justify=CENTER, **h) # Заголовок формы авторизации
labe.pack()
init_db  Инициализация базы данных

Label(root, text="Логин:").pack(m) # Метка для логина
username_entry = Entry(root) # Поле ввода
username_entry.pack(m)

Label(root, text="Пароль:").pack(m) # Метка для пароля
password_entry = Entry(root, show='*') # Поле ввода
password_entry.pack(m)

Button(root, text="Авторизоваться", command=attempt_login).pack(pady=10) # Кнопка для входа
Button(root, text="Открыть регистрацию", command=open_registration).pack(m) # Кнопка для открытия окна регистрации

# Запуск
root.mainloop()
