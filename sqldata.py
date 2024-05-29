from tkinter import *
from tkinter import ttk
import sqlite3
from PIL import Image, ImageTk

def create_sqldata_window(master):


# Fetch data from the database
    def fetch_data(table_name):
        conn = sqlite3.connect('OOPLAB8.db')
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        records = cursor.fetchall()
        conn.close()
        return records

    # Display data in the scrollable frame
    def display_data(scrollable_frame, data, headers, col_widths):
        # Clear the previous contents of the scrollable frame
        for widget in scrollable_frame.winfo_children():
            widget.destroy()

        # Display headers with fixed width
        for col, (header, width) in enumerate(zip(headers, col_widths)):
            header_label = Label(scrollable_frame, text=header, font=('Arial', 8, 'bold'), borderwidth=1, relief="solid", padx=5, pady=5, width=width)
            header_label.grid(row=0, column=col, sticky="nsew")

        # Display data with fixed width
        for row, record in enumerate(data, start=1):
            for col, (value, width) in enumerate(zip(record, col_widths)):
                cell = Label(scrollable_frame, text=value, font=('Arial', 8), borderwidth=1, relief="solid", padx=5, pady=5, width=width)
                cell.grid(row=row, column=col, sticky="nsew")

        # Configure the columns
        for col in range(len(headers)):
            scrollable_frame.grid_columnconfigure(col, weight=1)

    # Main window setup
    root = master
    root.title("User Information Viewer")
    root.geometry("1400x1000")

    # Background image
    bg_image = Image.open("C:\\Users\\Axis\\Desktop\\cell bg.png")
    bg_image = bg_image.resize((1920, 1080))
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = Label(root, image=bg_photo)
    bg_label.image = bg_photo
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    button_frame = Frame(root)
    button_frame.pack(pady=7)

    # Create a canvas and a vertical scrollbar
    canvas = Canvas(root)
    v_scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
    h_scrollbar = ttk.Scrollbar(root, orient="horizontal", command=canvas.xview)
    scrollable_frame = ttk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

    # Pack the canvas and both scrollbars
    canvas.pack(side="top", fill="both", expand=True, padx=20, pady=20)
    v_scrollbar.pack(side="right", fill="y")
    h_scrollbar.pack(side="bottom", fill="x")

    # Button configurations
    fetch_button = Button(button_frame, text="User Information", command=lambda: display_data(scrollable_frame, fetch_data('user_info_tbl'), user_info_headers, user_info_col_widths))
    fetch_button.pack(side=LEFT, padx=5)

    fetchtwo_button = Button(button_frame, text="Employee Registration", command=lambda: display_data(scrollable_frame, fetch_data('employee_registration'), employee_reg_headers, employee_reg_col_widths))
    fetchtwo_button.pack(side=LEFT, padx=5)

    fetchthree_button = Button(button_frame, text="Payroll", command=lambda: display_data(scrollable_frame, fetch_data('payrollseris'), payroll_headers, payroll_col_widths))
    fetchthree_button.pack(side=LEFT, padx=5)

    # Define headers and column widths for each table
    user_info_headers = ["First Name", "Middle Name", "Last Name", "Suffix", "Department", "Designation", "Username", "Password", "Confirm Password", "User Type", "User Status", "Employee No."]
    user_info_col_widths = [12, 12, 12, 8, 15, 15, 15, 15, 15, 10, 12, 13]

    employee_reg_headers = ["First Name", "Middle Name", "Last Name", "Suffix", "Date of Birth", "Gender", "Nationality", "Civil Status", "Department", "Designation",
                   "Quality Dep. Status", "Employee Status", "Paydate", "Employee No.", "Contact No.", "Email", "Social Media", "Social Media No.", "Address 1", "Address 2",
                   "City", "State", "Country", "Zipcode"]
    employee_reg_col_widths = [12, 12, 12, 8, 12, 12, 8, 12, 12, 12, 15, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]

    payroll_headers = ["First Name", "Middle Name", "Last Name", "Civil Status", "Qualified Menu", "Paydate", "Employee Stat", "Designation", "Basic Income", "Honorarium", "Others", "Gross Income", "Net Income", "Total Deduction"]
    payroll_col_widths = [12, 12, 12, 8, 15, 15, 15, 15, 15, 10, 12, 13, 10, 12]

def SQLData(master):
    create_sqldata_window(master)
