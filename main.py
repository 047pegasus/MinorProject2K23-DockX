from tkinter import PhotoImage,messagebox
from customtkinter import *
from PIL import Image, ImageTk

set_appearance_mode("dark")  # Modes: system (default), light, dark
set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

def fun_yes():
    messagebox.showinfo('Return','All containers are closed.')
    y=messagebox.askyesno("Confirmation","Do you want to Logout?")
    if y==True:
        root.destroy()
    else:
        messagebox.showinfo('Return','You will now return to the main screen.')

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

def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
CTkCanvas.create_circle = _create_circle

def _create_circle_arc(self, x, y, r, **kwargs):
    if "start" in kwargs and "end" in kwargs:
        kwargs["extent"] = kwargs["end"] - kwargs["start"]
        del kwargs["end"]
    return self.create_arc(x-r, y-r, x+r, y+r, **kwargs)
CTkCanvas.create_circle_arc = _create_circle_arc

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


button = CTkButton(master=framemenu,text="Logout",font=("Roboto", 20), fg_color='midnight blue', width=120,height=30,corner_radius=10,command=fun).pack(side=BOTTOM,padx=0,pady=(200,100))
framemenu.pack(side=LEFT,fill=BOTH,padx=0,pady=0)

#mainWindowFrame                                                                                                                                                                                                                                    
frame_main = CTkFrame(master=root, width=1000, height=800, fg_color="Black")

can_def1 = CTkCanvas(frame_main,bg = "MediumPurple4",height = "530",width = 400)

can_def1.create_circle(200, 200, 100, fill="gold2", outline="", width=4)
can_def1.create_circle_arc(200, 200, 100, fill="grey", outline="", start=45, end=140)
can_def1.create_circle(200, 200, 70, fill="MediumPurple4", outline="", width=4)

can_def1.pack(side=RIGHT, expand=True, padx=(20,0))

can_def2 = CTkCanvas(frame_main,bg = "MediumPurple4",height = "530",width = 400)

can_def2.create_circle(200, 200, 100, fill="spring green", outline="", width=4)
can_def2.create_circle_arc(200, 200, 100, fill="grey", outline="", start=165, end=220)
can_def2.create_circle(200, 200, 70, fill="MediumPurple4", outline="", width=4)

can_def2.pack(side=RIGHT, expand=True, padx=(20,0))

can_def3 = CTkCanvas(frame_main,bg = "MediumPurple4",height = "530",width = 400)

can_def3.create_circle(200, 200, 100, fill="coral", outline="", width=4)
can_def3.create_circle_arc(200, 200, 100, fill="grey", outline="", start=165, end=300)
can_def3.create_circle(200, 200, 70, fill="MediumPurple4", outline="", width=4)

can_def3.pack(side=RIGHT, expand = True,padx=(20,20))

frame_main.pack(side=RIGHT,padx=0,expand=True,fill=BOTH)

root.mainloop()
