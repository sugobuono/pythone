class Cliente:
    def __init__(self, nome, cognome, email):
        self._nome = nome
        self._cognome = cognome
        self._email = email
        self._acquisti = []

    def __str__(self):
        return f"{self._nome} {self._cognome} ({self._email})"
    
    def azzeraAcquisti(self):
        del self._acquisti[:-1]
        self._acquisti[0] = self._acquisti[0] - 10

    def effettuaAcquisto(self, ammontare):
        self._acquisti.append(int(ammontare))

    def scontoRaggiunto(self):
        if sum(self._acquisti[:-1]) >= 100:
            self.azzeraAcquisti()
            return True
        else:
            return False


mario = Cliente("Mario", "Rossi", "mariorossi@gmail.com")
print(mario)
mario.effettuaAcquisto(80)
mario.effettuaAcquisto(30)
mario.effettuaAcquisto(50)
if mario.scontoRaggiunto():
    print("Sconto raggiunto!")
    print(f"Ultima spesa scontata: {sum(mario._acquisti)}")
else:
    print("Sconto non raggiunto")