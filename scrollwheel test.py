import tkinter as tk
from tkinter import ttk
import sqlite3

def fetch_dataemp():
    conn = sqlite3.connect('OOPLAB8.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employee_registration")
    records = cursor.fetchall()
    conn.close()
    return records

def display_dataemp(scrollable_frame):
    # Clear the previous contents of the scrollable frame
    for widget in scrollable_frame.winfo_children():
        widget.destroy()

    data = fetch_dataemp()

    # Define the headers and set the width
    headers = ["First Name", "Middle Name", "Last Name", "Suffix", "Date of Birth", "Gender", "Nationality", "Civil Status", "Department", "Designation",
               "Quality Dep. Status", "Employee Status", "Paydate", "Employee No.", "Contact No.", "Email", "Social Media", "Social Media No.", "Address 1", "Address 2",
               "City", "State", "Country", "Zipcode"]
    col_widths = [12, 12, 12, 8, 12, 12, 8, 12, 12, 12, 15, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]  # Adjust the column widths here

    # Display headers with fixed width
    for col, (header, width) in enumerate(zip(headers, col_widths)):
        header_label = tk.Label(scrollable_frame, text=header, font=('Arial', 8, 'bold'), borderwidth=1, relief="solid", padx=5, pady=5, width=width)
        header_label.grid(row=0, column=col, sticky="nsew")

    # Display data with fixed width
    for row, record in enumerate(data, start=1):
        for col, (value, width) in enumerate(zip(record, col_widths)):
            cell = tk.Label(scrollable_frame, text=value, font=('Arial', 8), borderwidth=1, relief="solid", padx=5, pady=5, width=width)
            cell.grid(row=row, column=col, sticky="nsew")

    # Configure the columns
    for col in range(len(headers)):
        scrollable_frame.grid_columnconfigure(col, weight=1)

def create_main_window():
    root = tk.Tk()
    root.title("User Information Viewer")
    root.geometry("1400x1000")

    button_frame = tk.Frame(root)
    button_frame.pack(pady=7)

    fetch_button = tk.Button(button_frame, text="User Information", command=lambda: display_dataemp(scrollable_frame))
    fetch_button.pack(side=tk.LEFT, padx=5)

    fetchtwo_button = tk.Button(button_frame, text="Employee Registration", command=lambda: display_dataemp(scrollable_frame))
    fetchtwo_button.pack(side=tk.LEFT, padx=5)

    # Create a canvas and a vertical scrollbar
    canvas = tk.Canvas(root)
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

    root.mainloop()

if __name__ == "__main__":
    create_main_window()
