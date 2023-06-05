from tkinter import LabelFrame, PhotoImage,messagebox, ttk
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
root.title("DOCK-X")
screen_width =(int)(root.winfo_screenwidth())
screen_height =(int)(root.winfo_screenheight())
root.geometry("%d,%d" % (screen_width,screen_height))

#sidePaneMenu
framemenu = CTkFrame(master=root,height=screen_height,width=screen_width/4,fg_color="gray19")

img = CTkImage(light_image=Image.open("047pegasus.jpg"),dark_image=Image.open("047pegasus.jpg"),size=(150,150))
imglabel= CTkLabel(framemenu, text='', image = img, corner_radius=50).pack(side=TOP,padx=(10,10),pady=(20,10))

label = CTkLabel(master=framemenu,text="047pegasus",font=("Roboto", 20), fg_color='gray19',text_color='White').pack(side=TOP,padx=0,pady=(30,10))

homelabel = CTkButton(master=framemenu,text="Home",font=("Roboto" ,20), cursor='arrow', fg_color='gray19',hover_color='gray11',text_color='White').pack(side=TOP,padx=0,pady=(150,10))

containerlabel = CTkButton(master=framemenu,text="Containers",font=("Roboto", 20), cursor='arrow',fg_color='gray19',hover_color='gray11',text_color='White').pack(side=TOP,padx=0,pady=(20,10))

cpustatslabel = CTkButton(master=framemenu,text="Statistics",font=("Roboto", 20), cursor='arrow',fg_color='gray19',hover_color='gray11',text_color='White').pack(side=TOP,padx=0,pady=(20,10))

run_img = CTkImage(light_image=Image.open("docker_greenjpg.jpg"),dark_image=Image.open("docker_greenjpg.jpg"),size=(200,50))
running_label = CTkLabel(framemenu,text='', image= run_img,fg_color='green',corner_radius=0).pack(side=BOTTOM,padx=0,pady=(51,0))
button = CTkButton(framemenu,text="Logout",font=("Roboto", 20), fg_color='midnight blue', width=140,height=40,corner_radius=10,command=fun).pack(side=BOTTOM,padx=0,pady=(100,20))

framemenu.pack(side=LEFT,fill=BOTH,padx=0,pady=0)

#mainWindowFrame                                                                                                                                                                                                                                    
frame_main = CTkFrame(master=root, width=1000, height=800, fg_color="Black")

frame_Top = CTkFrame(master= frame_main, width=1000, height=500, fg_color="gray10")

can_def1 = CTkCanvas(frame_Top, bg = "MediumPurple4",height = "530",width = 400)

can_def1.create_circle(200, 200, 100, fill="gold2", outline="", width=4)
can_def1.create_circle_arc(200, 200, 100, fill="grey", outline="", start=45, end=140)
can_def1.create_circle(200, 200, 70, fill="MediumPurple4", outline="", width=4)
#frame_Bottom_can1 = CTkFrame(master=can_def1, width=400, height=100, fg_color="gray10").pack(side=BOTTOM,fill=BOTH,expand=True,padx=0,pady=0)
CTkLabel(can_def1,text="Container CPU Utilization",font=("Roboto Bold", 25), fg_color='MediumPurple4',text_color='White').pack(side=BOTTOM,fill=BOTH,expand=True,padx=(40,40),pady=(150,100))
CTkLabel(can_def1,text="75%",font=("Roboto Bold", 25), fg_color='MediumPurple4',text_color='White').pack(side=BOTTOM,padx=(50,40),pady=(185,0))
can_def1.pack(side=LEFT,expand=True, padx=(20,15),pady=10)

can_def2 = CTkCanvas(frame_Top,bg = "MediumPurple4",height = "530",width = 400)

can_def2.create_circle(200, 200, 100, fill="spring green", outline="", width=4)
can_def2.create_circle_arc(200, 200, 100, fill="grey", outline="", start=165, end=220)
can_def2.create_circle(200, 200, 70, fill="MediumPurple4", outline="", width=4)
CTkLabel(can_def2,text="Container Memory Utilization \n (NVRAM)",font=("Roboto Bold", 25), fg_color='MediumPurple4',text_color='White').pack(side=BOTTOM,fill=BOTH, expand=True,padx=(20,20),pady=(115,100))
CTkLabel(can_def2,text="65%",font=("Roboto Bold", 25), fg_color='MediumPurple4',text_color='White').pack(side=BOTTOM,padx=(45,40),pady=(185,0))
can_def2.pack(side=LEFT, expand=True, padx=(5,15),pady=10)

can_def3 = CTkCanvas(frame_Top,bg = "MediumPurple4",height = "530",width = 400)

can_def3.create_circle(200, 200, 100, fill="coral", outline="", width=4)
can_def3.create_circle_arc(200, 200, 100, fill="grey", outline="", start=165, end=300)
can_def3.create_circle(200, 200, 70, fill="MediumPurple4", outline="", width=4)
CTkLabel(can_def3,text="Net CPU Utilization",font=("Roboto Bold", 25), fg_color='MediumPurple4',text_color='White').pack(side=BOTTOM,fill=BOTH,expand=True,padx=(80,80),pady=(150,100))
CTkLabel(can_def3,text="70%",font=("Roboto Bold", 25), fg_color='MediumPurple4',text_color='White').pack(side=BOTTOM,padx=(50,40),pady=(185,0))
can_def3.pack(side=LEFT,expand = True,padx=(5,20), pady=10)

frame_Top.pack(side=TOP,fill=BOTH,expand=True,padx=0,pady=0)

frame_Bottom = CTkFrame(master=frame_main, width=1000, height=400, fg_color="gray10")
style = ttk.Style(root)
style.theme_use("clam")
style.configure("Treeview", background="black", fieldbackground="black", foreground="white")

table=ttk.Treeview(frame_Bottom, columns= ('ID', 'Name', 'Status'),show= 'headings')
table.heading('ID', text='Container ID')
table.heading('Name', text='Container Name')
table.heading('Status', text='Container Status')

for i in range(3):
    ID=('2')
    Name=('Redis Enterprise')
    Status=('Running')
    data = (ID,Name , Status)
    table.insert(parent='',index = 0 , values= data)


table.pack(fill=BOTH,expand=False,padx=100,pady=(10,0))

frame_Bottombar = CTkFrame(master=frame_Bottom, width=1000, height=0.5, fg_color="gray19", corner_radius=0)
CPUlabel = CTkLabel(master=frame_Bottombar,text="CPU: 65.01%",font=("Roboto" ,15), fg_color='gray19',text_color='White').pack(side=LEFT,padx=40,pady=0)
Memlabel = CTkLabel(master=frame_Bottombar,text="Memory: 61%",font=("Roboto" ,15), fg_color='gray19',text_color='White').pack(side=LEFT,padx=10,pady=0)
Disklabel = CTkLabel(master=frame_Bottombar,text="Disk: 35%",font=("Roboto" ,15), fg_color='gray19',text_color='White').pack(side=LEFT,padx=10,pady=0)
Conlabel = CTkLabel(master=frame_Bottombar,text="Containers: Online ✅",font=("Roboto" ,15), fg_color='gray19',text_color='White').pack(side=RIGHT,padx=(0,40),pady=0)
Servlabel = CTkLabel(master=frame_Bottombar,text="Service: Running ⚡",font=("Roboto" ,15), fg_color='gray19',text_color='White').pack(side=RIGHT,padx=20,pady=0)
frame_Bottombar.pack(side=BOTTOM,fill=BOTH,expand=True,padx=0,pady=(200,0))

frame_Bottom.pack(side=BOTTOM,fill=BOTH,expand=True,padx=0,pady=0)
frame_main.pack(side=RIGHT,padx=0,expand=True,fill=BOTH)

root.mainloop()
