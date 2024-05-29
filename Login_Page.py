import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import lab_b
import lab_c
import lab_d
import sqldata

class LoginSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("Login System")
        self.master.configure(bg="light blue")
        self.master.geometry("700x600")
        self.frame = tk.Frame(master=self.master, bg="light blue")
        self.frame.place(relx=0.5, rely=0.5, anchor="center")  # Placing the frame in the center

        self.create_widgets()

    def create_widgets(self):
        self.create_label()
        self.create_entry_username()
        self.create_entry_password()
        self.create_button_login()
        self.create_checkbox_remember()

    def create_label(self):
        self.label = tk.Label(
            master=self.frame, text="Login System", font=("Times New Roman bold", 50), bg="light blue", fg="black"
        )
        self.label.grid(row=0, column=0, columnspan=2, pady=20)

    def create_entry_username(self):
        self.username = tk.StringVar()
        tk.Label(self.frame, text="Username:", font=("Times New Roman", 18), bg="light blue", fg="black").grid(row=1, column=0, sticky="e")
        self.entry_username = tk.Entry(
            master=self.frame, textvariable=self.username, width=30, font=("Times New Roman", 18)
        )
        self.entry_username.grid(row=1, column=1, padx=10, pady=10, sticky="w")

    def create_entry_password(self):
        self.password = tk.StringVar()
        tk.Label(self.frame, text="Password:", font=("Times New Roman", 18), bg="light blue", fg="black").grid(row=2, column=0, sticky="e")
        self.entry_password = tk.Entry(
            master=self.frame,
            textvariable=self.password,
            width=30,
            font=("Times New Roman", 18),
            show="*",
        )
        self.entry_password.grid(row=2, column=1, padx=10, pady=10, sticky="w")

    def create_button_login(self):
        self.button = tk.Button(master=self.frame, text="Login", command=self.handle_login, font=("Arial", 18))
        self.button.grid(row=3, column=1, pady=20)

    def create_checkbox_remember(self):
        self.remember_me = tk.BooleanVar()
        self.checkbox_remember_me = tk.Checkbutton(
            master=self.frame, text="Remember Me", variable=self.remember_me, font=("Times New Roman", 18), bg="light blue", fg="black"
        )
        self.checkbox_remember_me.grid(row=4, column=1, pady=10)

    def handle_login(self):
        username = self.username.get()
        password = self.password.get()

        if not username:
            messagebox.showwarning("Login Failed", "Please enter a username.")
            return

        if not password:
            messagebox.showwarning("Login Failed", "Please enter a password.")
            return

        # Define credentials for employee info and payroll systems
        employee_info_credentials = {'username': '1', 'password': '1'}
        payroll_credentials = {'username': '2', 'password': '2'}
        user_credentials = {'username': '3', 'password': '3'}
        admin_credentials = {'username': 'admin', 'password': 'admin'}

        if username == employee_info_credentials['username'] and password == employee_info_credentials['password']:
            self.open_employee_info()
        elif username == payroll_credentials['username'] and password == payroll_credentials['password']:
            self.open_payroll()
        elif username == user_credentials['username'] and password == user_credentials['password']:
            self.open_user()
        elif username == admin_credentials['username'] and password == admin_credentials['password']:
            self.admin()
        else:
            messagebox.showwarning("Login Failed", "Invalid username or password.")

    def open_employee_info(self):
        self.master.withdraw()  # Hide the login window
        employee_info_window = tk.Toplevel(self.master)
        lab_b.EmployeeInfo(employee_info_window)

    def open_payroll(self):
        self.master.withdraw()  # Hide the login window
        payroll_window = tk.Toplevel(self.master)
        lab_c.Payroll(payroll_window)

    def open_user(self):
        self.master.withdraw()  # Hide the login window
        user_window = tk.Toplevel(self.master)
        lab_d.User(user_window)

    def admin(self):
        self.master.withdraw()  # Hide the login window
        admin = tk.Toplevel(self.master)
        self.admin_window(admin)

    def sqldatawindow(self):
        self.master.withdraw()  # Hide the login window
        sql_window1 = tk.Toplevel(self.master)
        sqldata.SQLData(sql_window1)


    def admin_window(self, window):
        window.title("ADMIN")
        window.geometry("1920x1080")

        bg_image = Image.open("C:\\Users\\Axis\\PycharmProjects\\OOP FINALS LAB 8\\pics\\ADAMSONBG.png")
        bg_image = bg_image.resize((1950, 1100))
        bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = tk.Label(window, image=bg_photo)
        bg_label.image = bg_photo
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        #window creator

        main_frame = tk.Frame(window)
        main_frame.place(relx=0.25, rely=0.50, anchor="center")

        employee_button = ttk.Button(main_frame, text="emp", command= self.open_employee_info)
        employee_button.grid(row=0, column=0, padx=5, pady=5)

        payroll_button = ttk.Button(main_frame, text="payroll", command= self.open_payroll)
        payroll_button.grid(row=0, column=1, padx=5, pady=5)

        user_button = ttk.Button(main_frame, text="user", command=self.open_user)
        user_button.grid(row=0, column=2, padx=5, pady=5)

        sql_button = ttk.Button(main_frame, text="SQL Data", command=self.sqldatawindow)
        sql_button.grid(row=0, column=3, padx=5, pady=5)


root = tk.Tk()
app = LoginSystem(root)
root.mainloop()