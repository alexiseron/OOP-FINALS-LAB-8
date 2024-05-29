import sqlite3
from tkinter import *
from tkcalendar import DateEntry

def create_employee_info_window(master):

    def create_label_entry(frame, text, x_rel, y_rel, width):
        label = Label(frame, text=text, font=("Arial", 10), bg="#FFFFFF")
        label.place(relx=x_rel, rely=y_rel)

        entry = Entry(frame, bg="#E4E0E0", width=width)
        entry.place(relx=x_rel, rely=y_rel + 0.04)

        return entry

    def create_option_menu(frame, options, x_rel, y_rel, width):
        selected_option = StringVar()
        selected_option.set(options[0])
        option_menu = OptionMenu(frame, selected_option, *options, command=on_select)
        option_menu.config(bg="#FFFFFF", activebackground="#E4E0E0", bd=0, width=width, height=1)
        option_menu.place(relx=x_rel, rely=y_rel)
        return selected_option

    def browse_file():
        pass

    def on_select(value):
        print("Selected gender:", value)

    def save_command():
        conn = sqlite3.connect('C:\\Users\\Axis\\PycharmProjects\\OOP FINALS LAB 8\\OOPLAB8.db')
        cursor = conn.cursor()
        create_table_query = '''CREATE TABLE IF NOT EXISTS employee_registration (
            firstname TEXT,
            middlename TEXT,
            lastname TEXT,
            suffix TEXT,
            bday TEXT,
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

        data = [
            firstname.get(),
            middlename.get(),
            lastname.get(),
            suffix.get(),
            bday_entry.get(),
            selected_gender.get(),
            selected_nationality.get(),
            selected_civilstat.get(),
            department.get(),
            designation.get(),
            selected_qualitydepstat.get(),
            empstatus.get(),
            paydate_entry.get(),
            employeenum.get(),
            contactno.get(),
            email.get(),
            selected_socmed.get(),
            socmedno.get(),
            address1.get(),
            address2.get(),
            city.get(),
            state.get(),
            selected_country.get(),
            zipcode.get()
        ]

        insert_query = '''INSERT INTO employee_registration (
            firstname, middlename, lastname, suffix, bday, gender, nationality, civilstat, department, designation, qualitydepstat, empstatus, paydate, employeenum, contactno, email, socmed, socmedno, address1, address2, city, state, country, zipcode
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
        cursor.execute(insert_query, data)

        conn.commit()
        conn.close()

        print("UPLOADED")

        clear_entries()

    def clear_entries():
        entries = [
            firstname, middlename, lastname, suffix,
            bday_entry, selected_gender, selected_nationality,
            selected_civilstat, department, designation,
            selected_qualitydepstat, empstatus, paydate_entry,
            employeenum, contactno, email, selected_socmed,
            socmedno, address1, address2, city, state,
            selected_country, zipcode
        ]

        for entry in entries:
            if isinstance(entry, Entry):
                entry.delete(0, "end")
            elif isinstance(entry, StringVar):
                entry.set("")

    window = master
    window.geometry("1200x800")
    window.config(bg="#87CEEB")

    frame = Frame(window, width=1100, height=700, bg="#FFFFFF")
    frame.place(relx=.5, rely=.5, anchor="center")

    user_prof = PhotoImage(file='C:\\Users\\Axis\\PycharmProjects\\OOP FINALS LAB 8\\pics\\userprof2.png')
    user_prof = user_prof.subsample(4, 4)

    label = Label(frame, image=user_prof)
    label.place(x=130, y=100)

    choose_file_button = Button(window, text="Choose File", command=browse_file)
    choose_file_button.pack(padx=250, pady=200, anchor='nw')

    boldtitle = Label(frame, text="SE-RI'S EMPLOYEE PERSONAL INFORMATION", font=('Algerian', 30, 'bold'), bg="#FFFFFF")
    boldtitle.place(x=100, y=50)

    firstname = create_label_entry(frame, "First Name", 0.28, 0.2, 25)
    middlename = create_label_entry(frame, "Middle Name", 0.45, 0.2, 25)
    lastname = create_label_entry(frame, "Last Name", 0.61, 0.2, 25)
    suffix = create_label_entry(frame, "Suffix", 0.77, 0.2, 25)

    bday = Label(window, text="Date of Birth", font=("Arial", 10), bg="#FFFFFF")
    bday.place(relx=.297, rely=.29)
    bday_entry = DateEntry(window, bg="#E4E0E0", width=18, borderwidth=2, font=("Helvetica", 11))
    bday_entry.place(relx=.297, rely=.32)

    gender = Label(frame, text="Gender", font=("Arial", 10), bg="#FFFFFF")
    gender.place(relx=.45, rely=.27)
    gender_options = ["Select your gender", "Male", "Female", "Others"]
    selected_gender = create_option_menu(frame, gender_options, 0.45, 0.3, 15)

    nationality = Label(frame, text="Nationality", font=("Arial", 10), bg="#FFFFFF")
    nationality.place(relx=.61, rely=.27)
    nationality_options = ["---", "Filipino", "American", "Chinese"]
    selected_nationality = create_option_menu(frame, nationality_options, 0.61, 0.3, 13)

    civilstat = Label(frame, text="Civil Status", font=("Arial", 10), bg="#FFFFFF")
    civilstat.place(relx=.77, rely=.27)
    civilstat_options = ["--Select One--", "Single", "Married", "Widow"]
    selected_civilstat = create_option_menu(frame, civilstat_options, 0.77, 0.3, 15)

    department = create_label_entry(frame, "Department", 0.1, 0.38, 50)
    designation = create_label_entry(frame, "Designation", 0.42, 0.38, 40)

    qualitydepstat = Label(frame, text="Quality Dep. Status", font=("Arial", 10), bg="#FFFFFF")
    qualitydepstat.place(relx=.67, rely=.38)
    qualitydepstat_options = ["--select one--"]
    selected_qualitydepstat = create_option_menu(frame, qualitydepstat_options, 0.67, 0.41, 30)

    empstatus = create_label_entry(frame, "Employee Status", 0.1, 0.46, 70)

    paydate = Label(window, text="Paydate", font=("Arial", 10), bg="#FFFFFF")
    paydate.place(relx=.53, rely=.46)
    paydate_entry = DateEntry(window, bg="#E4E0E0", width=7, borderwidth=2, font=("Helvetica", 11))
    paydate_entry.place(relx=.53, rely=.5)

    employeenum = create_label_entry(frame, "Employee Number", 0.65, 0.46, 30)

    semi_heading = Label(frame, text="Contact Info", font=('Arial', 15, 'bold'), bg="#FFFFFF")
    semi_heading.place(x=100, y=385)

    contactno = create_label_entry(frame, "Contact No.", 0.1, 0.6, 30)
    email = create_label_entry(frame, "Email", 0.3, 0.6, 45)

    socmed = Label(frame, text="Other (Social Media)", font=("Arial", 10), bg="#FFFFFF")
    socmed.place(relx=.56, rely=.6)
    socmed_options = ["--select one--"]
    selected_socmed = create_option_menu(frame, socmed_options, 0.56, 0.64, 25)

    socmedno = create_label_entry(frame, "Social Media Account ID/NO", 0.76, 0.6, 40)

    semi_heading2 = Label(frame, text="Address", font=('Arial', 15, 'bold'), bg="#FFFFFF")
    semi_heading2.place(x=100, y=480)

    address1 = create_label_entry(frame, "Address Line 1", 0.1, 0.74, 50)
    address2 = create_label_entry(frame, "Address Line 2", 0.4, 0.74, 50)
    city = create_label_entry(frame, "City Municipality", 0.1, 0.81, 50)
    state = create_label_entry(frame, "State/Province", 0.4, 0.81, 50)

    country = Label(frame, text="Country", font=("Arial", 10), bg="#FFFFFF")
    country.place(relx=.7, rely=.74)
    country_options = ["--select one--"]
    selected_country = create_option_menu(frame, country_options, 0.7, 0.77, 25)

    zipcode = create_label_entry(frame, "Zip Code", 0.7, 0.81, 25)

    save_button = Button(frame, text="SAVE", bg="#87CEEB", font=("Arial, 10"),
                         fg="#000000", width=6, height=1, command=save_command)
    save_button.place(x=100, y=650)

def EmployeeInfo(master):
    create_employee_info_window(master)