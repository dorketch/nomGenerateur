from Tkinter import *
from nomGen import *
from random import randint



def showingui():
    text.delete(1.0,END)
    i = DblNom.get()
    if i==0:
        leNom = prenomNom()
        text.insert(INSERT, str(leNom.single))
        text.insert(INSERT, "\n")
        
    else:
        leNom = prenomNom()
        text.insert(INSERT, str(leNom.result))
        text.insert(INSERT, "\n")

        


root = Tk()
root.resizable(width=False, height=False)
root.title("Generateur de noms - Par Martin M")
root.geometry('570x400+130+100')

DblNom = BooleanVar()
DblNom.set(True)
#startName=shownom()

text= Text(root)
btnGen = Button(root, text="Generer un nom", command=showingui)
btnDblNom = Checkbutton(root, text="Noms de famille compose", variable=DblNom, onvalue=True)

btnDblNom.grid(column=0, row=0)
btnGen.grid(column=1, row=0, columnspan=1)
text.grid(column=0, row=1,columnspan=3, rowspan=5, sticky=(N))

showingui()
#
#nbnomslbl = Label(root, text="Nombre de noms:")
#nbnomslbl.pack( side = LEFT )
#nbnomsentry = Entry(root, bd=5)
#nbnomsentry.pack( side = LEFT )

root.mainloop()

