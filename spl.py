import tkinter as tk
from tkinter import ttk
from customtkinter import *
from PIL import Image, ImageTk


i = 0

def load():
    global i
    if i <= 10:
        txt = 'Loading...' + str(10 * i) + '%'
        progress_label.configure(text=txt)
        progress['value'] = 10 * i
        i += 1
        progress_label.after(600, load)
    else:
        root.destroy()  
        top()  

def top():
    import test.py
    


root = tk.Tk()
root.title("Splash screen")



img = CTkImage(light_image=Image.open("splash.png"),dark_image=Image.open("splash.png"),size=(500,300))
imglabel= CTkLabel(root, text='', image = img, corner_radius=50, bg_color='#101828').pack(side=TOP,padx=(10,10),pady=(20,10))

root.config(background="#101828")

welcome_label=CTkLabel(root,text="DOCK-X",font=("Roboto Bold", 60), fg_color="#101828",text_color='White')
welcome_label.pack(side=BOTTOM,fill=BOTH, expand=True,padx=0,pady=(0,200))

progress= ttk.Style()
progress.theme_use('alt')
progress.configure("red.Horizontal.TProgressbar", background='#108cff',)


progress = ttk.Progressbar(root, orient="horizontal", length=500, mode="determinate")
progress.pack(side=BOTTOM, expand=True,padx=0,pady=(0,300))


progress_label = tk.Label(root, text='Loading...',font=("Roboto Bold", 15), background="#101828", foreground='white')
progress_label.pack()


load()


root.mainloop()