class Cliente:
    def __init__(self, nome, cognome, email):
        self._nome = nome
        self._cognome = cognome
        self._email = email
        self._acquisti = []

    def __str__(self):
        return f"{self._nome} {self._cognome} ({self._email})"
    
    def azzeraAcquisti(self):
        self._acquisti.clear()

    def effettuaAcquisto(self, ammontare):
        try:
            self._acquisti.append(ammontare)
        except ValueError:
            print("Errore: Inserisci un valore numerico valido.")

    def scontoRaggiunto(self):
        if sum(self._acquisti) >= 100:
            self.azzeraAcquisti()
            return True
        else:
            return False

def main():
    print(""" Benvenuto nel programma di promozione!
    Inserisci i dati del cliente: """)
    cliente = Cliente(input("Nome: "), input("Cognome: "), input("Email: "))
    print(f"Cliente inserito: {cliente}")
    azione = input(""" Indicare l'azione da compiere:
                E = Effettua acquisto
                S = Stampa cliente
                M = Modifica informazioni cliente
                V = Visualizza sconto raggiunto
                Q = Esci dal programma\n\n""").upper()
    while azione != "Q":
        if azione == "E":
            if cliente.scontoRaggiunto():
                print("La prossima spesa sarà scontata di 10 euro!")
                cliente.effettuaAcquisto(int(input("Inserisci l'ammontare dell'acquisto: "))-10)
                verifica = True
            else:
                cliente.effettuaAcquisto(int(input("Inserisci l'ammontare dell'acquisto: ")))
                verifica = False
        elif azione == "S":
            print(cliente)
        elif azione == "M":
            cliente._nome = input("Nome: ")
            cliente._cognome = input("Cognome: ")
            cliente._email = input("Email: ")
        elif azione == "V":
            if verifica:
                print("Sconto raggiunto!")
            else:
                print("Sconto non raggiunto")
        azione = input(""" Indicare l'azione da compiere:
                E = Effettua acquisto
                S = Stampa cliente
                M = Modifica informazioni cliente
                V = Visualizza sconto raggiunto
                Q = Esci dal programma\n\n""").upper()
    
    if cliente.scontoRaggiunto():
        print("Sconto raggiunto!")
        print(f"Ultima spesa scontata: {sum(cliente._acquisti)}")
    else:
        print("Sconto non raggiunto")

if __name__ == "__main__":
    main()
