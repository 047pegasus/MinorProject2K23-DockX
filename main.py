from tkinter import PhotoImage
from customtkinter import *

set_appearance_mode("dark")  # Modes: system (default), light, dark
set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

root=CTk()
root.geometry("1920x1080")
frame = CTkFrame(master=root)
canvas_default = CTkCanvas(frame,bg = "Grey",height = "1920",width = 500)

#img = PhotoImage(file=".\owl.jpg")
#ctk.CTkButton(root, image = img).pack(side = LEFT)

canvas_default.pack()
label = CTkLabel(master=root,text="Ayushi",fg_color='black', width=120,height=25).grid(row=0,column=1)


frame.grid(row=0,column=0,padx=20)
root.mainloop()



