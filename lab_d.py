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
            first_name.get(),
            middle_name.get(),
            last_name.get(),
            suffix.get(),
            department.get(),
            designation.get(),
            username.get(),
            password.get(),
            confirm_password.get(),
            usertype.get(),
            userstatus.get(),
            employeenum.get()

        ]

        # Define the SQL query to insert data into the table
        insert_query = '''INSERT INTO user_info_tbl (first_name, middle_name, last_name, suffix, department, designation, username, password, confirm_password, usertype, userstatus, employeenum) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
        cursor.execute(insert_query, data)

        # Commit changes and close the connection
        con.commit()
        con.close()
        entries = [first_name, middle_name, last_name, suffix, department, designation,
                   username, password, confirm_password, usertype, userstatus, employeenum]

        print("UPLOADED")

        first_name.delete(0, "end")
        middle_name.delete(0, "end")
        last_name.delete(0, "end")
        suffix.delete(0, "end")
        department.delete(0, "end")
        designation.delete(0, "end")
        username.delete(0, "end")
        password.delete(0, "end")
        confirm_password.delete(0, "end")
        userstatus.delete(0, "end")
        usertype.delete(0, "end")
        employeenum.delete(0, "end")

    window = master
    window.geometry("1200x799")
    window.title("EMPLOYEE WINDOW")

    bg_image = Image.open("C:\\Users\\Axis\\Desktop\\BG.jpg")
    bg_image = bg_image.resize((1200, 799))  # Resize image to match window size
    bg_photo = ImageTk.PhotoImage(bg_image)

    bg_label = tk.Label(window, image=bg_photo)
    bg_label.image = bg_photo  # Keep a reference to avoid garbage collection
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    user_prof = PhotoImage(file='pics/userprof2.png')
    user_prof = user_prof.subsample(15, 15)

    frame = Frame(window, width=900, height=500, bg="#87CEEB")
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    label = Label(frame, image=user_prof)
    label.place(x=22, y=100)

    label = Label(window, text="User Account Information", font=('serif', 25, 'bold'), bg="#87CEEB")
    label.place(x=165, y=130)

    first_name = Label(window, text="First Name", font=(13), bg="#87CEEB")
    first_name.place(relx=.26, rely=.39)
    first_name = Entry(window, bg="#FFFFFF")
    first_name.place(relx=.26, rely=.43)

    middle_name = Label(window, text="Middle Name", font=(13), bg="#87CEEB")
    middle_name.place(relx=.38, rely=.39)
    middle_name = Entry(window, bg="#FFFFFF")
    middle_name.place(relx=.38, rely=.43)

    last_name = Label(window, text="Last Name", font=(13), bg="#87CEEB")
    last_name.place(relx=.51, rely=.39)
    last_name = Entry(window, bg="#FFFFFF")
    last_name.place(relx=.51, rely=.43)

    suffix = Label(window, text="Suffix", font=(13), bg="#87CEEB")
    suffix.place(relx=.64, rely=.39)
    suffix = Entry(window, bg="#FFFFFF")
    suffix.place(relx=.64, rely=.43)

    department = Label(window, text="Department", font=(20), bg="#87CEEB")
    department.place(relx=.76, rely=.39)
    department = Entry(window, bg="#FFFFFF")
    department.place(relx=.76, rely=.43)

    designation = Label(window, text="Designation", font=(20), bg="#87CEEB")
    designation.place(relx=.15, rely=.50)
    designation = Entry(window, bg="#FFFFFF", width=40)
    designation.place(relx=.15, rely=.55)

    username = Label(window, text="Username", font=(20), bg="#87CEEB")
    username.place(relx=.38, rely=.50)
    username = Entry(window, bg="#FFFFFF", width=40)
    username.place(relx=.38, rely=.55)

    password = Label(window, text="Password", font=(20), bg="#87CEEB")
    password.place(relx=.63, rely=.50)
    password = Entry(window, bg="#FFFFFF", width=40, show="*")
    password.place(relx=.63, rely=.55)

    confirm_password = Label(window, text="Confirm Password", font=(20), bg="#87CEEB")
    confirm_password.place(relx=.15, rely=.61)
    confirm_password = Entry(window, bg="#FFFFFF", width=40, show="*")
    confirm_password.place(relx=.15, rely=.66)

    usertype = Label(window, text="User Type", font=(20), bg="#87CEEB")
    usertype.place(relx=.38, rely=.61)
    usertype = Entry(window, bg="#FFFFFF", width=29)
    usertype.place(relx=.38, rely=.66)

    userstatus = Label(window, text="User Status", font=(20), bg="#87CEEB")
    userstatus.place(relx=.55, rely=.61)
    userstatus = Entry(window, bg="#FFFFFF", width=26)
    userstatus.place(relx=.55, rely=.66)

    employeenum = Label(window, text="Employee Number", font=(20), bg="#87CEEB")
    employeenum.place(relx=.70, rely=.61)
    employeenum = Entry(window, bg="#FFFFFF", width=28)
    employeenum.place(relx=.70, rely=.66)

    update_button = Button(window, text="Update", bg="#3E64dA", font=("Arial", 16),
                           fg="#FFFFFF", width=10, command=save_command)
    update_button.place(relx=.36, rely=.78, anchor=CENTER)

    delete_button = Button(window, text="Delete", bg="#FFDB58", font=("Arial", 16),
                           fg="#000000", width=10)
    delete_button.place(relx=.51, rely=.78, anchor=CENTER)

    cancel_button = Button(window, text="Cancel", bg="#FFFFFF", font=("Arial, 16"),
                           fg="#000000", width=10)
    cancel_button.place(relx=.66, rely=.78, anchor=CENTER)

def User(master):
    create_user_window(master)