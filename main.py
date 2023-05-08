from PIL import ImageTk, Image
from tkinter import PhotoImage
from customtkinter import *

set_appearance_mode("dark")  # Modes: system (default), light, dark
set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

root=CTk()
root.geometry("1920x1080")
frame = CTkFrame(master=root)
canvas_default = CTkCanvas(frame,bg = "Grey",height = "1920",width = 300)

img = Image.open("owl.jpg")
picimg=img.resize((100,100))
tkimg = ImageTk.PhotoImage(picimg)
CTkButton(canvas_default, image = tkimg).grid(row=0,column=0)
                                                                                                                  
label = CTkLabel(master=canvas_default,text="Ayushi",fg_color='black', width=120,height=25).grid(row=0,column=1)

button = CTkButton(master=root,text="Logout",fg_color='midnight blue', width=120,height=25,corner_radius=20).grid(row=0,column=0,padx=20,pady=(0,200))

canvas_default.grid(row=0,column=0,padx=20)

root.mainloop()



