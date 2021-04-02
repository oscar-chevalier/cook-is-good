from tkinter import *
from PIL import ImageTk,Image

window = Tk()
window.title("Cook is Good - /n")

#LOG0
#Ouvrir Logo
logo = Image.open("Logo.png")
#Resize
resized = logo.resize((100, 100))
new_logo = ImageTk.PhotoImage(resized)
label = Label(window, image=new_logo)
text = Label(window, text="Cook Is Good")

label.grid(row=0, column=0)
text.grid(row=1, column=0)


def donothing():
   filewin = Toplevel(window)
   button = Button(filewin, text="Do nothing button")
   button.pack()


def black_mode():
   window["bg"]="#282828"


def white_mode():
   window["bg"]="white"


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

