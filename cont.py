from tkinter import LabelFrame, PhotoImage,messagebox, ttk
from customtkinter import *
from PIL import Image, ImageTk
#from tkterminal import Terminal

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

def stats():
    root.destroy()
    import stats.py

def home():
    root.destroy()
    import main.py

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
root.title("DOCK-X")

root.attributes('-fullscreen', True)
screen_width =(int)(root.winfo_screenwidth())
screen_height =(int)(root.winfo_screenheight())
root.geometry("%d,%d" % (screen_width,screen_height))

#sidePaneMenu
framemenu = CTkFrame(master=root,height=screen_height,width=screen_width/4,fg_color="#313131")

img = CTkImage(light_image=Image.open('round.png'),dark_image=Image.open('round.png'),size=(150,150))
imglabel= CTkLabel(framemenu, text='', image = img, corner_radius=50).pack(side=TOP,padx=(10,10),pady=(20,10))

label = CTkLabel(master=framemenu,text="047pegasus",font=("Montserrat SemiBold", 20), fg_color='#3E3E3E',text_color='White').pack(side=TOP,padx=0,pady=(25,25))

download_home=CTkImage(light_image=Image.open("home.png"),dark_image=Image.open("home.png"),size=(30,30))

homelabel = CTkButton(master=framemenu,text="Home",font=("Montserrat SemiBold" ,20), cursor='arrow', fg_color='#3E3E3E',hover_color='gray11',text_color='White',image=download_home, command=home).pack(side=TOP,padx=(0,20),pady=(110,10))

download_stat=CTkImage(light_image=Image.open("statistics.png"),dark_image=Image.open("statistics.png"),size=(30,30))

cpustatslabel = CTkButton(master=framemenu,text="Statistics",font=("Montserrat SemiBold", 20), cursor='arrow',fg_color='#3E3E3E',hover_color='gray11',text_color='White',image=download_stat, command=stats).pack(side=TOP,padx=0,pady=(20,10))

download_cont=CTkImage(light_image=Image.open("box.png"),dark_image=Image.open("box.png"),size=(25,25))

contlabel = CTkButton(master=framemenu,text="Containers",font=("Montserrat SemiBold", 20), cursor='arrow',fg_color='#3E3E3E',hover_color='gray11',text_color='White',image=download_cont).pack(side=TOP,padx=0,pady=(20,10))

run_img = CTkImage(light_image=Image.open("docker_greenjpg.jpg"),dark_image=Image.open("docker_greenjpg.jpg"),size=(200,50))
running_label = CTkLabel(framemenu,text='', image= run_img,fg_color='green',corner_radius=0).pack(side=BOTTOM,padx=0,pady=(51,0))
button = CTkButton(framemenu,text="Logout",font=("Montserrat", 20), fg_color="#1D0042", width=140,height=40,corner_radius=10,command=fun).pack(side=BOTTOM,padx=0,pady=(100,20))

framemenu.pack(side=LEFT,fill=BOTH,padx=0,pady=0)

#mainWindowFrame                                                                                                                                                                                                                                    
frame_main = CTkFrame(master=root, width=1000, height=800, fg_color="Black")

frame_main.pack(side=RIGHT,padx=0,expand=True,fill=BOTH)

root.mainloop()