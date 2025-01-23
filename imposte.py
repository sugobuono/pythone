PRIMA_ALIQUOTA=0.23
SECONDA_ALIQUOTA=0.35
TERZA_ALIQUOTA=0.43

reddito=int(input("inserire il proprio reddito: "))
if 0<=reddito<=28000:
    aliquota=reddito*PRIMA_ALIQUOTA
elif 28001<=reddito<=50000:
    aliquota=reddito*SECONDA_ALIQUOTA
else:
    aliquota=reddito*TERZA_ALIQUOTA
print(aliquota)
print("il reddito al netto delle tasse è", reddito-aliquota)
