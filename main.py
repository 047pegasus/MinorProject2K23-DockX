from tkinter import PhotoImage,messagebox
from customtkinter import *
from PIL import Image, ImageTk

set_appearance_mode("dark")  # Modes: system (default), light, dark
set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green


def fun_yes():
    print("p")

def fun_no():
    y=messagebox.askyesno("Confirmation","Do you want to Logout?")
    if y==True:
        root.destroy()
    else:
        messagebox.showinfo('Return','You will now return to the main screen.')

def fun():
    x= messagebox.askyesno("Confirmation","Do you want to close all containers?")
    if x==True:
        fun_yes()
    else:
        fun_no()


root=CTk()
screen_width =(int)(root.winfo_screenwidth())
screen_height =(int)(root.winfo_screenheight())
root.geometry("%d,%d" % (screen_width,screen_height))

#sidePaneMenu
framemenu = CTkFrame(master=root,height=screen_height,width=screen_width/4,fg_color="gray19")

img = CTkImage(light_image=Image.open("owl.jpg"),dark_image=Image.open("owl.jpg"),size=(150,150))
imglabel= CTkLabel(framemenu, text='', image = img, corner_radius=50).pack(side=TOP,padx=(10,10),pady=(20,10))

label = CTkLabel(master=framemenu,text="047pegasus",font=("Roboto", 20), fg_color='gray19',text_color='White').pack(side=TOP,padx=0,pady=(30,10))

homelabel = CTkButton(master=framemenu,text="Home",font=("Roboto" ,20), cursor='arrow', fg_color='gray19',hover_color='gray11',text_color='White').pack(side=TOP,padx=0,pady=(150,10))

containerlabel = CTkButton(master=framemenu,text="Containers",font=("Roboto", 20), cursor='arrow',fg_color='gray19',hover_color='gray11',text_color='White').pack(side=TOP,padx=0,pady=(20,10))

cpustatslabel = CTkButton(master=framemenu,text="CPU Statistics",font=("Roboto", 20), cursor='arrow',fg_color='gray19',hover_color='gray11',text_color='White').pack(side=TOP,padx=0,pady=(20,10))


button = CTkButton(master=framemenu,text="Logout",font=("Roboto", 20), fg_color='midnight blue', width=120,height=30,corner_radius=20,command=fun).pack(side=BOTTOM,padx=0,pady=(200,100))
framemenu.pack(side=LEFT,fill=BOTH,padx=0,pady=0)

#mainWindowFrame                                                                                                                                                                                                                                    
frame_main = CTkFrame(master=root, width=1000, height=800, fg_color="Black")

can_def1 = CTkCanvas(frame_main,bg = "MediumPurple4",height = "530",width = 400)
can_def1.pack(side=RIGHT, expand=True, padx=20)

can_def2 = CTkCanvas(frame_main,bg = "MediumPurple4",height = "530",width = 400)
can_def2.pack(side=RIGHT, expand=True, padx=20)

can_def3 = CTkCanvas(frame_main,bg = "MediumPurple4",height = "530",width = 400)
can_def3.pack(side=RIGHT, expand = True,padx=20)

frame_main.pack(side=RIGHT,padx=20,expand=True)

root.mainloop()
