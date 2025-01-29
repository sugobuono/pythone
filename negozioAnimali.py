# Funzione che calcola lo sconto e lo stampa
def discount(prices, nItems):
    contaY = 0
    contaN = 0
    spesa_totale = 0
    spesa_animali = 0
    for non_scontato in range(nItems):
        decimale = str(prices[non_scontato])
        spesa_totale += float(decimale[:-1])
        if prices[non_scontato].find("Y") != -1:
            contaY += 1
            spesa_animali += float(decimale[:-1])
        else:
            contaN += 1
    spesa_articoli = spesa_totale - spesa_animali
    sconto = spesa_articoli*0.2
    pagamento = spesa_totale - sconto
    if contaY == 0:
        print("Non si ha diritto allo sconto poichè non si prende un animale.")
    elif contaY >= 1 and contaN < 5:
        print("Non si ha diritto allo sconto poichè servono almeno 5 articoli oltre all'animale.")
    else:
        print("Lo sconto è di", sconto, "euro, su un totale di", spesa_totale, "euro. Da pagare:", pagamento)
    
# Funzione che aggiunge uno zero dopo il primo decimale se l'utente se lo dimentica ad es. 33.4N diventa 33.40N
def aggiungiZero(current):
    if current[::-1].find(".") == 2:
        current = current[:-1] + "0" + current[-1]
        return current
    elif current.find(".") == -1:
        current = current[:-1] + ".00" + current[-1]
        return current
    else:
        return current
    
# Funzione che controlla che il prezzo sia scritto precisamente nel formato cifre+N o cifre+Y senza simboli, spazi o qualsiasi altro carattere
def controlloFormatoPrezzo(costo):
    if costo[-1] == "Y" or costo[-1] == "N":
        if costo.find(".") != -1:
            if costo[-3:-1].isdigit() == True and costo[:-4].isdigit() == True:
                return True
            else:
                return False
        else:
            if costo[:-1].isdigit():
                return True
            else:
                return False
    else:
        return False

# Inizializzazione lista e inserimento primo articolo
lista_prezzi = []
lista_prezzi.append(input("Inserire il prezzo del primo articolo e specificare ogni volta se si tratta di un animale con Y subito dopo il prezzo o N, inserire -1 per terminare.\n"))
lista_prezzi[0] = aggiungiZero(lista_prezzi[0])

# Ciclo che esorta a inserire almeno un prezzo se l'input è -1
while lista_prezzi[0] == "-1" or controlloFormatoPrezzo(lista_prezzi[0]) == False:
    print("Inserire almeno un prezzo:")
    lista_prezzi[0] = input()
contatore = 0

# Riempimento della lista con controllo dei valori inseriti
while lista_prezzi[contatore] != "-1":
    lista_prezzi.append(input("Inserire il prossimo prezzo:\n"))
    contatore += 1
    if lista_prezzi[contatore] != "-1":
        lista_prezzi[contatore] = aggiungiZero(lista_prezzi[contatore])
    while controlloFormatoPrezzo(lista_prezzi[contatore]) == False:
        if lista_prezzi[contatore] == "-1":
            break
        print("Formato dell'importo errato.")
        lista_prezzi.pop()
        lista_prezzi.append(input("Reinserire il prezzo:\n"))
print(lista_prezzi[:-1])

# Chiamo la funzione che stampa lo sconto
discount(lista_prezzi, contatore)