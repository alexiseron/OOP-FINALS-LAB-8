from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
import sqlite3

def create_user_window(master):

    def save_command():
        con = sqlite3.connect('OOPLAB8.db')
        cursor = con.cursor()
        create_table_query = '''CREATE TABLE IF NOT EXISTS user_info_tbl (first_name TEXT,middle_name TEXT,last_name TEXT,
                                    suffix TEXT, department TEXT,designation TEXT,username TEXT,password TEXT,confirm_password TEXT,usertype TEXT, userstatus TEXT,employeenum TEXT
                                    )'''
        cursor.execute(create_table_query)

        # Extract data from GUI elements
        data = [
            firstname.get(),
            middlename.get(),
            lastname.get(),
            suffix.get(),
            department.get(),
            designation.get(),
            username.get(),
            password.get(),
            password2.get(),
            usertype.get(),
            userstats.get(),
            empno.get()

        ]

        # Define the SQL query to insert data into the table
        insert_query = '''INSERT INTO user_info_tbl (first_name, middle_name, last_name, suffix, department, designation, username, password, confirm_password, usertype, userstatus, employeenum) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
        cursor.execute(insert_query, data)

        # Commit changes and close the connection
        con.commit()
        con.close()
        entries = [firstname, middlename, lastname, suffix, department, designation,
                   username, password, password2, usertype, userstats, empno]

        print("UPLOADED")

        firstname.delete(0, "end")
        middlename.delete(0, "end")
        lastname.delete(0, "end")
        suffix.delete(0, "end")
        department.delete(0, "end")
        designation.delete(0, "end")
        username.delete(0, "end")
        password.delete(0, "end")
        password2.delete(0, "end")
        userstats.delete(0, "end")
        usertype.delete(0, "end")
        empno.delete(0, "end")

    window = master
    window.geometry('1920x1080')
    window.config(bg='#a2f6c9')
    window.state("zoomed")
    window.title("SERIS USER INFO")

    bg_image = Image.open("C:\\Users\\Axis\\Desktop\\SERIUSER.jpg")
    bg_image = bg_image.resize((1920, 1080))
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = Label(window, image=bg_photo)
    bg_label.image = bg_photo
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    firstname = Label(window, text="FIRST NAME: ", font=('Impact', 20,), bg="#A9C4FF")
    firstname.place(x=580, y=430)
    firstname = Entry(window, width=9, bg='white', font=('Impact', 20,), highlightbackground='black',
                      highlightthickness='2')
    firstname.place(x=580, y=480)

    middlename = Label(window, text="MIDDLE NAME: ", font=('Impact', 20,), bg="#A9C4FF")
    middlename.place(x=780, y=430)
    middlename = Entry(window, width=10, bg='white', font=('Impact', 20,), highlightbackground='black',
                       highlightthickness='2')
    middlename.place(x=780, y=480)

    lastname = Label(window, text="LAST NAME: ", font=('Impact', 20,), bg="#A9C4FF")
    lastname.place(x=1000, y=430)
    lastname = Entry(window, width=9, bg='white', font=('Impact', 20,), highlightbackground='black',
                     highlightthickness='2')
    lastname.place(x=1000, y=480)

    suffix = Label(window, text="SUFFIX: ", font=('Impact', 20,), bg="#A9C4FF")
    suffix.place(x=1200, y=430)
    suffix = Entry(window, width=5, bg='white', font=('Impact', 20,), highlightbackground='black',
                   highlightthickness='2')
    suffix.place(x=1200, y=480)

    department = Label(window, text="DEPARTMENT: ", font=('Impact', 20,), bg="#A9C4FF")
    department.place(x=1330, y=430)
    department = Entry(window, width=10, bg='white', font=('Impact', 20,), highlightbackground='black',
                       highlightthickness='2')
    department.place(x=1330, y=480)

    # second line

    designation = Label(window, text="DESIGNATION: ", font=('Impact', 20,), bg="#A9C4FF")
    designation.place(x=390, y=550)
    designation = Entry(window, width=20, bg='white', font=('Impact', 20,), highlightbackground='black',
                        highlightthickness='2')
    designation.place(x=390, y=600)

    username = Label(window, text="USERNAME: ", font=('Impact', 20,), bg="#A9C4FF")
    username.place(x=785, y=550)
    username = Entry(window, width=20, bg='white', font=('Impact', 20,), highlightbackground='black',
                     highlightthickness='2')
    username.place(x=785, y=600)

    password = Label(window, text="PASSWORD: ", font=('Impact', 20,), bg="#A9C4FF")
    password.place(x=1185, y=550)
    password = Entry(window, width=18, bg='white', font=('Impact', 20,), highlightbackground='black',
                     highlightthickness='2', show="*")
    password.place(x=1185, y=600)

    # third line

    password2 = Label(window, text="CONFIRM PASSWORD: ", font=('Impact', 20,), bg="#A9C4FF")
    password2.place(x=390, y=670)
    password2 = Entry(window, width=20, bg='white', font=('Impact', 20,), highlightbackground='black',
                      highlightthickness='2')
    password2.place(x=390, y=720)

    usertype = Label(window, text="USERTYPE: ", font=('Impact', 20,), bg="#A9C4FF")
    usertype.place(x=785, y=670)
    usertype = Entry(window, width=13, bg='white', font=('Impact', 20,), highlightbackground='black',
                     highlightthickness='2')
    usertype.place(x=785, y=720)

    userstats = Label(window, text="USERSTATUS: ", font=('Impact', 20,), bg="#A9C4FF")
    userstats.place(x=1055, y=670)
    userstats = Entry(window, width=13, bg='white', font=('Impact', 20,), highlightbackground='black',
                      highlightthickness='2')
    userstats.place(x=1055, y=720)

    empno = Label(window, text="EMPLOYEE #: ", font=('Impact', 20,), bg="#A9C4FF")
    empno.place(x=1325, y=670)
    empno = Entry(window, width=11, bg='white', font=('Impact', 20,), highlightbackground='black',
                  highlightthickness='2')
    empno.place(x=1325, y=720)

    # BUTTONS
    update = Button(window, bg='#0077b6', fg='white', text="UPDATE", width=15, font=("Impact", 15),
                    highlightbackground='black', highlightthickness='2')
    update.place(x=550, y=820)

    delete = Button(window, bg='#FFDE59', fg='black', text="DELETE", width=15, font=("Impact", 15),
                    highlightbackground='black', highlightthickness='2')
    delete.place(x=750, y=820)

    save_button = Button(window, bg='#FFFFFF', fg='black', text="CANCEL", width=15, font=("Impact", 15),
                         highlightbackground='black', highlightthickness='2', command=save_command)
    save_button.place(x=950, y=820)


def User(master):
    create_user_window(master)