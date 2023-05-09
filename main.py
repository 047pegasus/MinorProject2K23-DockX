from customtkinter import *

set_appearance_mode("dark")  # Modes: system (default), light, dark
set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

root=CTk()
root.geometry("1920x1080")
  
frame1 = CTkFrame(master=root, width=1500, height=1000)
canvas_default = CTkCanvas(frame1,bg = "Black",height = "1045",width = 1610)
canvas_default.grid(row=0,column=0)
frame1.grid(row = 0, column = 0, padx = (0,800),pady=(0,50))         #240

frame2 = CTkFrame(master=root, width=400, height=530)
can_def1 = CTkCanvas(frame2,bg = "Teal",height = "530",width = 400)
can_def1.grid(row=0,column=0)
frame2.grid(row=0,column = 0,padx=400,pady=(50,410),sticky="nsw")        #400

frame3 = CTkFrame(master=root, width=400, height=530)
can_def2 = CTkCanvas(frame3,bg = "Teal",height = "530",width = 400)
can_def2.grid(row=0,column=0)
frame3.grid(row=0,column = 0,padx=800,pady=(50,410),sticky="nsw")

frame4 = CTkFrame(master=root, width=400, height=530)
can_def3 = CTkCanvas(frame4,bg = "Teal",height = "530",width = 400)
can_def3.grid(row=0,column=0)
frame4.grid(row=0,column = 0,padx=1200,pady=(50,410),sticky="nsw")

root.mainloop()

