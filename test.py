import sqlite3
from customtkinter import *
class Reg:
    def __init__(self, parent):


        self.root = CTkToplevel(parent)
        self.root.title('{EQ}')
        self.root.geometry("600x600")
        self.root.resizable(False, False)
        self.root.grab_set()
        self.root.focus_set()

        self.frame=CTkFrame(self.root)
        self.frame.grid(row=1, column=0, sticky="ew")
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)

        self.label1=CTkLabel(self.frame,text="Окно Входа и регистрации")
        self.label1.grid(row=0, column=2, padx=10, pady=10, sticky="e")

        self.label = CTkLabel(self.frame, text="Логин:")
        self.label.grid(row=1, column=1, padx=10, pady=10,sticky="e")
        self.username_entry = CTkEntry(self.frame)
        self.username_entry.grid(row=1, column=2, padx=10, pady=10,sticky="nswe")


        self.password_label = CTkLabel(self.frame, text="Пароль:")
        self.password_label.grid(row=2, column=1, padx=10, pady=10,sticky="e")
        self.password_entry = CTkEntry(self.frame, show="*")
        self.password_entry.grid(row=2, column=2, padx=10, pady=10,sticky="nswe")

        self.password_label = CTkLabel(self.frame, text="Имя:")
        self.password_label.grid(row=3, column=1, padx=10, pady=10, sticky="e")
        self.name = CTkEntry(self.frame)
        self.name.grid(row=3, column=2, padx=10, pady=10, sticky="nswe")

        self.password_label = CTkLabel(self.frame, text="Фамилия:")
        self.password_label.grid(row=4, column=1, padx=10, pady=10, sticky="e")
        self.second_name = CTkEntry(self.frame)
        self.second_name.grid(row=4, column=2, padx=10, pady=10, sticky="nswe")

        self.password_label = CTkLabel(self.frame, text="Группа:")
        self.password_label.grid(row=5, column=1, padx=10, pady=10, sticky="e")
        self.gr = CTkEntry(self.frame)
        self.gr.grid(row=5, column=2, padx=10, pady=10, sticky="nswe")

        self.login_button = CTkButton(self.frame, text="Назад", command=self.login)
        self.login_button.grid(row=6, column=0, padx=10, pady=10,sticky="e")
        self.registration_button = CTkButton(self.frame, text="Регистрация", command=self.registration)
        self.registration_button.grid(row=6, column=3, padx=10, pady=10,sticky="w")

    def registration(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        name = self.name.get()
        second_name = self.second_name.get()
        gr = self.gr.get()
        data=[username,password,name,second_name,gr]
        connection = sqlite3.connect('db/database.db')
        cursor = connection.cursor()

        cursor.execute('''INSERT INTO users (login,password,name,second_name,class) VALUES(?,?,?,?,?) ''', data)
        # Выбираем и сортируем пользователей по возрасту по убыванию
        cursor.execute('''SELECT * FROM users ''')
        results = cursor.fetchall()
        connection.commit()
        connection.close()
        print(results)




    def login(self):
        columns_to_check = ['login', 'password']
        table_name = 'users'
        conn = sqlite3.connect('db/database.db')
        cursor = conn.cursor()

        # Находим дубликаты и удаляем их
        cursor.execute(f'''
                DELETE FROM {table_name} WHERE rowid NOT IN (
                    SELECT MIN(rowid) FROM {table_name} GROUP BY {', '.join(columns_to_check)}
                )
            ''')

        conn.commit()
        conn.close()
        self.root.destroy()
