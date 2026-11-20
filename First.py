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

# Prima funzione con dato mutabile: modifica la lista ricevuta direttamente.
def aggiungi_lista(numeri: list) -> None:
    # Aggiunge il valore 10 alla fine della lista originale.
    numeri.append(10)

# Seconda funzione con dato mutabile: modifica il dizionario ricevuto.
def aggiungi_nome(persone: dict) -> None:
    # Inserisce una nuova coppia chiave-valore nel dizionario originale.
    persone["Mario"] = 30

# Terza funzione con dato mutabile: aggiunge un elemento al set ricevuto.
def aggiungi_colore(colori: set) -> None:
    # Inserisce il colore verde nel set originale.
    colori.add("verde")

# Prima funzione con dato immutabile: restituisce un nuovo numero.
def somma_due(numero: int) -> int:
    # Restituisce un nuovo intero ottenuto sommando 2.
    return numero + 2

# Seconda funzione con dato immutabile: restituisce una nuova stringa.
def rendi_maiuscola(parola: str) -> str:
    # Trasforma tutti i caratteri in maiuscolo creando una nuova stringa.
    return parola.upper()

# Terza funzione con dato immutabile: restituisce una nuova tupla.
def aggiungi_elemento_tupla(valori: tuple) -> tuple:
    # Crea una nuova tupla aggiungendo il valore 4 alla fine.
    return valori + (4,)

# Primo esempio: la funzione prende due liste e una variabile obbligatoria.
def unisci_con_prefisso(prima_lista: list, seconda_lista: list, prefisso: str) -> list:
    # Copia i dati della prima lista per non modificarla direttamente.
    risultato = prima_lista.copy()
    # Aggiunge al risultato tutti gli elementi della seconda lista.
    risultato.extend(seconda_lista)
    # Converte ogni elemento in testo e aggiunge il prefisso davanti.
    risultato_con_prefisso = [prefisso + str(elemento) for elemento in risultato]
    # Restituisce la nuova lista completa.
    return risultato_con_prefisso

# Secondo esempio: la seconda lista ha un valore di default, quindi può essere omessa.
def unisci_con_separatore(prima_lista: list, seconda_lista: list = None, separatore: str = " - ") -> list:
    # Copia la prima lista per creare un nuovo risultato.
    risultato = prima_lista.copy()
    # Controlla se la seconda lista è stata fornita.
    if seconda_lista is not None:
        # Aggiunge gli elementi della seconda lista al risultato.
        risultato.extend(seconda_lista)
    # Trasforma gli elementi in testo e li unisce usando il separatore.
    testo_unito = separatore.join(str(elemento) for elemento in risultato)
    # Restituisce una singola stringa invece di una lista.
    return testo_unito

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
    # di seguito troviamo i set altra collezione un python sia literal che dichiarativa
    mySet = {1, 2, 3, 4, 5}
    print("Il set è:", mySet)
    mySet1 = set([1, 2, 3, 4, 5])
    print("Il set1 è:", mySet1) 
    # oer aggiungere dati si usa add e si può usare frozenset per creare un set immutabile
    setImmutabile = frozenset([1, 2, 3, 4, 5])
    print("Il set immutabile è:", setImmutabile)
    set4 = {1, 2, 3, 4, 5}
    set4.add(6)
    print("Il set4 aggiornato è:", set4)
    # controllo se un elemento è contenuto nel set usando in
    print("3 è nel set4:", 3 in set4)   
    # operazione per vedere quali elementi sono in comune tra due set usando intersection
    set5 = {4, 5, 6, 7, 8}  
    set6 = set4.intersection(set5)
    print("Gli elementi in comune tra set4 e set5 sono:", set6)
    # se usiamo OR per unire due set otteniamo tutti gli elementi di entrambi i set senza duplicati
    set7 = set4.union(set5)
    print("L'unione di set4 e set5 è:", set7)
    # se usiamo or per mettere i dati che sono nell'uno o nell'altro set ma non in entrambi otteniamo la differenza simmetrica
    set8 = set4.symmetric_difference(set5)
    print("La differenza simmetrica tra set4 e set5 è:", set8)
    # Esempio semplice di ciclo for, che ripete le istruzioni per ogni elemento della lista.
    for numero in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        # Stampa il numero corrente preso dalla lista.
        print("Numero del ciclo for:", numero)
    # Esempio semplice di ciclo while, che ripete le istruzioni finche una condizione è vera.
    contatore = 0
    # Continua il ciclo finche il contatore è inferiore a 3.
    while contatore < 3:
        # Stampa il valore corrente del contatore.
        print("Contatore del ciclo while:", contatore)
        # Incrementa il contatore di 1 per avvicinarsi alla fine del ciclo.
        contatore += 1
    # Esempio semplice di istruzione if else, che verifica una condizione.
    voto = 18
    # Controlla se il voto è sufficiente.
    if voto >= 18:
        # Comunica che il voto è sufficiente.
        print("Voto sufficiente")
    # Esegue questa parte quando la condizione if è falsa.
    else:
        # Comunica che il voto non è sufficiente.
        print("Voto insufficiente")
    # Definisce l'inizio del range: il ciclo parte dal numero 2.
    start = 2
    # Definisce il limite finale: il ciclo si ferma prima del numero 11.
    stop = 11
    # Definisce il passo: il contatore aumenta di 2 ad ogni ripetizione.
    step = 2
    # Esegue il ciclo for usando start come valore iniziale, stop come limite esclusivo e step come incremento.
    for numero in range(start, stop, step):
        # Stampa il valore corrente di numero ad ogni passaggio del ciclo.
        print("Numero del for con range:", numero)
    # Esempio di ciclo for che usa range senza valori iniziale o passo definiti separatamente.
    for numero in range(5):
        # range(5) genera i numeri da 0 fino a 4.
        print("Numero del ciclo con solo range:", numero)
    # Primo esempio di list comprehension: trasforma ogni numero elevandolo al quadrato.
    numeri = [1, 2, 3, 4]
    # Crea una nuova lista usando quadrato come valore per ogni numero presente nella lista.
    quadrati = [numero ** 2 for numero in numeri]
    # Stampa la nuova lista dei numeri elevati al quadrato.
    print("I quadrati sono:", quadrati)
    # Secondo esempio di list comprehension: mantiene solo i numeri pari.
    numeri_misti = [1, 2, 3, 4, 5, 6]
    # Controlla ogni numero e aggiunge alla nuova lista solo quelli divisibili per 2.
    pari = [numero for numero in numeri_misti if numero % 2 == 0]
    # Stampa la nuova lista contenente soltanto i numeri pari.
    print("I numeri pari sono:", pari)
    # Primo esempio di dict comprehension: crea un dizionario con un numero come chiave e il suo quadrato come valore.
    numeri = [1, 2, 3, 4]
    # Per ogni numero, la chiave è numero e il valore è numero elevato al quadrato.
    quadrati_dict = {numero: numero ** 2 for numero in numeri}
    # Stampa il dizionario creato dalla comprensione.
    print("Dizionario dei quadrati:", quadrati_dict)
    # Secondo esempio di dict comprehension: converte i nomi in chiavi e ne calcola la lunghezza come valore.
    nomi = ["Anna", "Marco", "Luca"]
    # Per ogni nome, crea una coppia chiave-valore contenente nome e numero di lettere.
    lunghezze_nomi = {nome: len(nome) for nome in nomi}
    # Stampa il dizionario con i nomi e il numero delle loro lettere.
    print("Lunghezze dei nomi:", lunghezze_nomi)
    # Terzo esempio di dict comprehension: mantiene solo i prodotti con prezzo inferiore a 20.
    prezzi = {"pane": 3, "pizza": 12, "libro": 18, "computer": 500}
    # Per ogni coppia, verifica il prezzo e mantiene solo i prodotti economici.
    prezzi_economici = {prodotto: prezzo for prodotto, prezzo in prezzi.items() if prezzo < 20}
    # Stampa il dizionario filtrato.
    print("Prezzi inferiori a 20:", prezzi_economici)
    # Primo esempio di set comprehension: crea un insieme con i quadrati dei numeri.
    numeri = [1, 2, 2, 3, 3, 4]
    # Calcola il quadrato di ogni numero; i duplicati vengono eliminati automaticamente dal set.
    quadrati_set = {numero ** 2 for numero in numeri}
    # Stampa l'insieme dei quadrati, senza valori ripetuti.
    print("Set dei quadrati:", quadrati_set)
    # Secondo esempio di set comprehension: crea un insieme con i caratteri unici di una parola.
    parola = "python"
    # Per ogni lettera della parola, inserisce la lettera nell'insieme; i caratteri ripetuti compaiono una sola volta.
    lettere_uniche = {lettera for lettera in parola}
    # Stampa tutte le lettere uniche della parola.
    print("Lettere uniche:", lettere_uniche)
    # Terzo esempio di set comprehension: seleziona soltanto i numeri pari da una lista.
    numeri = [1, 2, 3, 4, 5, 6, 6]
    # Verifica il resto della divisione per 2 e aggiunge al set solo i numeri pari.
    pari_set = {numero for numero in numeri if numero % 2 == 0}
    # Stampa il set dei numeri pari senza duplicati.
    print("Set dei numeri pari:", pari_set)
    # Primo uso di una funzione mutabile: passa una lista alla funzione.
    lista_mutabile = [1, 2, 3]
    # Modifica la lista aggiungendo il numero 10.
    aggiungi_lista(lista_mutabile)
    # Stampa la lista modificata dall'esterno della funzione.
    print("Lista modificata:", lista_mutabile)
    # Secondo uso di una funzione mutabile: passa un dizionario alla funzione.
    persone_mutabili = {"Anna": 25}
    # Aggiunge Mario al dizionario originale.
    aggiungi_nome(persone_mutabili)
    # Stampa il dizionario modificato dall'esterno della funzione.
    print("Dizionario modificato:", persone_mutabili)
    # Terzo uso di una funzione mutabile: passa un set alla funzione.
    colori_mutabili = {"rosso", "blu"}
    # Aggiunge verde al set originale.
    aggiungi_colore(colori_mutabili)
    # Stampa il set modificato dall'esterno della funzione.
    print("Set modificato:", colori_mutabili)
    # Primo uso di una funzione immutabile: passa un intero alla funzione.
    numero_originale = 5
    # Conserva in una nuova variabile il risultato restituito dalla funzione.
    numero_nuovo = somma_due(numero_originale)
    # Stampa sia il numero originale sia il nuovo numero restituito.
    print("Numero originale:", numero_originale, "- Numero nuovo:", numero_nuovo)
    # Secondo uso di una funzione immutabile: passa una stringa alla funzione.
    parola_originale = "ciao"
    # Conserva la nuova stringa maiuscola restituita dalla funzione.
    parola_nuova = rendi_maiuscola(parola_originale)
    # Stampa sia la stringa originale sia quella nuova.
    print("Parola originale:", parola_originale, "- Parola nuova:", parola_nuova)
    # Terzo uso di una funzione immutabile: passa una tupla alla funzione.
    tupla_originale = (1, 2, 3)
    # Conserva la nuova tupla restituita dalla funzione.
    tupla_nuova = aggiungi_elemento_tupla(tupla_originale)
    # Stampa sia la tupla originale sia quella nuova.
    print("Tupla originale:", tupla_originale, "- Tupla nuova:", tupla_nuova)
    # Primo esempio con parametri obbligatori: crea due liste e una variabile.
    lista_a = [1, 2]
    lista_b = [3, 4]
    prefisso_numero = "N:"
    # Passa entrambe le liste e il prefisso alla funzione.
    lista_unita = unisci_con_prefisso(lista_a, lista_b, prefisso_numero)
    # Stampa il risultato ottenuto usando tutti i parametri.
    print("Due liste con variabile obbligatoria:", lista_unita)
    # Secondo esempio: prepara una sola lista da usare con il valore di default.
    lista_sola = ["mela", "pera"]
    # Chiama la funzione senza passare la seconda lista.
    risultato_singolo = unisci_con_separatore(lista_sola)
    # Usa il separatore di default perché non viene specificato dall'utente.
    print("Chiamata con una sola lista:", risultato_singolo)
    # Prepara una seconda lista per la chiamata completa.
    lista_aggiunta = ["pesca", "banana"]
    # Passa entrambe le liste e modifica anche il separatore.
    risultato_doppio = unisci_con_separatore(lista_sola, lista_aggiunta, " | ")
    # Stampa il risultato che contiene gli elementi di entrambe le liste.
    print("Chiamata con due liste:", risultato_doppio)
