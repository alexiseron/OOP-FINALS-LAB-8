import tkinter as tk
import sqlite3
from PIL import Image, ImageTk


def create_employeeinfowindow(master):

    def save_command():
        conn = sqlite3.connect('OOPLAB8.db')
        cursor = conn.cursor()
        create_table_query = '''CREATE TABLE IF NOT EXISTS employee_info_tbl (
                                    firstname TEXT,
                                    middlename TEXT,
                                    lastname TEXT,
                                    suffix TEXT,
                                    dateofbirth TEXT,
                                    gender TEXT,
                                    nationality TEXT,
                                    civilstat TEXT,
                                    department TEXT,
                                    designation TEXT,
                                    qualitydepstat TEXT,
                                    empstatus TEXT,
                                    paydate TEXT,
                                    employeenum TEXT,
                                    contactno TEXT,
                                    email TEXT,
                                    socmed TEXT,
                                    socmedno TEXT,
                                    address1 TEXT,
                                    address2 TEXT,
                                    city TEXT,
                                    state TEXT,
                                    country TEXT,
                                    zipcode TEXT
                                )'''
        cursor.execute(create_table_query)

        # Extract data from GUI elements
        data = [
            firstname_entry.get(),
            middlename_entry.get(),
            lastname_entry.get(),
            suffix_entry.get(),
            dateofbirth_entry.get(),
            gender_entry.get(),
            nationality_entry.get(),
            civilstat_entry.get(),
            department_entry.get(),
            designation_entry.get(),
            qualitydepstat_entry.get(),
            empstatus_entry.get(),
            paydate_entry.get(),
            employeenum_entry.get(),
            contactno_entry.get(),
            email_entry.get(),
            socmed_entry.get(),
            socmedno_entry.get(),
            address1_entry.get(),
            address2_entry.get(),
            city_entry.get(),
            state_entry.get(),
            country_entry.get(),
            zipcode_entry.get()
        ]

        # Define the SQL query to insert data into the table
        insert_query = '''INSERT INTO employee_info_tbl (
                            firstname, middlename, lastname, suffix, dateofbirth, gender, nationality, civilstat, department,
                            designation, qualitydepstat, empstatus, paydate, employeenum, contactno, email, socmed, socmedno,
                            address1, address2, city, state, country, zipcode
                          ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
        cursor.execute(insert_query, data)

        # Commit changes and close the connection
        conn.commit()
        conn.close()
        print("UPLOADED TO THE DATABASE")

    def clear_inputs():
        print("Clearing inputs...")
        firstname_entry.delete(0, tk.END)
        middlename_entry.delete(0, tk.END)
        lastname_entry.delete(0, tk.END)
        suffix_entry.delete(0, tk.END)
        dateofbirth_entry.delete(0, tk.END)
        gender_entry.delete(0, tk.END)
        nationality_entry.delete(0, tk.END)
        civilstat_entry.delete(0, tk.END)
        department_entry.delete(0, tk.END)
        designation_entry.delete(0, tk.END)
        qualitydepstat_entry.delete(0, tk.END)
        empstatus_entry.delete(0, tk.END)
        paydate_entry.delete(0, tk.END)
        employeenum_entry.delete(0, tk.END)
        contactno_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        socmed_entry.delete(0, tk.END)
        socmedno_entry.delete(0, tk.END)
        address1_entry.delete(0, tk.END)
        address2_entry.delete(0, tk.END)
        city_entry.delete(0, tk.END)
        state_entry.delete(0, tk.END)
        country_entry.delete(0, tk.END)
        zipcode_entry.delete(0, tk.END)


    window = master
    window.geometry('1920x1080')
    window.state("zoomed")
    window.config(bg='#a2f6c9')

    bg_image = Image.open("C:\\Users\\Axis\\Desktop\\SERIEMPLOYEE.jpg")
    bg_image = bg_image.resize((1920, 1080))
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = tk.Label(window, image=bg_photo)
    bg_label.image = bg_photo
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)


    firstframe = tk.Frame(window, width=800, height=150, bg='#CADDFF', highlightbackground='black', highlightthickness='2')
    firstframe.pack()
    firstframe.place(x=70, y=100)

    secondframe = tk.Frame(window, width=800, height=150, bg='#CADDFF', highlightbackground='black', highlightthickness='2')
    secondframe.pack()
    secondframe.place(x=70, y=270)

    thirdframe = tk.Frame(window, width=800, height=150, bg='#CADDFF', highlightbackground='black', highlightthickness='2')
    thirdframe.pack()
    thirdframe.place(x=70, y=440)

    fourthframe = tk.Frame(window, width=800, height=360, bg='#CADDFF', highlightbackground='black', highlightthickness='2')
    fourthframe.pack()
    fourthframe.place(x=70, y=610)

    # entries and labels

    userframe = tk.Frame(window, width=130, height=130, bg='#CADDFF', highlightbackground='black', highlightthickness='2')
    userframe.place(x=70, y=40)

    filebutton = tk.Button(window, width='10', text="Choose File", bg="white", fg="black", highlightbackground='#a2f6c9', highlightthickness='3', font=('Algerian', 8, 'bold'))
    filebutton.place(x=85, y=190)

    tk.Label(window, text="First Name:", font=('Algerian', 12,), bg="#CADDFF").place(x=235, y=110)
    firstname_entry = tk.Entry(window, width='20', bg="#FFFFFF", highlightbackground='black', highlightthickness='2')
    firstname_entry.place(x=235, y=140)

    tk.Label(window, text="Middle Name:", font=('Algerian', 12,), bg="#CADDFF").place(x=415, y=110)
    middlename_entry = tk.Entry(window, width='20', bg="#FFFFFF", highlightbackground='black', highlightthickness='2')
    middlename_entry.place(x=415, y=140)

    tk.Label(window, text="Last Name:", font=('Algerian', 12,), bg="#CADDFF").place(x=590, y=110)
    lastname_entry = tk.Entry(window, width='20', bg="#FFFFFF", highlightbackground='black', highlightthickness='2')
    lastname_entry.place(x=590, y=140)

    tk.Label(window, text="Suffix:", font=('Algerian', 12,), bg="#CADDFF").place(x=765, y=110)
    suffix_entry = tk.Entry(window, width='10', bg="#FFFFFF", highlightbackground='black', highlightthickness='2')
    suffix_entry.place(x=765, y=140)

    tk.Label(window, text="Date of Birth:", font=('Algerian', 12), bg="#CADDFF").place(x=235, y=170)
    dateofbirth_entry = tk.Entry(window, width='20', bg="#FFFFFF", highlightbackground='black', highlightthickness='2')
    dateofbirth_entry.place(x=235, y=200)

    tk.Label(window, text="Gender:", font=('Algerian', 12,), bg="#CADDFF").place(x=415, y=170)
    gender_entry = tk.Entry(window, width='10', bg="#FFFFFF", highlightbackground='black', highlightthickness='2')
    gender_entry.place(x=415, y=200)

    tk.Label(window, text="Nationality:", font=('Algerian', 12,), bg="#CADDFF").place(x=515, y=170)
    nationality_entry = tk.Entry(window, width='20', bg="#FFFFFF", highlightbackground='black', highlightthickness='2')
    nationality_entry.place(x=515, y=200)

    tk.Label(window, text="Civil Status:", font=('Algerian', 12,), bg="#CADDFF").place(x=690, y=170)
    civilstat_entry = tk.Entry(window, width='19', bg="#FFFFFF", highlightbackground='black', highlightthickness='2')
    civilstat_entry.place(x=695, y=200)

    # 2nd frame

    tk.Label(window, text="Department:", font=('Algerian', 12,), bg="#CADDFF").place(x=90, y=280)
    department_entry = tk.Entry(window, width='50', bg="#FFFFFF", highlightbackground='black', highlightthickness='2')
    department_entry.place(x=90, y=310)

    tk.Label(window, text="Designation:", font=('Algerian', 12,), bg="#CADDFF").place(x=510, y=280)
    designation_entry = tk.Entry(window, width='20', bg="#FFFFFF", highlightbackground='black', highlightthickness='2')
    designation_entry.place(x=510, y=310)

    tk.Label(window, text="Qualified Dep. Status:", font=('Algerian', 8, 'bold'), bg="#CADDFF").place(x=685, y=285)
    qualitydepstat_entry = tk.Entry(window, width='20', bg="#FFFFFF", highlightbackground='black', highlightthickness='2')
    qualitydepstat_entry.place(x=690, y=310)

    tk.Label(window, text="Employee Status:", font=('Algerian', 12,), bg="#CADDFF").place(x=90, y=350)
    empstatus_entry = tk.Entry(window, width='60', bg="#FFFFFF", highlightbackground='black', highlightthickness='2')
    empstatus_entry.place(x=90, y=375)

    tk.Label(window, text="PayDate:", font=('Algerian', 10), bg="#CADDFF").place(x=590, y=350)
    paydate_entry = tk.Entry(window, width='10', bg="#FFFFFF", highlightbackground='black', highlightthickness='2')
    paydate_entry.place(x=590, y=375)

    tk.Label(window, text="Employee Number:", font=('Algerian', 10), bg="#CADDFF").place(x=685, y=350)
    employeenum_entry = tk.Entry(window, width='20', bg="#FFFFFF", highlightbackground='black', highlightthickness='2')
    employeenum_entry.place(x=690, y=375)

    # 3rd frame

    tk.Label(window, text="Contact Info:", font=('Algerian', 12,), bg="#CADDFF").place(x=90, y=450)
    contactno_entry = tk.Entry(window, width='45', bg="#FFFFFF", highlightbackground='black', highlightthickness='2')
    contactno_entry.place(x=90, y=480)

    tk.Label(window, text="Email:", font=('Algerian', 12,), bg="#CADDFF").place(x=480, y=450)
    email_entry = tk.Entry(window, width='45', bg="#FFFFFF", highlightbackground='black', highlightthickness='2')
    email_entry.place(x=480, y=480)

    tk.Label(window, text="Other (Social Media):", font=('Algerian', 12,), bg="#CADDFF").place(x=90, y=510)
    socmed_entry = tk.Entry(window, width='45', bg="#FFFFFF", highlightbackground='black', highlightthickness='2')
    socmed_entry.place(x=90, y=540)

    tk.Label(window, text="Social Media Account ID/No:", font=('Algerian', 12,), bg="#CADDFF").place(x=480, y=510)
    socmedno_entry = tk.Entry(window, width='45', bg="#FFFFFF", highlightbackground='black', highlightthickness='2')
    socmedno_entry.place(x=480, y=540)

    # 4th frame

    tk.Label(window, text="Address Line 1:", font=('Algerian', 12,), bg="#CADDFF").place(x=90, y=620)
    address1_entry = tk.Entry(window, width='94', bg="#FFFFFF", highlightbackground='black', highlightthickness='2')
    address1_entry.place(x=90, y=650)

    tk.Label(window, text="Address Line 2:", font=('Algerian', 12,), bg="#CADDFF").place(x=90, y=690)
    address2_entry = tk.Entry(window, width='94', bg="#FFFFFF", highlightbackground='black', highlightthickness='2')
    address2_entry.place(x=90, y=720)

    tk.Label(window, text="City/Municipality:", font=('Algerian', 12,), bg="#CADDFF").place(x=90, y=760)
    city_entry = tk.Entry(window, width='45', bg="#FFFFFF", highlightbackground='black', highlightthickness='2')
    city_entry.place(x=90, y=790)

    tk.Label(window, text="State/Province:", font=('Algerian', 12,), bg="#CADDFF").place(x=480, y=760)
    state_entry = tk.Entry(window, width='45', bg="#FFFFFF", highlightbackground='black', highlightthickness='2')
    state_entry.place(x=480, y=790)

    tk.Label(window, text="Country:", font=('Algerian', 12,), bg="#CADDFF").place(x=90, y=830)
    country_entry = tk.Entry(window, width='45', bg="#FFFFFF", highlightbackground='black', highlightthickness='2')
    country_entry.place(x=90, y=860)

    tk.Label(window, text="Zip Code:", font=('Algerian', 12,), bg="#CADDFF").place(x=480, y=830)
    zipcode_entry = tk.Entry(window, width='25', bg="#FFFFFF", highlightbackground='black', highlightthickness='2')
    zipcode_entry.place(x=480, y=860)

    tk.Label(window, text="Picture Path:", font=('Algerian', 12,), bg="#CADDFF").place(x=90, y=900)
    picpath_entry = tk.Entry(window, width='40', bg="#FFFFFF", highlightbackground='black', highlightthickness='2')
    picpath_entry.place(x=90, y=930)

    save = tk.Button(window, width='10', text="Save", bg="black", fg="white", border='2', highlightbackground='#a2f6c9', highlightthickness='3', font=('Algerian', 10,), command=save_command)
    save.place(x=620, y=910)

    cancel = tk.Button(window, width='10', text="Cancel", bg="white", fg="black", border='2', highlightbackground='#a2f6c9', highlightthickness='3', font=('Algerian', 10,), command=clear_inputs)
    cancel.place(x=740, y=910)

def EmployeeInfo(master):
    create_employeeinfowindow(master)