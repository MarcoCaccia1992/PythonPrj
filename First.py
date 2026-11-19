# Definisce la classe, cioè il modello degli oggetti che possono stampare frasi e verificare numeri.
class YellowEchoAgent:
    # Descrive lo scopo della classe: ricevere una frase e stamparla in giallo nella console.
    """Riceve una frase e la stampa in giallo nella console."""

    # Definisce il metodo run, che riceve una frase di testo e non restituisce un valore.
    def run(self, phrase: str) -> None:
        # Stampa la frase in giallo usando codici ANSI, poi ripristina lo stile normale della console.
        print(f"\033[33m{phrase}\033[0m")


    # Definisce un metodo che chiede all'utente un numero e comunica se è pari o dispari.
    def paridispari(self):
        # Chiede un numero all'utente e conserva inizialmente l'input come testo.
        inp = input("inserisci numero: ")
        # Converte il testo inserito in un numero intero.
        numero = int(inp)
        # Calcola il resto della divisione del numero per 2.
        modulo = numero % 2
        # Controlla se il resto è zero, condizione che indica un numero pari.
        if modulo == 0:
            # Comunica all'utente che il numero è pari.
            print("è un numero pari")
        # Esegue il ramo alternativo quando il resto non è zero.
        else:
            # Comunica all'utente che il numero è dispari.
            print("è un numero dispari")

# Esegue il blocco seguente solo se questo file viene avviato direttamente.
if __name__ == "__main__":
    # Crea un oggetto della classe YellowEchoAgent e lo assegna alla variabile agent.
    agent = YellowEchoAgent()
    # Chiede una frase e la passa al metodo run per stamparla in giallo.
    agent.run(input("Scrivi una frase: "))
    # Avvia il metodo che chiede un numero e ne verifica la parità.
    agent.paridispari()
    # Questa stringa descrive la lista successiva, ma non è un commento Python e non viene mostrata.
    """dichiarazione di una lista"""
    # Crea una lista di cinque numeri interi.
    myList = [1,2,3,4,5]
    # Questa stringa descrive le stampe successive, ma non è un commento Python e non viene mostrata.
    """stampa di una lista"""
    # Stampa un'etichetta e l'intera lista.
    print("La lista è:", myList)
    # Stampa il numero di elementi contenuti nella lista.
    print("La lunghezza della lista è:", len(myList))
    # Stampa il primo elemento della lista, che si trova all'indice 0.
    print("Il primo elemento della lista è:", myList[0])
    # Crea una lista bidimensionale composta da tre liste di tre numeri ciascuna.
    biDimensionList = [[1,2,3],[4,5,6],[7,8,9]]
    # Stampa un'etichetta e l'intera lista bidimensionale.
    print("La lista bidimensionale è:", biDimensionList)    
    # Stampa il primo elemento della prima lista interna (riga 0, colonna 0).
    print("Il primo elemento della lista bidimensionale è:", biDimensionList[0][0])
    # Stampa il secondo elemento della seconda lista interna (riga 1, colonna 1).
    print("Il secondo elemnto della seconda lista della lista bidimensionale è:", biDimensionList[1][1])
    # inserisco alla seconda posizione un elemento nella mia lista
    myList.insert(1, 65)
    # Stampa la lista aggiornata dopo l'inserimento.    
    print("La lista aggiornata è:", myList)
    # controllo se un elemnto contenuto nella mia lista
    print("58 è nella lista:", 58 in myList)
    # di seguito posso copiare gli elementi di una lista in un'altra lista, sostituisco il secondo elemento della nuova lista e ne aggiungo uno
    myList2 = myList.copy()
    myList2[1] = 100
    myList2.append(200)
    print("La seconda lista è:", myList2)
    # creazione di una tupla, immutabile, non posso modificare gli elementi della tupla
    myTuple = ('oro', 'argento', 'bronzo')
    print("La tupla è:", myTuple)
    # la tupla si può dichiarare anche così
    medaglie = tuple(['oro', 'argento', 'bronzo'])
    print("La tupla medaglie è:", medaglie)
    # tuple unpacking o spacchettamento di una tupla per esaminarli, assegnando ad ogni elemento una variabile posta a sinistra in ordine di byte di posizione
    o, a, b = medaglie
    print("La medaglia d'oro è:", o)
    print("La medaglia d'argento è:", a)
    print("La medaglia di bronzo è:", b)
    # utilizzo dizionario che ha una struttura chiave:valore, dove la chiave è univoca e il valore può essere di qualsiasi tipo
    myDict = {'nome': 'Mario', 'cognome': 'Rossi', 'eta': 30}
    print("Il dizionario è:", myDict)

