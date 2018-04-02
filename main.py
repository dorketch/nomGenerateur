from Tkinter import *
from nomGen import *


root = Tk()
root.title("Generateur de noms - Par Martin M")
tableau = Frame(root)
tableau.pack()


text=Text(root)
text.pack(side = TOP)
def showingui():

    text.delete(1.0,END)
    text.insert(INSERT, str(shownom()))
    text.insert(INSERT, "\n")



generate = Button(tableau, text="Generer un nom", command = showingui)
generate.pack(side = RIGHT)
#
#nbnomslbl = Label(root, text="Nombre de noms:")
#nbnomslbl.pack( side = LEFT )
#nbnomsentry = Entry(root, bd=5)
#nbnomsentry.pack( side = LEFT )


root.mainloop()

