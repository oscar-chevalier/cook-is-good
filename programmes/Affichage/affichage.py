from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import time

from programmes.recettes.recettes_manager import conseiller_recette, recettes_existantes, gestionnaire_des_recettes
from programmes.cuisines.configer import chercheur_de_toutes_les_configs, supprimer_config, Config, trouveur_de_config, \
    createur_de_config, saver_de_config
from programmes.cuisines.cuisine_manager import cuisine_opener, chercheur_de_cuisines, Cuisine, cuisine_saver
from programmes.bases import crediter, Date
from programmes.stock.stock_manager import IngredientStock
from programmes.recettes.recettes_opener import decodage

config = trouveur_de_config()
langue = config.langue.dictionnaire['affichage_dev']


def liste_en_texte(liste):
    texte = ""
    for element in liste:
        texte += element + "\n"
    return texte


window = Tk()
window.title(" Cook is Good ")
mode = "white"
window.geometry("1000x1000")


# ----------------------- A propos window
def new_window():
    new = Toplevel(window)
    text = Label(new, font=('Helvetica bold', 0),
                 text="Icons by Freepik, \n Original idea by Marc Chevalier, \n UI by Maxime Bézot, \n Management by Oscar Chevalier")

    windowWidth = new.winfo_reqwidth()
    windowHeight = new.winfo_reqheight()
    print("Width", windowWidth, "Height", windowHeight)

    # Gets both half the screen width/height and window width/height
    positionRight = int(new.winfo_screenwidth() / 2 - windowWidth / 2)
    positionDown = int(new.winfo_screenheight() / 2 - windowHeight / 2)

    # Positions the window in the center of the page.
    new.geometry("+{}+{}".format(positionRight, positionDown))

    text.pack()


# OUVRIR
from programmes.recettes.recettes_opener import decodage


def ouvrir_fichier():
    window.filename = filedialog.askopenfilename(initialdir="/", title="Selectionner une recette",
                                                 filetypes=(("menu files", "*.menu"), ("all files", "*.*")))
    recette = decodage(window.filename.split('/')[-1].split('.')[0])
    affichage_recette = Label(window, text=str(recette), borderwidth=2, relief="solid")
    affichage_recette.grid(row=2, column=2)


# ----------------------- REMPLIR PAR RECETTES

"""
def recettes(config: Config):
    langue = config.langue.dictionnaire['affichage_dev']
    liste1 = recettes_existantes()
    liste2 = []
    for i, ele in enumerate(liste1):
        liste2.append(str(i) + ' ' + ele)
    #aff = Rectangle(50, 10, langue[20], liste2).aff(True)
    rep = reponses(aff, (), True)
    lecteur_de_recettes([liste1[int(rep)]], config)

def lecteur_de_recettes(str_recettes: List[str], config: Config):
    langue = config.langue.dictionnaire['affichage_dev']
    recettes = []
    for str_rec in str_recettes:
        recettes.append(decodage(str_rec))
    ordre_actions = gestionnaire_des_recettes(recettes)
    for i in range(len(ordre_actions)):
        suiv = ''
        if i + 1 < len(ordre_actions):
            suiv = ' ' + ordre_actions[i+1].aff_str()
        aff = Rectangle(100, 10, langue[21], [ordre_actions[i].aff_str(), suiv]).aff(True)
        reponses(aff, (), False)
"""

# ----------------------- PERIMES INGREDIENTS


bientot_perimes = Label(window, text="Ingrédients bientôt périmés", borderwidth=2, relief="solid")
ingredients_bientot_permimes = Label(window, text=liste_en_texte(config.cuisine.ingredients_bientot_perimes(0, 8)),
                                     borderwidth=5, relief="solid", highlightbackground="red")

bientot_perimes.grid(row=1, column=3)
ingredients_bientot_permimes.grid(row=2, column=3)

# LOG0
# Ouvrir Logo
logo = Image.open("programmes/Affichage/Logo.png")
# Resize
resized = logo.resize((142, 100))
new_logo = ImageTk.PhotoImage(resized)
label = Label(window, image=new_logo, padx=5)
text = Label(window, text="Cook Is Good", pady=5)

label.grid(row=0, column=0)
text.grid(row=1, column=0)


# Timer

def clock():
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")

    timer.config(text=hour + ":" + minute + ":" + second, font=('Helvatical bold', 30))
    timer.after(1000, clock)


timer = Label(window, text="")
# timer.after(5000, update)
clock()
timer.grid(row=2, column=0)


# .after(ms) -> fais la chose après x ms


# Other

def donothing():
    filewin = Toplevel(window)
    button = Button(filewin, text="Do nothing button")
    button.pack()


def black_mode():
    global mode
    window["bg"] = "#282828"
    mode = "#282828"


def white_mode():
    global mode
    window["bg"] = "white"
    mode = "white"


def aff_main_menu():
    menu = Menu(window)
    new_item = Menu(menu)

    new_item.add_command(label='Nouveau')
    new_item.add_command(label='Ouvrir', command=ouvrir_fichier)
    menu.add_cascade(label='Fichier', menu=new_item)

    affichage = Menu(menu)
    affichage.add_command(label="Augmenter la taille")
    affichage.add_command(label="Diminuer la taille")
    affichage.add_command(label="Mode sombre", command=black_mode)
    affichage.add_command(label="Mode clair", command=white_mode)
    menu.add_cascade(label='Affichage', menu=affichage)

    outils = Menu(menu)
    outils.add_command(label="Changer la langue")
    outils.add_command(label="Aide")
    outils.add_command(label="A propos", command=new_window)
    menu.add_cascade(label="Outils", menu=outils)

    # Last - Config
    window.config(menu=menu)
    window.mainloop()

