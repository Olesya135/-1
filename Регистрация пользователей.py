import sqlite3
from tkinter import *
from tkinter import messagebox

def init_db():
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    conn.commit()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)''')
    conn.close()
def register(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    conn.commit()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        messagebox.showinfo("Успех", "Пользователь зарегистрирован!")
    except sqlite3.IntegrityError:
        messagebox.showerror("Ошибка", "Пользователь с таким логином уже существует.")
    conn.close()
def authenticater(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()
    conn.close()
    return user is not None
def open_registration():
    reg = Toplevel(root)
    conn = sqlite3.connect('users.db')
    conn.commit()
    reg.title("Регистрация")
    reg.geometry("250x250")
    main_label = Label(reg, text='Регистрация', font=f, justify=CENTER, **h)
    main_label.pack()

    Label(reg, text="Логин:").pack(m)
    reg_username = Entry(reg)
    reg_username.pack(m)

    Label(reg, text="Пароль:").pack(m)
    reg_password = Entry(reg, show='*')
    reg_password.pack(m)

    Button(reg, text="Зарегистрироваться",
           command=lambda: register(reg_username.get(), reg_password.get())).pack(pady=10)
def attempt_login():
    username = username_entry.get()
    password = password_entry.get()
    if authenticater(username, password):
        messagebox.showinfo("Успех", "Вы успешно авторизованы!")
    else:
        messagebox.showerror("Ошибка", "Неверный логин или пароль.")
root = Tk()
root.title("Авторизация")
root.geometry("300x300")
f = ('Arial', 15)
m = {'pady':5}
h = {'padx': 10, 'pady': 12}
labe = Label(root, text='Авторизация', font=f, justify=CENTER, **h)
labe.pack()
init_db()

Label(root, text="Логин:").pack(m)
username_entry = Entry(root)
username_entry.pack(m)

Label(root, text="Пароль:").pack(m)
password_entry = Entry(root, show='*')
password_entry.pack(m)

Button(root, text="Авторизоваться", command=attempt_login).pack(pady=10)
Button(root, text="Открыть регистрацию", command=open_registration).pack(m)

root.mainloop()