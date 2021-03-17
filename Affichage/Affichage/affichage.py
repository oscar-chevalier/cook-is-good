from tkinter import *
from PIL import ImageTk,Image
import time

window = Tk()
window.title("Cook is Good - /n")
mode = "white"


#LOG0
#Ouvrir Logo
logo = Image.open("Logo.png")
#Resize
resized = logo.resize((142,100))
new_logo = ImageTk.PhotoImage(resized)
label = Label(window,image=new_logo,padx=5)
text = Label(window,text="Cook Is Good",pady=5)

label.grid(row=0,column=0)
text.grid(row=1,column=0)


# Timer

def clock():
   hour = time.strftime("%H")
   minute = time.strftime("%M")
   second = time.strftime("%S")

   timer.config(text=hour + ":" + minute + ":" + second)
   timer.after(1000,clock)
   
def update():
   timer.config(text="New Text",font=(48),fg=black)
   
timer = Label(window,text="")
#timer.after(5000, update)
clock()
timer.grid(row=20,column=0)

#.after(ms) -> fais la chose après x ms


# Other

def donothing():
   filewin = Toplevel(window)
   button = Button(filewin, text="Do nothing button")
   button.pack()

def black_mode():
   global mode
   window["bg"]="#282828"
   mode = "#282828"
   
def white_mode():
   global mode
   window["bg"]="white"
   mode = "white"

menu = Menu(window)
new_item = Menu(menu)

new_item.add_command(label='Nouveau',command=donothing)
new_item.add_command(label='Ouvrir')
menu.add_cascade(label='Fichier', menu=new_item)


affichage = Menu(menu)
affichage.add_command(label="Augmenter la taille")
affichage.add_command(label="Diminuer la taille")
affichage.add_command(label="Mode sombre",command=black_mode)
affichage.add_command(label="Mode clair",command=white_mode)
menu.add_cascade(label='Affichage', menu=affichage)

outils = Menu(menu)
outils.add_command(label="Changer la langue")
outils.add_command(label="Aide")
menu.add_cascade(label="Outils",menu=outils)


#Last - Config
window.config(menu=menu)
window.mainloop()

