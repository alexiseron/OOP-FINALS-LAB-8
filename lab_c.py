from tkinter import *
import sqlite3
from PIL import Image, ImageTk

def create_payrollwindow(master):

    def selected_civil_status(choice):
        print("Selected Civil Status: " + choice)


    def selected_quality(choice):
        print("Selected Quality Dep. Status: " + choice)


    def selected_paydate(choice):
        print("Selected Paydate: " + choice)

    def search():
            con = sqlite3.connect("OOPLAB8.db")
            cur = con.cursor()
            cur.execute(f"SELECT * FROM employee_info_tbl WHERE employeenum = '{employeenum.get()}'")

            info = cur.fetchone()
            print(info)

            first_name_entry.delete(0, "end")
            first_name_entry.insert(0, info[1])

            middle_name_entry.delete(0, "end")
            middle_name_entry.insert(0, info[2])

            last_name_entry.delete(0, "end")
            last_name_entry.insert(0, info[3])

            dept_entry.delete(0, "end")
            dept_entry.insert(0, info[9])

            civil_status_entry.delete(0, "end")
            civil_status_entry.insert(0, info[8])

            qualified_menu.delete(0, "end")
            qualified_menu.insert(0, info[11])

            paydate_entry.delete(0, "end")
            paydate_entry.insert(0, info[13])

            emp_stat_entry.delete(0, "end")
            emp_stat_entry.insert(0, info[12])

            designation_entry.delete(0, "end")
            designation_entry.insert(0, info[10])

            con.close()

    def netIncome():
        gross = float(gross_entry.get())

        # ---------- SSS Contribution Computation ---------- #
        sss_con, g_var = 180.00, gross

        while sss_con < 900.00 and g_var >= 4250:
            g_var -= 500.00
            sss_con += 22.50

        SSS_entry.config(state="normal")
        SSS_entry.delete(0, "end")
        SSS_entry.insert(0, f"{sss_con}")
        SSS_entry.config(state="readonly")

        # ---------- PhilHealth contribution ---------- #
        s_co = paydate_entry.get().split("/")
        salary_cutoff_year = int(s_co[2])

        if salary_cutoff_year == 2019:
            premium_rate = 0.0275
            upper_value = 50000
        elif salary_cutoff_year == 2020:
            premium_rate = 0.03
            upper_value = 60000
        elif salary_cutoff_year == 2021:
            premium_rate = 0.035
            upper_value = 70000
        elif salary_cutoff_year == 2022:
            premium_rate = 0.04
            upper_value = 80000
        elif salary_cutoff_year == 2023:
            premium_rate = 0.045
            upper_value = 90000
        else:  # for years 2024-2025
            premium_rate = 0.05
            upper_value = 100000

        if gross <= 10000:
            philhealth_con = 10000 * premium_rate
            # if gross earnings is less than PhP 10,000, a fixed value is deducted
        elif 10000 > gross > upper_value:
            philhealth_con = gross * premium_rate
            # if gross earnings is more than 10k but less than the upper value,
            # the contribution is based on a percentage of the premium rate
        else:
            philhealth_con = upper_value * premium_rate
            #  if gross earnings is higher than year's upper value (e.g. year 2024 = 100,000),
            #  a fixed value is also deducted

        phil_entry.config(state="normal")
        phil_entry.delete(0, "end")
        phil_entry.insert(0, f"{philhealth_con}")
        phil_entry.config(state="readonly")

        # ----------Withholding Tax ---------- #
        if 0.00 < gross <= 10417.00:
            withholding_tax = 0
        elif 10417.00 < gross <= 16666.00:
            over = gross - 10417.00
            withholding_tax = 0 + (over * 0.15)
        elif 16666.00 < gross <= 33332.00:
            over = gross - 16667.00
            withholding_tax = 937.50 + (over * 0.2)
        elif 33332.00 < gross <= 83332.00:
            over = gross - 33333.00
            withholding_tax = 4270.70 + (over * 0.25)
        elif 83332.00 < gross <= 333332.00:
            over = gross - 83333.00
            withholding_tax = 16770.70 + (over * 0.3)
        else:  # for gross pay equal to 333,333 and above
            over = gross - 333333.00
            withholding_tax = 91770.70 + (over * 0.35)

        tax_entry.config(state="normal")
        tax_entry.delete(0, "end")
        tax_entry.insert(0, f"{withholding_tax}")
        tax_entry.config(state="readonly")

        pagibig_entry.config(state="normal")
        pagibig_entry.delete(0, "end")
        pagibig_entry.insert(0, "100")
        pagibig_entry.config(state="readonly")

        deduction = float(sss_con + philhealth_con + withholding_tax + 100)

        deduction += float(sss_loan_entry.get())
        deduction += float(pagibig_loan_entry.get())
        deduction += float(faculty_loan_entry.get())
        deduction += float(faculty_deposit_entry.get())
        deduction += float(salary_loan_entry.get())
        deduction += float(other_loan_entry.get())

        total_loan_entry.config(state="normal")
        total_loan_entry.delete(0, "end")
        total_loan_entry.insert(0, f"{deduction}")
        total_loan_entry.config(state="readonly")
        net_entry.config(state="normal")
        net_entry.delete(0, "end")
        net_entry.insert(0, f"{gross - deduction}")
        net_entry.config(state="readonly")

    def grossIncome():
        income_0 = float(rate_entry.get()) * float(cut_off_entry.get())
        income_1 = float(rate1_entry.get()) * float(cut_off1_entry.get())
        income_2 = float(rate2_entry.get()) * float(cut_off2_entry.get())
        gross_income = income_0 + income_1 + income_2
        gross_entry.insert(0, gross_income)

        income_entry.insert(0, income_0)
        income1_entry.insert(0, income_1)
        income2_entry.insert(0, income_2)

    def save_command():
        # Connect to SQLite database
        conn = sqlite3.connect('OOPLAB8.db')  # Changed from .py to .db
        cursor = conn.cursor()

        # Create table if it does not exist
        create_table_query = '''CREATE TABLE IF NOT EXISTS payrollseris (
            employeenum TEXT,
            first_name_entry TEXT,
            middle_name_entry TEXT,
            last_name_entry TEXT,
            civil_status_entry TEXT,
            qualified_menu TEXT,
            paydate_entry TEXT,
            emp_stat_entry TEXT,
            designation_entry TEXT,
            basic_income TEXT,
            honorarium_income TEXT,
            other_income TEXT,
            gross_income TEXT,
            net_entry TEXT,
            total_deduction TEXT
        )'''
        cursor.execute(create_table_query)

        # Extract data from GUI elements
        data = [
            employeenum.get(),
            first_name_entry.get(),
            middle_name_entry.get(),
            last_name_entry.get(),
            civil_status_entry.get(),
            qualified_menu.get(),
            paydate_entry.get(),
            emp_stat_entry.get(),
            designation_entry.get(),
            income_entry.get(),
            income1_entry.get(),
            income2_entry.get(),
            gross_entry.get(),
            net_entry.get(),
            total_loan_entry.get()
        ]

        # Define the SQL query to insert data into the table
        insert_query = '''INSERT INTO payrollseris (
            employeenum, first_name_entry, middle_name_entry, last_name_entry, civil_status_entry,
            qualified_menu, paydate_entry, emp_stat_entry, designation_entry,
            basic_income, honorarium_income, other_income, gross_income, net_entry, total_deduction
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
        cursor.execute(insert_query, data)

        # Commit changes and close the connection
        conn.commit()
        conn.close()

        # Print confirmation message
        print("UPLOADED")

        # Clear the entries (Optional)
        entries = [first_name_entry, middle_name_entry, last_name_entry, civil_status_entry, qualified_menu, paydate_entry,
                   emp_stat_entry, designation_entry,
                   income_entry, income1_entry, income2_entry, gross_entry, net_entry, total_loan_entry]
        for entry in entries:
            entry.delete(0, 'end')

    def clear_entries():
        for entry in (employeenum, dept_entry, rate_entry, cut_off_entry, income_entry,
                      rate1_entry, cut_off1_entry, income1_entry,
                      rate2_entry, cut_off2_entry, income2_entry,
                      gross_entry, net_entry,
                      first_name_entry, middle_name_entry, last_name_entry,
                      civil_status_entry, qualified_menu, paydate_entry,
                      emp_stat_entry, designation_entry,
                      SSS_entry, phil_entry, pagibig_entry, tax_entry,
                      sss_loan_entry, pagibig_loan_entry, faculty_deposit_entry,
                      faculty_loan_entry, salary_loan_entry, other_loan_entry,
                      total_loan_entry):
            entry.delete(0, 'end')

    window = master
    window.geometry('1920x1080')
    window.config(bg='#a2f6c9')
    window.state("zoomed")
    window.title("SERIS CHOICE PAYROLL")

    bg_image = Image.open("C:\\Users\\Axis\\Desktop\\SERIPAYROLL.jpg")
    bg_image = bg_image.resize((1920, 1080))
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = Label(window, image=bg_photo)
    bg_label.image = bg_photo
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Employee Number
    employeenum = Label(window, text="Employee Number: ",font=('Algerian', 12,), bg="#A9C4FF")
    employeenum.place(x=510, y=240)
    employeenum = Entry(window, width=23, bg='white')
    employeenum.place(x=710, y=240)

    # Search Employee
    search_emp_label = Label(window, text="Search Employee: ",font=('Algerian', 12,), bg="#A9C4FF")
    search_emp_label.place(x=510, y=280)
    search_button = Button(window, bg='red', fg='white', text="SEARCH", font=('Algerian', 9,),command=search)
    search_button.place(x=710, y=280)

    # Department
    dept_label = Label(window, text="Department: ",font=('Algerian', 12,), bg="#A9C4FF")
    dept_label.place(x=510, y=320)
    dept_entry = Entry(window, width=23, bg='white')
    dept_entry.place(x=710, y=320)

    # Basic Income
    heading1 = Label(window, text="BASIC INCOME -------------------------------------------", fg="black", font=("Algerian", 10, "bold"), bg="#A9C4FF")
    heading1.place(x=510, y=360)

    # Rate / hour
    rate_label = Label(window, text="Rate / Hour: ",font=('Algerian', 12,), bg="#A9C4FF")
    rate_label.place(x=510, y=400)
    rate_entry = Entry(window, width=23, bg='white')
    rate_entry.place(x=710, y=400)

    # No. of Hours / Cut Off
    cut_off_label = Label(window, text="No. of Hours / Cut Off: ",font=('Algerian', 9,), bg="#A9C4FF")
    cut_off_label.place(x=510, y=440)
    cut_off_entry = Entry(window, width=23, bg='white')
    cut_off_entry.place(x=710, y=440)

    # Income / Cut Off
    income_label = Label(window, text="Income / Cut Off: ",font=('Algerian', 12,), bg="#A9C4FF")
    income_label.place(x=510, y=480)
    income_entry = Entry(window, width=23, bg='white')
    income_entry.place(x=710, y=480)

    # Honorarium Income
    heading2 = Label(window, text="HONORARIUM INCOME---------------------------------", fg="black", font=("Algerian", 10, "bold"), bg="#A9C4FF")
    heading2.place(x=510, y=520)

    # Rate / hour
    rate1_label = Label(window, text="Rate / Hour: ",font=('Algerian', 12,), bg="#A9C4FF")
    rate1_label.place(x=510, y=560)
    rate1_entry = Entry(window, width=23, bg='white')
    rate1_entry.place(x=710, y=560)

    # No. of Hours / Cut Off
    cut_off1_label = Label(window, text="No. of Hours / Cut Off: ",font=('Algerian', 9,), bg="#A9C4FF")
    cut_off1_label.place(x=510, y=600)
    cut_off1_entry = Entry(window, width=23, bg='white')
    cut_off1_entry.place(x=710, y=600)

    # Income / Cut Off
    income1_label = Label(window, text="Income / Cut Off: ",font=('Algerian', 12,), bg="#A9C4FF")
    income1_label.place(x=510, y=640)
    income1_entry = Entry(window, width=23, bg='white')
    income1_entry.place(x=710, y=640)

    # Other Income
    heading3 = Label(window, text="OTHER INCOME-------------------------------------------", fg="black",font=("Algerian", 10, "bold"), bg="#A9C4FF")
    heading3.place(x=510, y=680)

    # Rate / hour
    rate2_label = Label(window, text="Rate / Hour: ",font=('Algerian', 12,), bg="#A9C4FF")
    rate2_label.place(x=510, y=720)
    rate2_entry = Entry(window, width=23, bg='white')
    rate2_entry.place(x=710, y=720)

    # No. of Hours / Cut Off
    cut_off2_label = Label(window, text="No. of Hours / Cut Off: ",font=('Algerian', 9,), bg="#A9C4FF")
    cut_off2_label.place(x=510, y=760)
    cut_off2_entry = Entry(window, width=23, bg='white')
    cut_off2_entry.place(x=710, y=760)

    # Income / Cut Off
    income2_label = Label(window, text="Income / Cut Off: ",font=('Algerian', 12,), bg="#A9C4FF")
    income2_label.place(x=510, y=800)
    income2_entry = Entry(window, width=23, bg='white')
    income2_entry.place(x=710, y=800)

    # Summary Income
    heading4 = Label(window, text="SUMMARY INCOME--------------------------------------", fg="black", font=("Algerian", 10, "bold"), bg="#A9C4FF")
    heading4.place(x=510, y=840)

    # Gross Income
    gross_label = Label(window, text="Gross Income: ",font=('Algerian', 12,), bg="#A9C4FF")
    gross_label.place(x=510, y=880)
    gross_entry = Entry(window, width=23, bg='white')
    gross_entry.place(x=710, y=880)

    # Income / Cut Off
    net_label = Label(window, text="Net Income: ",font=('Algerian', 12,), bg="#A9C4FF")
    net_label.place(x=510, y=920)
    net_entry = Entry(window, width=23, bg='white')
    net_entry.place(x=710, y=920)

    #-----------------------------------------------------------------------------------------------------------------------

    # First name section
    first_name_label = Label(window, text="First Name",font=('Algerian', 12,), bg="#A9C4FF")
    first_name_label.place(x=930, y=120)
    first_name_entry = Entry(window, width=25, bg='white')
    first_name_entry.place(x=1100, y=120)

    # Middle Name
    middle_name_label = Label(window, text="Middle Name",font=('Algerian', 12,), bg="#A9C4FF")
    middle_name_label.place(x=930, y=160)
    middle_name_entry = Entry(window, width=25, bg='white')
    middle_name_entry.place(x=1100, y=160)

    # Surname
    last_name_label = Label(window, text="Surname",font=('Algerian', 12,), bg="#A9C4FF")
    last_name_label.place(x=930, y=200)
    last_name_entry = Entry(window, width=25, bg='white')
    last_name_entry.place(x=1100, y=200)

    # Civil Status
    civil_status_label = Label(window, text="Civil Status",font=('Algerian', 12,), bg="#A9C4FF")
    civil_status_label.place(x=930, y=240)
    civil_status_entry = Entry(window,width=25, bg="white")
    civil_status_entry.place(x=1100, y=240)

    # Quality Dep. Status
    qualified_label = Label(window, text="Qualified Dep. Status",font=('Algerian', 8,), bg="#A9C4FF")
    qualified_label.place(x=930, y=280)
    qualified_menu = Entry(window,width=25, bg="white")
    qualified_menu.place(x=1100, y=280)

    # Paydate
    paydate_label = Label(window, text="Paydate",font=('Algerian', 12,), bg="#A9C4FF")
    paydate_label.place(x=930, y=320)
    paydate_entry = Entry(window, width=25, bg="white")
    paydate_entry.place(x=1100, y=320)

    # Employee Status
    emp_stat_label = Label(window, text="Employee Status:",font=('Algerian', 10,), bg="#A9C4FF")
    emp_stat_label.place(x=930, y=360)
    emp_stat_entry = Entry(window, width=25, bg='white')
    emp_stat_entry.place(x=1100, y=360)

    # Designation
    designation_label = Label(window, text="Designation",font=('Algerian', 12,), bg="#A9C4FF")
    designation_label.place(x=930, y=400)
    designation_entry = Entry(window, width=25, bg='white')
    designation_entry.place(x=1100, y=400)

    # REGULAR DEDUCTIONS
    heading5 = Label(window, text="REGULAR DEDUCTIONS---------------------", fg="black", font=('Algerian', 12,'bold'), bg="#A9C4FF")
    heading5.place(x=930, y=440)

    # SSS Contribution
    SSS_label = Label(window, text="SSS Contribution:", font=('Algerian', 10,), bg="#A9C4FF")
    SSS_label.place(x=930, y=480)
    SSS_entry = Entry(window, width=25, bg='white')
    SSS_entry.place(x=1100, y=480)

    # Philhealth Contribution
    phil_label = Label(window, text="Philhealth Contribution:", font=('Algerian', 8,), bg="#A9C4FF")
    phil_label.place(x=930, y=520)
    phil_entry = Entry(window, width=25, bg='white')
    phil_entry.place(x=1100, y=520)

    # Pagibig Contribution
    pagibig_label = Label(window, text="Pagibig Contribution:", font=('Algerian', 8,), bg="#A9C4FF")
    pagibig_label.place(x=930, y=560)
    pagibig_entry = Entry(window, width=25, bg='white')
    pagibig_entry.place(x=1100, y=560)

    # Income Tax Contribution
    tax_label = Label(window, text="Income Tax  Contribution:", font=('Algerian', 7,), bg="#A9C4FF")
    tax_label.place(x=930, y=600)
    tax_entry = Entry(window, width=25, bg='white')
    tax_entry.place(x=1100, y=600)

    # OTHER DEDUCTIONS
    heading6 = Label(window, text="OTHER DEDUCTIONS----------------------------------", fg="black", font=("Algerian", 10, "bold"), bg="#A9C4FF")
    heading6.place(x=930, y=640)

    # SSS Loan
    sss_loan_label = Label(window, text="SSS Loan:", font=('Algerian', 12,), bg="#A9C4FF")
    sss_loan_label.place(x=930, y=680)
    sss_loan_entry = Entry(window, width=25, bg='white')
    sss_loan_entry.place(x=1100, y=680)

    # Pagibig Loan
    pagibig_loan_label = Label(window, text="Pagibig Loan:", font=('Algerian', 12,), bg="#A9C4FF")
    pagibig_loan_label.place(x=930, y=710)
    pagibig_loan_entry = Entry(window, width=25, bg='white')
    pagibig_loan_entry.place(x=1100, y=710)

    # Faculty Savings Deposit
    faculty_deposit_label = Label(window, text="Faculty Savings Deposit:", font=('Algerian', 8,), bg="#A9C4FF")
    faculty_deposit_label.place(x=930, y=740)
    faculty_deposit_entry = Entry(window, width=25, bg='white')
    faculty_deposit_entry.place(x=1100, y=740)

    # Faculty Savings Loan
    faculty_loan_label = Label(window, text="Faculty Savings Loan:", font=('Algerian', 8,), bg="#A9C4FF")
    faculty_loan_label.place(x=930, y=770)
    faculty_loan_entry = Entry(window, width=25, bg='white')
    faculty_loan_entry.place(x=1100, y=770)

    # Salary Loan
    salary_loan_label = Label(window, text="Salary Loan:", font=('Algerian', 12,), bg="#A9C4FF")
    salary_loan_label.place(x=930, y=800)
    salary_loan_entry = Entry(window, width=25, bg='white')
    salary_loan_entry.place(x=1100, y=800)

    # Other Loans
    other_loan_label = Label(window, text="Other Loans:", font=('Algerian', 12,), bg="#A9C4FF")
    other_loan_label.place(x=930, y=830)
    other_loan_entry = Entry(window, width=25, bg='white')
    other_loan_entry.place(x=1100, y=830)

    justalabel = Label(window, text="--------------------------------------------------------------------------", font=('Algerian', 10,), bg="#A9C4FF")
    justalabel.place(x=930, y=850)
    # Total Deductions
    total_label = Label(window, text="Total Deductions:", font=('Algerian', 10,), bg="#A9C4FF")
    total_label.place(x=930, y=880)
    total_loan_entry = Entry(window, width=25, bg='white')
    total_loan_entry.place(x=1100, y=880)
    #-----------------------------------------------------------------------------------------------------------------------

    # BUTTONS
    gross_button = Button(window, bg='#0077b6', fg='white', text="GROSS INCOME", font=("Algerian",8),command=grossIncome)
    gross_button.place(x=930, y=920)

    net_button = Button(window, bg='#0077b6', fg='white', text="NET INCOME",font=("Algerian",8),command=netIncome)
    net_button.place(x=1035, y=920)

    save_button = Button(window, bg='#138086', fg='white', text="SAVE",font=("Algerian",8),command=save_command)
    save_button.place(x=1125, y=920)

    update_button = Button(window, bg='#138086', fg='white', text="UPDATE",font=("Algerian",8))
    update_button.place(x=1175, y=920)

    NEW_button = Button(window, bg='orange', fg='black', text="NEW",font=("Algerian",8),command=clear_entries)
    NEW_button.place(x=1245, y=920)

def Payroll(master):
    create_payrollwindow(master)