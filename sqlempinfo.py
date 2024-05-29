import sqlite3
from tkinter import *
from tkinter import ttk

def create_sql2_window(master):

    def fetch_data():
        # Connect to SQLite database
        conn = sqlite3.connect('OOPLAB8.db')
        cursor = conn.cursor()

        # Execute the query to fetch data
        cursor.execute("SELECT * FROM employee_registration")
        records = cursor.fetchall()

        # Close the database connection
        conn.close()

        # Clear the previous contents of the Treeview
        for row in tree.get_children():
            tree.delete(row)

        # Insert new data into the Treeview
        for record in records:
            tree.insert("", "end", values=record)


    # Create the main window
    window = master
    window.title("Employee Data Viewer")
    window.geometry("1200x600")  # Adjusted window size

    # Create a frame for the button
    button_frame = Frame(window)
    button_frame.pack(pady=20)

    # Add a button to fetch and display data
    fetch_button = Button(button_frame, text="Fetch Data", command=fetch_data)
    fetch_button.pack()

    # Create a frame for the Treeview and scrollbar
    tree_frame = Frame(window)
    tree_frame.pack(pady=20)

    # Add a horizontal scrollbar to the frame
    scrollbar = Scrollbar(tree_frame, orient=HORIZONTAL)
    scrollbar.pack(side=BOTTOM, fill=X)

    # Create a Treeview to display data in a table format
    tree = ttk.Treeview(tree_frame, columns=("firstname", "middlename", "lastname", "suffix", "bday", "gender", "nationality", "civilstat", "department", "designation", "qualitydepstat", "empstatus", "paydate", "employeenum", "contactno", "email", "socmed", "socmedno", "address1", "address2", "city", "state", "country", "zipcode"),
                        show='headings', xscrollcommand=scrollbar.set)

    # Configure the scrollbar
    scrollbar.config(command=tree.xview)

    # Define headings
    tree.heading("firstname", text="First Name")
    tree.heading("middlename", text="Middle Name")
    tree.heading("lastname", text="Last Name")
    tree.heading("suffix", text="Suffix")
    tree.heading("bday", text="Birthday")
    tree.heading("gender", text="Gender")
    tree.heading("nationality", text="Nationality")
    tree.heading("civilstat", text="Civil Status")
    tree.heading("department", text="Department")
    tree.heading("designation", text="Designation")
    tree.heading("qualitydepstat", text="Quality Dep. Status")
    tree.heading("empstatus", text="Employee Status")
    tree.heading("paydate", text="Paydate")
    tree.heading("employeenum", text="Employee Number")
    tree.heading("contactno", text="Contact No.")
    tree.heading("email", text="Email")
    tree.heading("socmed", text="Social Media")
    tree.heading("socmedno", text="Social Media No.")
    tree.heading("address1", text="Address 1")
    tree.heading("address2", text="Address 2")
    tree.heading("city", text="City")
    tree.heading("state", text="State")
    tree.heading("country", text="Country")
    tree.heading("zipcode", text="Zipcode")

    # Adjust column widths
    for col in tree["columns"]:
        tree.column(col, width=140, anchor=CENTER)

    tree.pack()


def SQLEmpInfo(master):
    create_sql2_window(master)

