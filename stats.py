from tkinter import LabelFrame, PhotoImage, messagebox, ttk
from customtkinter import *
from PIL import Image, ImageTk

set_appearance_mode("dark")  # Modes: system (default), light, dark
set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

def fun_yes():
    messagebox.showinfo('Return', 'All containers are closed.')
    y = messagebox.askyesno("Confirmation", "Do you want to Logout?")
    if y:
        root.destroy()
    else:
        messagebox.showinfo('Return', 'You will now return to the main screen.')


def fun_no():
    y = messagebox.askyesno("Confirmation", "Do you want to Logout?")
    if y:
        root.destroy()
    else:
        messagebox.showinfo('Return', 'You will now return to the main screen.')


def fun():
    x = messagebox.askyesno("Confirmation", "Do you want to close all containers?")
    if x:
        fun_yes()
    else:
        fun_no()

def home():
    root.destroy()
    import main.py

def cont():
    root.destroy()
    import cont.py

root = CTk()
root.title("DOCK-X")
root.attributes('-fullscreen', True)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width},{screen_height}")

# sidePaneMenu
framemenu = CTkFrame(master=root, height=screen_height, width=screen_width / 4, fg_color="#313131")

img = CTkImage(light_image=Image.open('round.png'), dark_image=Image.open('round.png'), size=(150, 150))
imglabel = CTkLabel(framemenu, text='', image=img, corner_radius=50).pack(side=TOP, padx=(10, 10), pady=(20, 10))

label = CTkLabel(master=framemenu, text="047pegasus", font=("Montserrat", 20), fg_color='#3E3E3E',text_color='White').pack(side=TOP, padx=0, pady=(25, 25))

download_home = CTkImage(light_image=Image.open("home.png"), dark_image=Image.open("home.png"), size=(30, 30))

homelabel = CTkButton(master=framemenu, text="Home", font=("Montserrat", 20), cursor='arrow', fg_color='#3E3E3E',hover_color='gray11', text_color='White', image=download_home, command=home).pack(side=TOP, padx=(0, 20), pady=(110, 10))

download_stat = CTkImage(light_image=Image.open("statistics.png"), dark_image=Image.open("statistics.png"), size=(30, 30))

cpustatslabel = CTkButton(master=framemenu, text="Statistics", font=("Montserrat", 20), cursor='arrow', fg_color='#3E3E3E', hover_color='gray11', text_color='White', image=download_stat).pack(side=TOP, padx=0, pady=(20, 10))

download_cont = CTkImage(light_image=Image.open("box.png"), dark_image=Image.open("box.png"), size=(25, 25))

contlabel = CTkButton(master=framemenu, text="Containers", font=("Montserrat", 20), cursor='arrow',fg_color='#3E3E3E', hover_color='gray11', text_color='White', image=download_cont, command=cont).pack( side=TOP, padx=0, pady=(20, 10))

run_img = CTkImage(light_image=Image.open("docker_greenjpg.jpg"), dark_image=Image.open("docker_greenjpg.jpg"),size=(200, 50))
running_label = CTkLabel(framemenu, text='', image=run_img, fg_color='green', corner_radius=0).pack(side=BOTTOM, padx=0,  pady=(51, 0))
button = CTkButton(framemenu, text="Logout", font=("Montserrat", 20), fg_color="#1D0042", width=140, height=40,corner_radius=10, command=fun).pack(side=BOTTOM, padx=0, pady=(100, 20))

framemenu.pack(side=LEFT, fill=BOTH, padx=0, pady=0)

# mainWindowFrame
frame_main = CTkFrame(master=root, width=1000, height=800, fg_color="Black")

frame_Top = CTkFrame(master=frame_main, width=1000, height=300, fg_color="gray10")
cpu = CTkCanvas(frame_Top, bg="#1F1E2E", height="300", width=1000,highlightthickness=0)
header = CTkFrame(cpu, width=1000, height=50, fg_color="#1F1E2E")
cputag = CTkLabel(header, text="CPU", font=("Montserrat SemiBold", 20), fg_color="#1F1E2E", text_color='White').pack(side=TOP, padx=0, pady=(5,0))
header.pack(side=TOP, fill=BOTH, expand=True, padx=0, pady=(0,0))
cpugraph = CTkFrame(cpu, width=1000, height=250, fg_color="#1F1E2E")
'''
Actual Graph implementation
'''
cpugraph.pack(side=TOP, fill=BOTH, expand=True, padx=0, pady=(0,0))
cpu.pack(side=TOP, fill=BOTH, expand=True, padx=20, pady=20)
frame_Top.pack(side=TOP, fill=BOTH, expand=True, padx=0, pady=(0,0))

frame_Bottom = CTkFrame(master=frame_main, width=1000, height=600, fg_color="gray10")

frame_BottomTop = CTkFrame(master=frame_Bottom, width=1000, height=450, fg_color="gray10")
#NETWORK GRAPH
network = CTkCanvas(frame_BottomTop, bg="#1F1E2E", height="400", width=310,highlightthickness=0)
header_network = CTkFrame(network, width=310, height=50, fg_color="#1F1E2E")
networktag = CTkLabel(header_network, text="NETWORK", font=("Montserrat SemiBold", 20), fg_color="#1F1E2E", text_color='White').pack(side=TOP, padx=0, pady=(5,0))
header_network.pack(side=TOP, fill=BOTH, expand=True, padx=0, pady=(0,0))
networkgraph = CTkFrame(network, width=310, height=350, fg_color="#1F1E2E")
'''
Actual Graph implementation
'''
networkgraph.pack(side=TOP, fill=BOTH, expand=True, padx=0, pady=(0,0))
network.pack(side=LEFT, fill=BOTH, expand=TRUE, padx=10, pady=5)
#STORAGE GRAPH
storage = CTkCanvas(frame_BottomTop, bg="#1F1E2E", height="400", width=310,highlightthickness=0)
header_storage = CTkFrame(storage, width=310, height=50, fg_color="#1F1E2E")
storagetag = CTkLabel(header_storage, text="STORAGE", font=("Montserrat SemiBold", 20), fg_color="#1F1E2E", text_color='White').pack(side=TOP, padx=0, pady=(5,0))
header_storage.pack(side=TOP, fill=BOTH, expand=True, padx=0, pady=(0,0))
storagegraph = CTkFrame(storage, width=310, height=350, fg_color="#1F1E2E")
'''
Actual Graph implementation
'''
storagegraph.pack(side=TOP, fill=BOTH, expand=True, padx=0, pady=(0,0))
storage.pack(side=LEFT, fill=BOTH, expand=TRUE, padx=10, pady=5)
anim_img = CTkImage(light_image=Image.open("splash.png"), dark_image=Image.open("splash.png"), size=(500, 350))
splash_label= CTkLabel(frame_BottomTop, text='', image=anim_img, corner_radius=0).pack(side=LEFT, fill=BOTH, expand=TRUE, padx=10, pady=(60,20))
frame_BottomTop.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=0)

frame_BottomBottom = CTkFrame(master=frame_Bottom, width=1000, height=250, fg_color="gray10")
#MEMORY GRAPH
memory = CTkCanvas(frame_Bottom, bg="#1F1E2E", height="221", width=950,highlightthickness=0)
header_memory = CTkFrame(memory, width=950, height=50, fg_color="#1F1E2E")
memorytag = CTkLabel(header_memory, text="MEMORY", font=("Montserrat SemiBold", 20), fg_color="#1F1E2E", text_color='White').pack(side=TOP, padx=0, pady=(5,0))
header_memory.pack(side=TOP, fill=BOTH, expand=True, padx=0, pady=(0,0))
memorygraph = CTkFrame(memory, width=950, height=171, fg_color="#1F1E2E")
'''
Actual Graph implementation
'''
memorygraph.pack(side=TOP, fill=BOTH, expand=True, padx=0, pady=(0,0))
memory.pack(side=TOP, fill=BOTH, expand=TRUE, padx=20, pady=20)
frame_BottomBottom.pack(side=TOP, fill=BOTH, expand=True, padx=20, pady=(20,0))

frame_Bottombar = CTkFrame(master=frame_main, width=1000, height=70, fg_color="gray19", corner_radius=0) 
CPUlabel = CTkLabel(master=frame_Bottombar,text="CPU: 65.01%",font=("Montserrat" ,15), fg_color='gray19',text_color='White').pack(side=LEFT,padx=40,pady=12)
Memlabel = CTkLabel(master=frame_Bottombar,text="Memory: 61%",font=("Montserrat" ,15), fg_color='gray19',text_color='White').pack(side=LEFT,padx=10,pady=12)
Disklabel = CTkLabel(master=frame_Bottombar,text="Disk: 35%",font=("Montserrat" ,15), fg_color='gray19',text_color='White').pack(side=LEFT,padx=10,pady=12)
Conlabel = CTkLabel(master=frame_Bottombar,text="Containers: Online ✅",font=("Montserrat" ,15), fg_color='gray19',text_color='White').pack(side=RIGHT,padx=(0,40),pady=12)
Servlabel = CTkLabel(master=frame_Bottombar,text="Service: Running ⚡",font=("Montserrat" ,15), fg_color='gray19',text_color='White').pack(side=RIGHT,padx=20,pady=12)
frame_Bottombar.pack(side=BOTTOM,fill=BOTH,expand=True,padx=0,pady=0)

frame_Bottom.pack(side=TOP, fill=BOTH, expand=True, padx=0, pady=0)
frame_main.pack(side=RIGHT, padx=0, expand=True, fill=BOTH)

root.mainloop()
