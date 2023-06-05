from tkinter import *
from customtkinter import *
from PIL import Image, ImageTk

set_appearance_mode("dark")  # Modes: system (default), light, dark
set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green


root=CTk()
root.title("Splash screen")
screen_width =(int)(root.winfo_screenwidth())
screen_height =(int)(root.winfo_screenheight())
root.geometry("%d,%d" % (screen_width,screen_height))



img = CTkImage(light_image=Image.open("splash.png"),dark_image=Image.open("splash.png"),size=(500,300))
imglabel= CTkLabel(root, text='', image = img, corner_radius=50).pack(side=TOP,padx=(10,10),pady=(20,10))

root.config(background="#101828")









































root.mainloop()