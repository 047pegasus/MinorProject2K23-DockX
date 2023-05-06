from customtkinter import *

set_appearance_mode("dark")  # Modes: system (default), light, dark
set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

root=CTk()
root.geometry("1366x720")
  
frame = CTkFrame(master=root, width=200, height=200)
canvas_default = CTkCanvas(frame,bg = "Grey",height = "200",width = 200)


canvas_default.pack()
  
frame.pack()  

root.mainloop()