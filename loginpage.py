import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.geometry('1920x1080')
window.title("Login Page")
window.state("zoomed")

image = Image.open("C:\\Users\\Axis\\Desktop\\A.png")
tk_image = ImageTk.PhotoImage(image)
image_label = tk.Label(window, image=tk_image)
image_label.place(x=0, y=0, relwidth=1, relheight=1)


tk.Label(window,text="USERNAME:", bg="#CADDFF", fg="black" ,font=('Impact', 20, 'bold'),width=10,highlightbackground='black', highlightthickness='2')\
.place(x=1100,y=330)
username = tk.Entry(window,width='20', bg="#FFFFFF", highlightbackground='black', highlightthickness='2',font=('Impact', 20, 'bold'))
username.place(x=1300,y=330)

tk.Label(window,text="PASSWORD:", bg="#CADDFF", fg="black" ,font=('Impact', 20, 'bold'),width=10,highlightbackground='black', highlightthickness='2')\
.place(x=1100,y=430)
password = tk.Entry(window,width='20', bg="#FFFFFF", highlightbackground='black', highlightthickness='2',font=('Impact', 20, 'bold'), show="*")
password.place(x=1300,y=430)

login_button = tk.Button(window,width='20',text="Login", bg="black", fg="white",border='2', highlightbackground='#a2f6c9', highlightthickness='3', font=('Impact',20,))
login_button.place(x=1225,y=550)

window.mainloop()