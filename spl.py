import tkinter as tk
from tkinter import ttk
from customtkinter import *
from PIL import Image, ImageTk

i = 0

def load():
    global i
    if i <= 5:
        txt = 'Loading...' + str(20 * i) + '%'
        progress_label.configure(text=txt)
        progress['value'] = 20 * i
        i += 1
        progress_label.after(200, load)
    else:
        root.destroy()  
        top()  

def top():
    import test.py
    


root = tk.Tk()
root.title("Splash screen")
root.eval('tk::PlaceWindow . center')
root.overrideredirect(True)


img = CTkImage(light_image=Image.open("splash.png"),dark_image=Image.open("splash.png"),size=(500,300))
imglabel= CTkLabel(root, text='', image = img, corner_radius=50, bg_color='#101828').pack(side=TOP,padx=0,pady=0)

root.config(background="#101828")

welcome_label=CTkLabel(root,text="DOCK-X",font=("Roboto Bold", 60), fg_color="#101828",text_color='White')
welcome_label.pack(side=TOP,fill=BOTH, expand=True,padx=0,pady=(0,20))

progress= ttk.Style()
progress.theme_use('alt')
progress.configure("red.Horizontal.TProgressbar", background='#00002a')



progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate", style="red.Horizontal.TProgressbar")
progress.pack(side=BOTTOM, expand=True,padx=0,pady=(0,30))


progress_label = tk.Label(root, text='Loading...',font=("Roboto Bold", 15), background="#101828", foreground='white')
progress_label.pack(side=BOTTOM, expand=True,padx=0,pady=10)


load()


root.mainloop()
