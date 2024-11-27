lista = []
def aggiungiElementi():
    x = input()
    lista.append(x) # l'input va fatto nel main

def visualizzaElementi():
    for i in range(len(lista)):
        print(f"{i + 1}. {lista[i]}") #

def rimuoviElementi():
    x = input()
    lista.pop(x - 1)

def contaElementi():

    print(f"Numero di elementi nella lista: {len(lista)}")

def svuotaLista():
    lista.clear()

while True:
    print("premi 0 per uscire,\npremi 1 per aggiungerre un elemento,\npremi 2 per visualizzare la lista,\n premi 3 per eliminare un elemento,\n premi 4 per contare gli elementi della lista,\n premi 5 per eliminare un elemento")
    x=int(input(""))
    if x == 0:
        break
    elif x == 1:
        aggiungiElementi()
    elif x == 2:
        visualizzaElementi()
    elif x == 3:
        rimuoviElementi()
    elif x == 4:
        contaElementi()
    elif x == 5:
        svuotaLista()
