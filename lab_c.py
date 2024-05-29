from tkinter import *
import sqlite3

def create_payroll_window(master):


    def selected_civil_status(choice):
        print("Selected Civil Status: " + choice)


    def selected_quality(choice):
        print("Selected Quality Dep. Status: " + choice)


    def selected_paydate(choice):
        print("Selected Paydate: " + choice)

    def search():

        con = sqlite3.connect("OOPLAB8.db")
        cur = con.cursor()
        cur.execute(f"SELECT * FROM employee_registration WHERE employeenum = '{emp_no_entry.get()}'")

        info = cur.fetchone()
        print(info)

        first_name_entry.delete(0, "end")
        first_name_entry.insert(0, info[0])

        middle_name_entry.delete(0, "end")
        middle_name_entry.insert(0, info[1])

        last_name_entry.delete(0, "end")
        last_name_entry.insert(0, info[2])

        dept_entry.delete(0, "end")
        dept_entry.insert(0, info[8])

        civil_status_entry.delete(0, "end")
        civil_status_entry.insert(0, info[7])

        qualified_menu.delete(0, "end")
        qualified_menu.insert(0, info[10])

        paydate_entry.delete(0, "end")
        paydate_entry.insert(0, info[12])

        emp_stat_entry.delete(0, "end")
        emp_stat_entry.insert(0, info[11])

        designation_entry.delete(0, "end")
        designation_entry.insert(0, info[9])


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


    import sqlite3


    def save_command():
        # Connect to SQLite database
        conn = sqlite3.connect('OOPLAB8.db')  # Changed from .py to .db
        cursor = conn.cursor()

        # Create table if it does not exist
        create_table_query = '''CREATE TABLE IF NOT EXISTS payrollseris (
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
            first_name_entry, middle_name_entry, last_name_entry, civil_status_entry,
            qualified_menu, paydate_entry, emp_stat_entry, designation_entry,
            basic_income, honorarium_income, other_income, gross_income, net_entry, total_deduction
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
        cursor.execute(insert_query, data)

        # Commit changes and close the connection
        conn.commit()
        conn.close()

        # Print confirmation message
        print("UPLOADED")

        # Clear the entries (Optional)
        entries = [first_name_entry, middle_name_entry, last_name_entry, civil_status_entry, qualified_menu, paydate_entry,
                   emp_stat_entry, designation_entry, dept_entry,
                   income_entry, income1_entry, income2_entry, gross_entry, net_entry, total_loan_entry]
        for entry in entries:
            entry.delete(0, 'end')

    window = master

    window.title("SE-RI'S CHOICE PAYROLL")

    window.geometry("1337x780")

    button_frame = Frame(window)
    button_frame.pack()

    window.configure(bg="white")  # Set background color

    cf = Frame(window, width=800, height=1500, bg='#e9eaed')
    cf.place(x=330, y=50)

    cf = Frame(window, width=100, height=100, bg='black')
    cf.place(x=350, y=90)


    # heading
    heading = Label(window, text="SE-RI'S CHOICE PAYROLL", bg="#e9eaed", fg="black", font=("Georgia", 20, "bold"))
    heading.place(relx=0.55, rely=0.06, anchor=CENTER)

    # employee basic info
    heading1 = Label(window, text="EMPLOYEE BASIC INFO:", fg="black", font=("Arial", 10, "bold"), bg="#e9eaed")
    heading1.place(relx=0.25, rely=0.08)

    # Employee Number
    emp_no_label = Label(window, text="Employee Number: ", bg="#e9eaed")
    emp_no_label.place(relx=0.26, rely=0.32)
    emp_no_entry = Entry(window, width=25, bg='white')
    emp_no_entry.place(relx=0.37, rely=0.32)

    # Search Employee
    search_emp_label = Label(window, text=" Search Employee: ", bg="#e9eaed")
    search_emp_label.place(relx=0.26, rely=0.36)
    search_button = Button(window, bg='red', fg='white', text="SEARCH", command=search)
    search_button.place(relx=0.37, rely=0.36)

    # Department
    dept_label = Label(window, text="Department: ", bg="#e9eaed")
    dept_label.place(relx=0.26, rely=0.40)
    dept_entry = Entry(window, width=25, bg='white')
    dept_entry.place(relx=0.37, rely=0.40)

    # Basic Income
    heading1 = Label(window, text="BASIC INCOME:", fg="black", font=("Arial", 10, "bold"), bg="#e9eaed")
    heading1.place(relx=0.25, rely=0.43)

    # Rate / hour
    rate_label = Label(window, text="Rate / Hour: ", bg="#e9eaed")
    rate_label.place(relx=0.26, rely=0.46)
    rate_entry = Entry(window, width=25, bg='white')
    rate_entry.place(relx=0.37, rely=0.46)

    # No. of Hours / Cut Off
    cut_off_label = Label(window, text="No. of Hours / Cut Off: ", bg="#e9eaed")
    cut_off_label.place(relx=0.26, rely=0.50)
    cut_off_entry = Entry(window, width=25, bg='white')
    cut_off_entry.place(relx=0.37, rely=0.50)

    # Income / Cut Off
    income_label = Label(window, text="Income / Cut Off: ", bg="#e9eaed")
    income_label.place(relx=0.26, rely=0.54)
    income_entry = Entry(window, width=25, bg='white')
    income_entry.place(relx=0.37, rely=0.54)

    # Honorarium Income
    heading2 = Label(window, text="HONORARIUM INCOME:", fg="black", font=("Arial", 10, "bold"), bg="#e9eaed")
    heading2.place(relx=0.25, rely=0.57)

    # Rate / hour
    rate1_label = Label(window, text="Rate / Hour: ", bg="#e9eaed")
    rate1_label.place(relx=0.26, rely=0.60)
    rate1_entry = Entry(window, width=25, bg='white')
    rate1_entry.place(relx=0.37, rely=0.60)

    # No. of Hours / Cut Off
    cut_off1_label = Label(window, text="No. of Hours / Cut Off: ", bg="#e9eaed")
    cut_off1_label.place(relx=0.26, rely=0.64)

    cut_off1_entry = Entry(window, width=25, bg='white')
    cut_off1_entry.place(relx=0.37, rely=0.64)

    # Income / Cut Off
    income1_label = Label(window, text="Income / Cut Off: ", bg="#e9eaed")
    income1_label.place(relx=0.26, rely=0.68)

    income1_entry = Entry(window, width=25, bg='white')
    income1_entry.place(relx=0.37, rely=0.68)

    # Other Income
    heading3 = Label(window, text="OTHER INCOME:", fg="black", font=("Arial", 10, "bold"), bg="#e9eaed")
    heading3.place(relx=0.25, rely=0.71)

    # Rate / hour
    rate2_label = Label(window, text="Rate / Hour: ", bg="#e9eaed")
    rate2_label.place(relx=0.26, rely=0.74)

    rate2_entry = Entry(window, width=25, bg='white')
    rate2_entry.place(relx=0.37, rely=0.74)

    # No. of Hours / Cut Off
    cut_off2_label = Label(window, text="No. of Hours / Cut Off: ", bg="#e9eaed")
    cut_off2_label.place(relx=0.26, rely=0.78)

    cut_off2_entry = Entry(window, width=25, bg='white')
    cut_off2_entry.place(relx=0.37, rely=0.78)

    # Income / Cut Off
    income2_label = Label(window, text="Income / Cut Off: ", bg="#e9eaed")
    income2_label.place(relx=0.26, rely=0.82)

    income2_entry = Entry(window, width=25, bg='white')
    income2_entry.place(relx=0.37, rely=0.82)

    # Summary Income
    heading4 = Label(window, text="SUMMARY INCOME:", fg="black", font=("Arial", 10, "bold"), bg="#e9eaed")
    heading4.place(relx=0.25, rely=0.85)

    # Gross Income
    gross_label = Label(window, text="Gross Income: ", bg="#e9eaed")
    gross_label.place(relx=0.26, rely=0.88)

    gross_entry = Entry(window, width=25, bg='white')
    gross_entry.place(relx=0.37, rely=0.88)

    # Income / Cut Off
    net_label = Label(window, text="NET INCOME: ", bg="#e9eaed")
    net_label.place(relx=0.26, rely=0.92)

    net_entry = Entry(window, width=25, bg='white')
    net_entry.place(relx=0.37, rely=0.92)

    # First name section
    first_name_label = Label(window, text="First Name", bg="#e9eaed")
    first_name_label.place(relx=0.51, rely=0.10)

    first_name_entry = Entry(window, width=25, bg='white')
    first_name_entry.place(relx=0.62, rely=0.10)

    # Middle Name
    middle_name_label = Label(window, text="Middle Name", bg="#e9eaed")
    middle_name_label.place(relx=0.51, rely=0.13)

    middle_name_entry = Entry(window, width=25, bg='white')
    middle_name_entry.place(relx=0.62, rely=0.13)

    # Surname
    last_name_label = Label(window, text="Surname", bg="#e9eaed")
    last_name_label.place(relx=0.51, rely=0.16)

    last_name_entry = Entry(window, width=25, bg='white')
    last_name_entry.place(relx=0.62, rely=0.16)

    # Civil Status
    civil_status_label = Label(window, text="Civil Status", bg="#e9eaed")
    civil_status_label.place(relx=0.51, rely=0.20)

    civil_status_entry = Entry(window, bg="white")
    civil_status_entry.place(relx=0.62, rely=0.20)
    civil_status_entry.config(width=25)

    # Quality Dep. Status
    qualified_label = Label(window, text="Qualified Dep. Status", bg="#e9eaed")
    qualified_label.place(relx=0.51, rely=0.24)

    qualified_menu = Entry(window, bg="white")
    qualified_menu.place(relx=0.62, rely=0.24)
    qualified_menu.config(width=25)

    # Paydate
    paydate_label = Label(window, text="Paydate", bg="#e9eaed")
    paydate_label.place(relx=0.51, rely=0.28)
    paydate_entry = Entry(window, width=25, bg="white")
    paydate_entry.place(relx=0.62, rely=0.28)

    # Employee Status
    emp_stat_label = Label(window, text="Employee Status:", bg="#e9eaed")
    emp_stat_label.place(relx=0.51, rely=0.33)

    emp_stat_entry = Entry(window, width=25, bg='white')
    emp_stat_entry.place(relx=0.62, rely=0.33)

    # Designation
    designation_label = Label(window, text="Designation", bg="#e9eaed")
    designation_label.place(relx=0.51, rely=0.36)

    designation_entry = Entry(window, width=25, bg='white')
    designation_entry.place(relx=0.62, rely=0.36)

    # REGULAR DEDUCTIONS
    heading5 = Label(window, text="REGULAR DEDUCTIONS", fg="black", font=("Arial", 10, "bold"), bg="#e9eaed")
    heading5.place(relx=0.50, rely=0.40)

    # SSS Contribution
    SSS_label = Label(window, text="SSS Contribution:", bg="#e9eaed")
    SSS_label.place(relx=0.51, rely=0.44)

    SSS_entry = Entry(window, width=25, bg='white')
    SSS_entry.place(relx=0.62, rely=0.44)

    # Philhealth Contribution
    phil_label = Label(window, text="Philhealth Contribution:", bg="#e9eaed")
    phil_label.place(relx=0.51, rely=0.47)

    phil_entry = Entry(window, width=25, bg='white')
    phil_entry.place(relx=0.62, rely=0.47)

    # Pagibig Contribution
    pagibig_label = Label(window, text="Pagibig Contribution:", bg="#e9eaed")
    pagibig_label.place(relx=0.51, rely=0.50)

    pagibig_entry = Entry(window, width=25, bg='white')
    pagibig_entry.place(relx=0.62, rely=0.50)

    # Income Tax Contribution
    tax_label = Label(window, text="Income Tax  Contribution:", bg="#e9eaed")
    tax_label.place(relx=0.51, rely=0.53)

    tax_entry = Entry(window, width=25, bg='white')
    tax_entry.place(relx=0.62, rely=0.53)

    # OTHER DEDUCTIONS
    heading6 = Label(window, text="OTHER DEDUCTIONS", fg="black", font=("Arial", 10, "bold"), bg="#e9eaed")
    heading6.place(relx=0.50, rely=0.58)

    # SSS Loan
    sss_loan_label = Label(window, text="SSS Loan:", bg="#e9eaed")
    sss_loan_label.place(relx=0.51, rely=0.62)

    sss_loan_entry = Entry(window, width=25, bg='white')
    sss_loan_entry.place(relx=0.62, rely=0.62)

    # Pagibig Loan
    pagibig_loan_label = Label(window, text="Pagibig Loan:", bg="#e9eaed")
    pagibig_loan_label.place(relx=0.51, rely=0.65)

    pagibig_loan_entry = Entry(window, width=25, bg='white')
    pagibig_loan_entry.place(relx=0.62, rely=0.65)

    # Faculty Savings Deposit
    faculty_deposit_label = Label(window, text="Faculty Savings Deposit:", bg="#e9eaed")
    faculty_deposit_label.place(relx=0.51, rely=0.68)

    faculty_deposit_entry = Entry(window, width=25, bg='white')
    faculty_deposit_entry.place(relx=0.62, rely=0.68)

    # Faculty Savings Loan
    faculty_loan_label = Label(window, text="Faculty Savings Loan:", bg="#e9eaed")
    faculty_loan_label.place(relx=0.51, rely=0.71)

    faculty_loan_entry = Entry(window, width=25, bg='white')
    faculty_loan_entry.place(relx=0.62, rely=0.71)

    # Salary Loan
    salary_loan_label = Label(window, text="Salary Loan:", bg="#e9eaed")
    salary_loan_label.place(relx=0.51, rely=0.74)

    salary_loan_entry = Entry(window, width=25, bg='white')
    salary_loan_entry.place(relx=0.62, rely=0.74)

    # Other Loans
    other_loan_label = Label(window, text="Other Loans:", bg="#e9eaed")
    other_loan_label.place(relx=0.51, rely=0.78)

    other_loan_entry = Entry(window, width=25, bg='white')
    other_loan_entry.place(relx=0.62, rely=0.78)

    # DEDUCTIONS SUMMARY
    heading7 = Label(window, text="DEDUCTIONS SUMMARY", fg="black", font=("Arial", 10, "bold"), bg="#e9eaed")
    heading7.place(relx=0.50, rely=0.83)

    # Total Deductions
    total_label = Label(window, text="Total Deductions:", bg="#e9eaed")
    total_label.place(relx=0.51, rely=0.87)

    total_loan_entry = Entry(window, width=25, bg='white')
    total_loan_entry.place(relx=0.62, rely=0.87)

    # BUTTONS
    gross_button = Button(window, bg='#0077b6', fg='white', text="GROSS INCOME", command=grossIncome)
    gross_button.place(relx=0.50, rely=0.91)

    net_button = Button(window, bg='#0077b6', fg='white', text="NET INCOME", command=netIncome)
    net_button.place(relx=0.587, rely=0.91)

    save_button = Button(window, bg='#138086', fg='white', text="SAVE", command=save_command)
    save_button.place(relx=0.66, rely=0.91)

    update_button = Button(window, bg='#138086', fg='white', text="UPDATE")
    update_button.place(relx=0.70, rely=0.91)

    NEW_button = Button(window, bg='orange', fg='black', text="NEW")
    NEW_button.place(relx=0.75, rely=0.91)

def Payroll(master):
    create_payroll_window(master)