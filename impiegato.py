class Employee:
    def __init__(self, nome, cognome, salario):
        self._nome = nome
        self._cognome = cognome
        self._salario = salario
    def __repr__(self):
        return f"Oggetto Employee: {self._nome} {self._cognome} guadagna {self._salario} euro"
class Manager(Employee):
    def __init__(self, nome, cognome, salario, reparto):
        super().__init__(nome, cognome, salario)
        self._reparto = reparto
    def __repr__(self):
        return f"Oggetto Manager: {self._nome} {self._cognome} guadagna {self._salario} euro, si occupa del reparto {self._reparto}"
    
mario = Employee('Mario', 'Rossi', 1500)
luigi = Manager('Luigi', 'Verdi', 2000, 'abbigliamento')
print(mario)
print(luigi)