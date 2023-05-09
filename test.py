#Write code to define a side menu using tkinter for an application. The side menu should have the following options:
#1. Home
#2. About
#3. Contact
#4. Exit

#This side menu must have a height equal to the application

from tkinter import *
from customtkinter import *

set_appearance_mode("dark")  # Modes: system (default), light, dark
set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

root=CTk()
root.geometry("1920x1080")
root.title("Side Menu")

def home():
    print("Home")

def about():
    print("About")

def contact():
    print("Contact")

def exit():
    print("Exit")

canvas_default = CTkCanvas(root,bg = "Green",height = 1080,width = 300)

label = CTkLabel(master=canvas_default,text="Home",fg_color='black', width=120,height=25).grid(row=0,column=1)

label = CTkLabel(master=canvas_default,text="About",fg_color='black', width=120,height=25).grid(row=1,column=1)

label = CTkLabel(master=canvas_default,text="Contact",fg_color='black', width=120,height=25).grid(row=2,column=1)

label = CTkLabel(master=canvas_default,text="Exit",fg_color='black', width=120,height=25).grid(row=3,column=1)

canvas_default.grid(row=0,column=0,padx=20)

root.mainloop()

