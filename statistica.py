
def isNumber (stringaNumero) :
    if len(stringaNumero) > 0 :
        if stringaNumero.isdigit() :
            return True
        else :
            if stringaNumero.startswith("-") and stringaNumero[1:].isdigit() :   # [] vuol dire che parto dal secondo carattere all'ultimo se scrivevo da [0:-2] dal primo carattere al -2
                return True
            else :
                return False
    else :  
        return False
    

def main():
    valutazione = []
    val = 0
    valUtente   = input("Valutazioni del film visto da 1 a 5!")
    while isNumber(valUtente):
        valutazione.append(int(valUtente))
        valUtente = input()
    valutazione.remove(min(valutazione))
    valutazione.remove(max(valutazione))
    print("La media del film visto è", sum(valutazione) / len(valutazione))

        
main()