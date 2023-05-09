from tkinter import PhotoImage
from customtkinter import *

set_appearance_mode("dark")  # Modes: system (default), light, dark
set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

root=CTk()
root.geometry("1920x1080")

canvas_default = CTkCanvas(root,bg = "Green",height = 1080,width = 300)

#img = PhotoImage(file=".\owl.jpg")
#ctk.CTkButton(root, image = img).pack(side = LEFT)
  
#canvas_default = CTkCanvas(frame,bg = "Grey",height = "200",width = 200)
label = CTkLabel(master=canvas_default,text="Ayushi",fg_color='black', width=120,height=25).grid(row=0,column=1)

canvas_default.grid(row=0,column=0,padx=20)

root.mainloop()



