from tkinter import *
 
root = Tk()
root.geometry("300x300")
root.title(" ton poid ")


#--------------------------------------------------------------------------
# definition des variables


#----------------------------------------
#recupere le poids et remplace la veuleur du texte
def Take_input():
    
    INPUT = inputtxt.get("1.0", "end-1c")
    Output.insert(END, "ton poids est de " + INPUT)
#----------------------------------------
        
#----------------------------------------
# Clear les espaces de texte
def clear():
    Output.delete("1.0", "end-1c")
    inputtxt.delete("1.0", "end-1c")
#---------------------------------------


#--------------------------------------
#Deffinition variable exit
def exit():
    root.destroy()
#-------------------------------------

#--------------------------------------------------------------------------
     
l = Label(text = "Quelle est ton poids")

inputtxt = Text(root, height = 1,
                width = 25,
                bg = "light yellow")
 
Output = Text(root, height = 5, 
              width = 25, 
              bg = "light cyan")
 
Display = Button(root, height = 2,
                 width = 20, 
                 text ="Show",
                 command = lambda:Take_input())

Display2 = Button(root, height = 2,
                 width = 20, 
                 text ="Clear",
                 command = lambda:clear())

exit_button = Button(root, height = 15,
                 width = 20,  text="Exit", command=root.destroy) 
root.bind("<Escape>", lambda event:exit())

  
l.pack()
inputtxt.pack()
Display.pack(pady=20)
Output.pack()
Display2.pack()
exit_button.pack(pady=20)

mainloop()