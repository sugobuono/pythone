PRIMA_ALIQUOTA=0.23
SECONDA_ALIQUOTA=0.35
TERZA_ALIQUOTA=0.45

reddito=int(input("inserire il proprio reddito: "))
if 0<=reddito<=28000:
    aliquota=reddito*PRIMA_ALIQUOTA
if 28001<=reddito<=50000:
    aliquota=reddito*SECONDA_ALIQUOTA
if reddito>=50000:
    aliquota=reddito*TERZA_ALIQUOTA
print("il reddito al netto delle tasse è", int(reddito-aliquota))