import sqlite3
from tkinter import *
from tkinter import ttk

def create_sql3_window(master):

    def fetch_data():
        # Connect to SQLite database
        conn = sqlite3.connect('OOPLAB8.db')
        cursor = conn.cursor()

        # Execute the query to fetch data
        cursor.execute("SELECT * FROM user_info_tbl")
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
    window.title("Payroll Data Viewer")
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
    tree = ttk.Treeview(tree_frame, columns=("first_name", "middle_name", "last_name", "suffix", "department", "designation", "username", "password", "confirm_password", "usertype", "userstatus", "employeenum"),
                        show='headings', xscrollcommand=scrollbar.set)

    # Configure the scrollbar
    scrollbar.config(command=tree.xview)

    # Define headings
    tree.heading("first_name", text="First Name")
    tree.heading("middle_name", text="Middle Name")
    tree.heading("last_name", text="Last Name")
    tree.heading("suffix", text="Suffix")
    tree.heading("department", text="Department")
    tree.heading("designation", text="Designation")
    tree.heading("username", text="Username")
    tree.heading("password", text="Password")
    tree.heading("confirm_password", text="Confirm Password")
    tree.heading("usertype", text="User Type")
    tree.heading("userstatus", text="User Status")
    tree.heading("employeenum", text="Employee No.")

    # Adjust column widths
    for col in tree["columns"]:
        tree.column(col, width=100, anchor=CENTER)

    tree.pack()

def SQLUserReg(master):
    create_sql3_window(master)
