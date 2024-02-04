from customtkinter import *
from test import  Reg
import sqlite3

class ChildWindow:
    def __init__(self, parent):
        self.root = CTkToplevel(parent)
        self.root.title('Авторизация')
        self.root.geometry("600x600")
        self.root.resizable(False, False)
        self.root.grab_set()
        self.root.focus_set()

        self.frame=CTkFrame(self.root)
        self.frame.grid(row=1, column=0, sticky="ew")
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)

        #self.frame.grid_columnconfigure(2,weight=1)
        self.label1=CTkLabel(self.frame,text="Окно Входа и регистрации")
        self.label1.grid(row=0, column=3, padx=10, pady=10, sticky="e")

        self.label = CTkLabel(self.frame, text="Логин:")
        self.label.grid(row=1, column=1, padx=10, pady=10,sticky="e")
        self.username_entry = CTkEntry(self.frame)
        self.username_entry.grid(row=1, column=2,columnspan=2 , padx=10, pady=10,sticky="nswe")


        self.password_label = CTkLabel(self.frame, text="Пароль:")
        self.password_label.grid(row=2, column=1, padx=10, pady=10,sticky="e")
        self.password_entry = CTkEntry(self.frame, show="*",width=300)
        self.password_entry.grid(row=2, column=2,columnspan=2, padx=10, pady=10,sticky="nswe")

        self.login_button = CTkButton(self.root, text="Войти", command=self.login)
        self.login_button.grid(row=3, column=0, padx=10, pady=10,sticky="e")
        self.registration_button = CTkButton(self.root, text="Регистрация", command=self.registration)
        self.registration_button.grid(row=3, column=0, padx=10, pady=10,sticky="w")


    def registration(self):

        Reg(self.root)

    def login(self):
        connection = sqlite3.connect('db/database.db')
        cursor = connection.cursor()

        # Выбираем и сортируем пользователей по возрасту по убыванию
        cursor.execute('''SELECT * FROM users ''')
        results = cursor.fetchall()

        print(results)

        connection.close()



        username = self.username_entry.get()
        password = self.password_entry.get()

        # Here you can add your authentication logic
        for row in results:
            if row[1] == username and row[2] == password:

                print("Найдена запись с нужными значениями в ячейках")
                self.root.destroy()
            else:

                print("Authentication failed")
