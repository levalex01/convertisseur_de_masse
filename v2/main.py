#--------------------------
# Dépendance

from tkinter import *
import emoji
#-------------------------

#-------------------------
#inforamtion sur la page
root = Tk()
root.geometry("300x400")
root.title(" convertisseur de masse ")
#-------------------------

#--------------------------------------------------------------------------
# definition des variables

        
#----------------------------------------
# Clear les espaces de texte
def clear():
    Output.delete("1.0", "end-1c")
    inputtxt.delete("1.0", "end-1c")
#---------------------------------------

#---------------------------------------
# Défénition de variable pour la 
# conversion entre Kg to Lb & Lb to Kg

def Kg_to_Lb():
    INPUT = inputtxt.get("1.0", "end-1c")
    try:
        kg = float(INPUT)
        lb = round(kg * 2.205, 2)
        Output.insert(END, f"Le poids est de {lb} LB\n")
    except ValueError:
        Output.insert(END, emoji.emojize("oups une erreur est survenue\n 🙃"))

def Lb_to_Kg():
    INPUT = inputtxt.get("1.0", "end-1c")
    try:
        lb = float(INPUT)
        kg = round(lb / 2.205, 2)
        Output.insert(END, f"Le poids est de {kg} Kg\n")
    except ValueError:
        Output.insert(END, emoji.emojize("oups une erreur est survenue\n 🙃"))


#--------------------------------------
#Deffinition variable exit
def exit():
    root.destroy()
#-------------------------------------

#--------------------------------------------------------------------------


#-------------------------------------
# Propriété de la page

l = Label(text = "Quelle est le poids")

inputtxt = Text(root, height = 1,
                width = 100,
                bg = "light yellow")
 
Output = Text(root, height = 5, 
              width = 100, 
              bg = "light cyan")
 
Kg_to_lb = Button(root, height = 2,
                 width = 20, 
                 text ="Kg à Lb",
                 command = lambda:Kg_to_Lb())
lb_to_kg = Button(root, height = 2,
                 width = 20, 
                 text ="Lb à Kg",
                 command = lambda:Lb_to_Kg())

Clear = Button(root, height = 2,
                 width = 20, 
                 text ="Clear",
                 command = lambda:clear())

exit_button = Button(root, height = 15,
                 width = 20,  text="Exit", command=root.destroy) 


root.bind("<Escape>", lambda event:exit()) # Touche sur le clavier pour faire l'application

# Suite des éléments sur la page
l.pack() # titre
inputtxt.pack() # entrée de la donner
Kg_to_lb.pack(pady=20) # La type de conversion
lb_to_kg.pack(pady=20) # La type de conversion
Output.pack()  # sortie de la donnée
Clear.pack() # Vide les zone de donnée
exit_button.pack(pady=20) # boutton pour la sortie

mainloop()