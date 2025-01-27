numero = input("inserire il primo numero: ")
n = 0
sum = 0
while numero.isdigit():
    n += 1
    sum += float(numero)
    numero = input()
print("la media è:", sum/n)