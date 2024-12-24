from tkinter import messagebox

from customtkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
def login():
 if usernameEntry.get() == '' or passwordEntry.get()=='':
      messagebox.showerror('Error','All fields Are Empty')
 elif usernameEntry.get()=='shriyansh' and passwordEntry.get()=='1234':
      messagebox.showinfo('success','Login is successfull');
      root.destroy()

      import ems
 else:
     messagebox.showerror('Error','Wrong credential')

root=CTk()
root.geometry('930x478')
root.resizable(0,0)
root.title('login page')
image=CTkImage(Image.open('cover.jpg'),size=(930,478))
imageLabel=CTkLabel(root,image=image,text='')
imageLabel.place(x=0,y=0)
headinglabel=CTkLabel(root,text='Employee Management System',bg_color='#FFF0CF',font=('Goudy Old Style',25,'bold'),text_color='navy',corner_radius=50)
headinglabel.place(x=280,y=110)
usernameEntry=CTkEntry(root,placeholder_text='Enter Your Username',width=180,corner_radius=20,bg_color='#FFF0CF',text_color="white", font=("tahoma",15))
usernameEntry.place(x=365,y=150)
passwordEntry=CTkEntry(root,placeholder_text='Enter Your Password',width=180,show='*',corner_radius=20,bg_color='#FFF0CF',text_color="white", font=("tahoma",15))
passwordEntry.place(x=365,y=190)
loginButton=CTkButton(root,text='Login',bg_color='#fff0cf',cursor='hand2',command=login,corner_radius=20)
loginButton.place(x=385,y=230)
root.mainloop()
