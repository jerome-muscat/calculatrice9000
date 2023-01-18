from tkinter import *
import tkinter as tk

formule = "" 

def click(num): 
    global formule 
    formule = formule + str(num) 
    equation.set(formule) 

def egalclick(): 
    try: 
        global formule 
        resultat = str(eval(formule))
        memoire(formule + "=" + str(resultat))
        equation.set(resultat) 
        formule = resultat

    except: 
        equation.set(" error ") 
        formule = "" 

def effacer(): 
    global formule 
    formule = "" 
    equation.set("") 

def supprimer_dernier_caractere():
    global formule
    calculatrice.delete(len(calculatrice.get())-1, END)
    formule = calculatrice.get()

def memoire(formule):
    tableau = []
    tableau += formule
    historique.insert(END, formule)
    
def acc_historique():
    suprhistorique.configure(state=NORMAL, background='red')

def sup_historique():
    suprhistorique.configure(state=DISABLED, background='#383B44')
    historique.delete(0, END)

fenetre = tk.Tk() 
fenetre.title("Calculatrice") 
fenetre.geometry("360x500")
fenetre.configure(background="#1E2026")
equation = StringVar() 
calculatrice = Entry(fenetre, textvariable=equation, background="#1E2026", fg = 'white', border=0)
calculatrice.grid(columnspan=5,  pady= 30 , padx = 20 , ipadx = 100 , ipady = 10)

chiffre_1 = Button(fenetre, text=' 1 ', command=lambda: click(1), height=2, width=10, background='#383B44', fg='white') 
chiffre_1.grid(row=6, column=0) 

chiffre_2 = Button(fenetre, text=' 2 ', command=lambda: click(2), height=2, width=10, background='#383B44', fg='white') 
chiffre_2.grid(row=6, column=1) 

chiffre_3 = Button(fenetre, text=' 3 ', command=lambda: click(3), height=2, width=10, background='#383B44', fg='white') 
chiffre_3.grid(row=6, column=2) 

chiffre_4 = Button(fenetre, text=' 4 ', command=lambda: click(4), height=2, width=10, background='#383B44', fg='white') 
chiffre_4.grid(row=5, column=0) 

chiffre_5 = Button(fenetre, text=' 5 ', command=lambda: click(5), height=2, width=10, background='#383B44', fg='white' ) 
chiffre_5.grid(row=5, column=1) 

chiffre_6 = Button(fenetre, text=' 6 ', command=lambda: click(6), height=2, width=10, background='#383B44', fg='white') 
chiffre_6.grid(row=5, column=2) 

chiffre_7 = Button(fenetre, text=' 7 ', command=lambda: click(7), height=2, width=10, background='#383B44', fg='white') 
chiffre_7.grid(row=4, column=0) 

chiffre_8 = Button(fenetre, text=' 8 ', command=lambda: click(8), height=2, width=10, background='#383B44', fg='white') 
chiffre_8.grid(row=4, column=1) 

chiffre_9 = Button(fenetre, text=' 9 ', command=lambda: click(9), height=2, width=10, background='#383B44', fg='white') 
chiffre_9.grid(row=4, column=2)

plus_moins = Button(fenetre, text=' \U0000207A/\U0000208B ', command=lambda: click("-"), height=2, width= 10, background='#383B44', fg='white')
plus_moins.grid(row= 7, column=0)

chiffre_0 = Button(fenetre, text=' 0 ', command=lambda: click(0), height=2, width=10, background='#383B44', fg='white') 
chiffre_0.grid(row=7, column=1) 

plus = Button(fenetre, text=' + ', command=lambda: click("+"), height=2, width=10, background='#30323A', fg='white') 
plus.grid(row=6, column=3) 

soustrac = Button(fenetre, text=' - ', command=lambda: click("-"), height=2, width=10, background='#30323A', fg='white') 
soustrac.grid(row=5, column=3) 

multipl = Button(fenetre, text=' x ', command=lambda: click("*"), height=2, width=10, background='#30323A', fg='white') 
multipl.grid(row=4, column=3) 

divide = Button(fenetre, text=' \U000000F7 ', command=lambda: click("/"), height=2, width=10, background='#30323A', fg='white') 
divide.grid(row=3, column=3) 
    
racine_carree = Button(fenetre, text="\U0000221A", command=lambda: click("**0.5"), height=2, width=10, background='#30323A', fg='white') 
racine_carree.grid(row=3, column=2) 

puissance_carree = Button(fenetre, text="x\U000000B2", command=lambda: click("**2"), height=2, width=10, background='#30323A', fg='white') 
puissance_carree.grid(row=3, column=1) 

puissance = Button(fenetre, text="x\U0000207F", command=lambda: click("**"), height=2, width=10, background='#30323A', fg='white') 
puissance.grid(row=3, column=0) 

egal = Button(fenetre, text=' = ', command=egalclick, height=2, width=10, background='#4CC2FF') 
egal.grid(row=7, column=3) 

effacer = Button(fenetre, text='C', command=effacer, height=2, width=10, background='#30323A', fg='white') 
effacer.grid(row=2, column=2)  

supprimer_dernier_caractère = Button(fenetre, text="\U0000232B", command=supprimer_dernier_caractere, height=2, width=10, background='#30323A', fg='white') 
supprimer_dernier_caractère.grid(row=2, column=3) 

Decimal= Button(fenetre, text=',', command=lambda: click('.'), height=2, width=10, background='#383B44', fg='white') 
Decimal.grid(row=7, column=2) 
   
percent= Button(fenetre, text='%', command=lambda: click('/100'), height=2, width=10, background='#30323A', fg='white') 
percent.grid(row=2, column=1)  
    
memo= Button(fenetre, text='M', command= lambda: acc_historique(), height=2, width=10, background='#30323A', fg='white') 
memo.grid(row=2, column=0)

parenthese_ouverte= Button(fenetre, text='(', command=lambda: click('('), height=2, width=10, background='#383B44', fg='white') 
parenthese_ouverte.grid(row=8, column=0)

parenthese_fermee= Button(fenetre, text=')', command=lambda: click(')'), height=2, width=10, background='#383B44', fg='white') 
parenthese_fermee.grid(row=8, column=1)

suprhistorique= Button(fenetre, text= 'supr. historique', command= lambda: sup_historique(), height=2, width=23, background='#383B44', fg='white', state=DISABLED)
suprhistorique.grid(row=8, column=2, columnspan = 2)

historique = Listbox(fenetre, height = 4, background="#1E2026", fg = 'white', border=0, highlightthickness=0)
historique.grid(row=9, columnspan=5,pady= 10, ipadx = 100 , ipady = 10)
    
fenetre.mainloop()