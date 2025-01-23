PRIMA_ALIQUOTA=0.23
SECONDA_ALIQUOTA=0.35
TERZA_ALIQUOTA=0.43

base1=28000*0.23
base2=22000*0.35
reddito=int(input("inserire il proprio reddito:"))
if reddito<=28000:
    aliquota=reddito*PRIMA_ALIQUOTA
    print("il reddito al netto delle tasse è:",reddito-aliquota)
else:
    if reddito<=50000:
        aliquota=base1+(reddito-28000)*0.35
        print("il reddito al netto delle tasse è:",reddito-aliquota)
    else:
        aliquota=base1+base2+(reddito-50000)*0.43
        print("il reddito al netto delle tasse è:",reddito-aliquota)
