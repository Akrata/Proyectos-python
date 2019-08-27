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
       


lista_nueva = []
crearLista(lista_nueva)

variable = 0

click = ""
while click != "q":
    click = input("apreta cualquier tecla para sacar numero, letra 'Q' para salir")
    print (lista_nueva[variable])
    if variable != 2599:
        variable +=1
    else:
        variable = 0
   

    



