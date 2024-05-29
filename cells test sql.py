import tkinter as tk
from tkinter import ttk
import sqlite3

def fetch_data():
    conn = sqlite3.connect('OOPLAB8.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user_info_tbl")
    records = cursor.fetchall()
    conn.close()
    return records

def display_data(scrollable_frame):
    # Clear the previous contents of the scrollable frame
    for widget in scrollable_frame.winfo_children():
        widget.destroy()

    data = fetch_data()

    # Define the headers and set the width
    headers = ["First Name", "Middle Name", "Last Name", "Suffix", "Department", "Designation", "Username", "Password", "Confirm Password", "User Type", "User Status", "Employee No."]
    col_widths = [12, 12, 12, 8, 15, 15, 15, 15, 15, 10, 12, 13]  # Adjust the column widths here

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

    fetch_button = tk.Button(button_frame, text="User Information", command=lambda: display_data(scrollable_frame))
    fetch_button.pack()

    # Create a canvas and a scrollbar
    canvas = tk.Canvas(root)
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Pack the canvas and scrollbar
    canvas.pack(side="left", fill="both", expand=True, padx=20, pady=1)
    scrollbar.pack(side="right", fill="y")

    root.mainloop()

if __name__ == "__main__":
    create_main_window()
