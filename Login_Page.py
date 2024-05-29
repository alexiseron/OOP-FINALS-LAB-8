import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import lab_b  # Assuming these are your custom modules
import lab_c
import lab_d
import sqldata


class LoginSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("Login System")
        self.master.geometry("1920x1080")
        self.master.state("zoomed")

        # Load and set the background image
        self.image = Image.open("C:\\Users\\Axis\\Desktop\\SERILOGIN.jpg")
        self.tk_image = ImageTk.PhotoImage(self.image)
        self.image_label = tk.Label(master, image=self.tk_image)
        self.image_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.create_widgets()

    def create_widgets(self):
        self.create_entry_username()
        self.create_entry_password()
        self.create_button_login()

    def create_entry_username(self):
        self.username = tk.StringVar()
        tk.Label(self.master, text="USERNAME:", bg="#CADDFF", fg="black", font=('Impact', 20, 'bold'), width=10,
                 highlightbackground='black', highlightthickness=2) \
            .place(x=1100, y=330)
        self.entry_username = tk.Entry(self.master, textvariable=self.username, width=20, bg="#FFFFFF",
                                       highlightbackground='black', highlightthickness=2, font=('Impact', 20, 'bold'))
        self.entry_username.place(x=1300, y=330)

    def create_entry_password(self):
        self.password = tk.StringVar()
        tk.Label(self.master, text="PASSWORD:", bg="#CADDFF", fg="black", font=('Impact', 20, 'bold'), width=10,
                 highlightbackground='black', highlightthickness=2) \
            .place(x=1100, y=430)
        self.entry_password = tk.Entry(self.master, textvariable=self.password, width=20, bg="#FFFFFF",
                                       highlightbackground='black', highlightthickness=2, font=('Impact', 20, 'bold'),
                                       show="*")
        self.entry_password.place(x=1300, y=430)

    def create_button_login(self):
        self.button = tk.Button(self.master, text="Login", command=self.handle_login, bg="black", fg="white", border=2,
                                highlightbackground='#a2f6c9', highlightthickness=3, font=('Impact', 20), width=20)
        self.button.place(x=1225, y=550)

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

    def sqldata(self):
        self.master.withdraw()  # Hide the login window
        sql_window1 = tk.Toplevel(self.master)
        sqldata.SQLData(sql_window1)

    def admin_window(self, window):
        window.title("ADMIN")
        window.geometry("1920x1080")
        window.title("SERIS INFORMATION SYSTEM (ADMIN)")

        bg_image = Image.open("C:\\Users\\Axis\\Desktop\\SERIADMIN.jpg")
        bg_image = bg_image.resize((1920, 1080))
        bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = tk.Label(window, image=bg_photo)
        bg_label.image = bg_photo
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)


        employee_button = tk.Button(window, text="EMPLOYEE PAGE", font=("Impact",20,"bold"),bg="white", fg="black", border='2',highlightbackground='black', highlightthickness='2',  command=self.open_employee_info)
        employee_button.place(x=1500,y=400)

        payroll_button = tk.Button(window, text="PAYROLL PAGE",font=("Impact",20,"bold"),bg="white", fg="black", border='2',highlightbackground='black', highlightthickness='2', command=self.open_payroll)
        payroll_button.place(x=1500,y=540)

        user_button = tk.Button(window, text="USER PAGE",font=("Impact",20,"bold"),bg="white", fg="black", border='2',highlightbackground='black', highlightthickness='2' ,command=self.open_user)
        user_button.place(x=1500,y=660)

        payrollsql_button = tk.Button(window, text="PAYROLL DATA",font=("Impact",20,"bold"),bg="white", fg="black", border='2',highlightbackground='black', highlightthickness='2' ,command=self.sqldata)
        payrollsql_button.place(x=1500,y=790)

# Example usage
root = tk.Tk()
app = LoginSystem(root)
root.mainloop()
