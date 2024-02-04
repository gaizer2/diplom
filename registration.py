import sqlite3
import time
from crypto import CRYPTO

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,font


class REGISTRATION:
    def __init__(self):



        def relative_to_assets(path: str) -> Path:
            OUTPUT_PATH = Path(__file__).parent
            ASSETS_PATH = OUTPUT_PATH / Path(r"assets_reg\frame0")

            return ASSETS_PATH / Path(path)


        self.window2 = Tk()

        self.window2.geometry("1314x700")
        self.window2.configure(bg = "#FFFFFF")

        custom_font1 = font.Font(family='Arial', size='30')
        if 1==1:
            canvas = Canvas(
                self.window2,
                bg = "#FFFFFF",
                height = 700,
                width = 1314,
                bd = 0,
                highlightthickness = 0,
                relief = "ridge"
            )

            canvas.place(x = 0, y = 0)
            image_image_1 = PhotoImage(
                file=relative_to_assets("image_1.png"))
            image_1 = canvas.create_image(
                657.0,
                350.0,
                image=image_image_1
            )

            image_image_2 = PhotoImage(
                file=relative_to_assets("image_2.png"))
            image_2 = canvas.create_image(
                657.0,
                341.0,
                image=image_image_2
            )

            entry_image_1 = PhotoImage(
                file=relative_to_assets("entry_1.png"))
            entry_bg_1 = canvas.create_image(
                744.0,
                157.5,
                image=entry_image_1
            )
            self.entry_1 = Entry(
                bd=0,
                bg="#B78CFB",
                fg="#000716",
                highlightthickness=0,
                font = custom_font1
            )
            self.entry_1.place(
                x=602.0,
                y=133.0,
                width=284.0,
                height=47.0
            )

            canvas.create_text(
                409.0,
                138.0,
                anchor="nw",
                text="Логин",
                fill="#723EC5",
                font=("MontserratRoman SemiBold", 36 * -1)
            )

            entry_image_2 = PhotoImage(
                file=relative_to_assets("entry_2.png"))
            entry_bg_2 = canvas.create_image(
                744.0,
                238.5,
                image=entry_image_2
            )
            self.entry_2 = Entry(
                bd=0,
                bg="#B78CFB",
                fg="#000716",
                highlightthickness=0,
                font = custom_font1
            )
            self.entry_2.place(
                x=602.0,
                y=214.0,
                width=284.0,
                height=47.0
            )

            canvas.create_text(
                409.0,
                219.0,
                anchor="nw",
                text="Пароль",
                fill="#723EC5",
                font=("MontserratRoman SemiBold", 36 * -1)
            )

            entry_image_3 = PhotoImage(
                file=relative_to_assets("entry_3.png"))
            entry_bg_3 = canvas.create_image(
                744.0,
                318.5,
                image=entry_image_3
            )
            self.entry_3 = Entry(
                bd=0,
                bg="#B78CFB",
                fg="#000716",
                highlightthickness=0,
                font = custom_font1
            )
            self.entry_3.place(
                x=602.0,
                y=294.0,
                width=284.0,
                height=47.0
            )

            canvas.create_text(
                408.0,
                299.0,
                anchor="nw",
                text="Имя",
                fill="#723EC5",
                font=("MontserratRoman SemiBold", 36 * -1)
            )

            entry_image_4 = PhotoImage(
                file=relative_to_assets("entry_4.png"))
            entry_bg_4 = canvas.create_image(
                744.0,
                399.5,
                image=entry_image_4
            )
            self.entry_4 = Entry(
                bd=0,
                bg="#B78CFB",
                fg="#000716",
                highlightthickness=0,
                font = custom_font1
            )
            self.entry_4.place(
                x=602.0,
                y=375.0,
                width=284.0,
                height=47.0
            )

            canvas.create_text(
                408.0,
                380.0,
                anchor="nw",
                text="Фамилия",
                fill="#723EC5",
                font=("MontserratRoman SemiBold", 36 * -1)
            )

            entry_image_5 = PhotoImage(
                file=relative_to_assets("entry_5.png"))
            entry_bg_5 = canvas.create_image(
                744.0,
                480.5,
                image=entry_image_5
            )
            self.entry_5 = Entry(
                bd=0,
                bg="#B78CFB",
                fg="#000716",
                highlightthickness=0,
                font = custom_font1
            )
            self.entry_5.place(
                x=602.0,
                y=456.0,
                width=284.0,
                height=47.0
            )

            canvas.create_text(
                408.0,
                461.0,
                anchor="nw",
                text="Группа",
                fill="#723EC5",
                font=("MontserratRoman SemiBold", 36 * -1)
            )

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))


        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.btn_click1,
            relief="flat"
        )
        button_1.place(
            x=524.0,
            y=570.0,
            width=289.0,
            height=88.0
        )
        self.window2.resizable(False, False)
        self.window2.mainloop()



    def btn_click1(self):

        GG,private_key=CRYPTO.shifor(1,'qw')
        CRYPTO.re_shifor(1,GG,private_key)

        username = self.entry_1.get()
        password = self.entry_2.get()
        name = self.entry_3.get()
        second_name = self.entry_4.get()
        gr = self.entry_5.get()
        data = [username, password, name, second_name, gr]
        print(data)
        connection = sqlite3.connect('db/database.db')
        cursor = connection.cursor()

        if cursor.execute('''INSERT INTO users (login,password,name,second_name,class) VALUES(?,?,?,?,?) ''', data):
            # Выбираем и сортируем пользователей по возрасту по убыванию
            cursor.execute('''SELECT * FROM users ''')
            results = cursor.fetchall()
            connection.commit()
            connection.close()
            #print(results)
            self.window2.destroy()



if __name__ == "__main__":
    REGISTRATION()