import tkinter as tk

abecedario = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
num = []



def rellenar_num():
    i=0
    while len(num) < 100:
        i+=1
        num.append(i-1)

rellenar_num()

def crearLista(lista):
    numero="00"
    if numero != "Z99":
        for l in abecedario:
            for x in num:
                numero =  (l + str(x))
            
                lista.append(numero)
    else:
        print ("no")

variableFarmacia = 0     
variableAdmision =0
def clickFarmacia():
    lista_nueva = []
    crearLista(lista_nueva)

    global variableFarmacia 
    print (lista_nueva[variableFarmacia] + " Numero para Farmacia")  
    if variableFarmacia != 2599:
        variableFarmacia +=1
    else:
        variable = 0

def clickAdmision():
    lista_nueva = []
    crearLista(lista_nueva)

    global variableAdmision 
    print (lista_nueva[variableAdmision] + " Numero para Admision")  
    if variableAdmision != 2599:
        variableAdmision +=1
    else:
        variableAdmision = 0







app = tk.Tk()
app.geometry("800x600")

button = tk.Button(app, text="Entregar numero Farmacia",command=clickFarmacia)
button2 = tk.Button(app, text="Entregar numero admision",command=clickAdmision)
button.pack()
button2.pack()


app.mainloop()
