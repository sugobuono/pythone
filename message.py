class Message:
    def __init__(self, mittente: str, destinatario: str):
        self._mittente = mittente
        self._destinatario = destinatario
        self._listaRighe = []
        self._testo = ''
    def appendi(self, frase: str):
        self._listaRighe.append(frase)
    def toString(self):
        self._testo =  " ".join(self._listaRighe)
        print(f"From: {self._mittente}\nTo: {self._destinatario}\n{self._testo}")

mess = Message("Marco", "Mirko")
mess.appendi("Ciao oggi è una bella giornata,")
mess.appendi("ma sto male")
mess.toString()