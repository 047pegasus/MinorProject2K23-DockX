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


root = CTk()
root.title("DOCK-X")

# root.attributes('-fullscreen', True)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width},{screen_height}")

# sidePaneMenu
framemenu = CTkFrame(master=root, height=screen_height, width=screen_width / 4, fg_color="#3E3E3E")

img = CTkImage(light_image=Image.open('047pegasus.jpg'), dark_image=Image.open('047pegasus.jpg'), size=(150, 150))
imglabel = CTkLabel(framemenu, text='', image=img, corner_radius=50).pack(side=TOP, padx=(10, 10), pady=(20, 10))

label = CTkLabel(master=framemenu, text="047pegasus", font=("Montserrat", 20), fg_color='#3E3E3E',text_color='White').pack(side=TOP, padx=0, pady=(25, 25))

download_home = CTkImage(light_image=Image.open("home.png"), dark_image=Image.open("home.png"), size=(30, 30))

homelabel = CTkButton(master=framemenu, text="Home", font=("Montserrat", 20), cursor='arrow', fg_color='#3E3E3E',hover_color='gray11', text_color='White', image=download_home).pack(side=TOP, padx=(0, 20), pady=(110, 10))

download_stat = CTkImage(light_image=Image.open("statistics.png"), dark_image=Image.open("statistics.png"), size=(30, 30))

cpustatslabel = CTkButton(master=framemenu, text="Statistics", font=("Montserrat", 20), cursor='arrow', fg_color='#3E3E3E', hover_color='gray11', text_color='White', image=download_stat).pack(side=TOP, padx=0, pady=(20, 10))

download_cont = CTkImage(light_image=Image.open("box.png"), dark_image=Image.open("box.png"), size=(25, 25))

contlabel = CTkButton(master=framemenu, text="Containers", font=("Montserrat", 20), cursor='arrow',fg_color='#3E3E3E', hover_color='gray11', text_color='White', image=download_cont).pack( side=TOP, padx=0, pady=(20, 10))

run_img = CTkImage(light_image=Image.open("docker_greenjpg.jpg"), dark_image=Image.open("docker_greenjpg.jpg"),size=(200, 50))
running_label = CTkLabel(framemenu, text='', image=run_img, fg_color='green', corner_radius=0).pack(side=BOTTOM, padx=0,  pady=(51, 0))
button = CTkButton(framemenu, text="Logout", font=("Montserrat", 20), fg_color="#1D0042", width=140, height=40,corner_radius=10, command=fun).pack(side=BOTTOM, padx=0, pady=(100, 20))

framemenu.pack(side=LEFT, fill=BOTH, padx=0, pady=0)

# mainWindowFrame
frame_main = CTkFrame(master=root, width=1000, height=800, fg_color="Black")

frame_Top = CTkFrame(master=frame_main, width=1000, height=300, fg_color="gray10")

cpu = CTkCanvas(frame_Top, bg="#1F1E2E", height="200", width=1700,highlightthickness=0)
cpu.pack(side=TOP, expand=True, padx=20, pady=10)
frame_Top.pack(side=TOP, fill=BOTH, expand=True, padx=0, pady=0)

frame_Bottom = CTkFrame(master=frame_main, width=1000, height=1000, fg_color="gray10")

frame_Bottombar = CTkFrame(master=frame_Bottom, width=500, height=0.5, fg_color="gray19", corner_radius=0)
CPUlabel = CTkLabel(master=frame_Bottombar, text="CPU: 65.01%", font=("Montserrat", 15), fg_color='gray19', text_color='White').pack(side=LEFT, padx=40, pady=0)
Memlabel = CTkLabel(master=frame_Bottombar, text="Memory: 61%", font=("Montserrat", 15), fg_color='gray19',text_color='White').pack(side=LEFT, padx=10, pady=0)
Disklabel = CTkLabel(master=frame_Bottombar, text="Disk: 35%", font=("Montserrat", 15), fg_color='gray19', text_color='White').pack(side=LEFT, padx=10, pady=0)
Conlabel = CTkLabel(master=frame_Bottombar, text="Containers: Online ✅", font=("Montserrat", 15), fg_color='gray19', text_color='White').pack(side=RIGHT, padx=(0, 40), pady=0)
Servlabel = CTkLabel(master=frame_Bottombar, text="Service: Running ⚡", font=("Montserrat", 15), fg_color='gray19', text_color='White').pack(side=RIGHT, padx=20, pady=0)
frame_Bottombar.pack(side=BOTTOM, fill=BOTH, expand=True, padx=0, pady=0)

frame_BottomLeft = CTkFrame(master=frame_Bottom, width=800, height=740, fg_color="gray10")
memory = CTkCanvas(frame_BottomLeft, bg="#1F1E2E", height="400", width=650,highlightthickness=0)
memory.pack(side=LEFT, expand=False, padx=20, pady=(10,300))
network = CTkCanvas(frame_BottomLeft, bg="#1F1E2E", height="400", width=500,highlightthickness=0)
network.pack(side=LEFT, expand=FALSE, padx=0, pady=(10,300))


frame_BottomRight = CTkFrame(master=frame_Bottom, width=475, height=740, fg_color="gray10")
style = ttk.Style(root)
style.theme_use("alt")
style.configure("Treeview", background="black", fieldbackground="black", foreground="white", font=('Montserrat Medium', 14), rowheight=40)
style.configure("Treeview.Heading", background="black", fieldbackground="black", foreground="#ACAAFF", font=('Montserrat SemiBold', 17))

table=ttk.Treeview(frame_BottomRight, columns= ('ID', 'Name'),show= 'headings')
table.configure(height=10)
table.column("# 1", anchor='center')
table.heading('ID', text='C_ID')
table.column("# 2", anchor='center')
table.heading('Name', text='C_Name')

for i in range(2):
    ID=('')
    Name=('')
   
    data = (ID,Name )
    table.insert(parent='',index = 0 , values= data)

table.pack(side=TOP,expand=False,padx=0,pady=10)

frame_BottomLeft.pack(side=LEFT, fill=BOTH, expand=True, padx=0, pady=0)
frame_BottomRight.pack(side=LEFT, fill=BOTH, expand=True, padx=0, pady=0)

frame_Bottom.pack(side=BOTTOM, fill=BOTH, expand=True, padx=0, pady=0)
frame_main.pack(side=RIGHT, padx=0, expand=True, fill=BOTH)

root.mainloop()
