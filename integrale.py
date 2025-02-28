# Versione completamente autonoma, ho utilizzata chatgpt per trovare l'esistenza della funzione arange, visto che mi servivano step decimali.
from math import sqrt, pi
import numpy
def integrale(n):
    return sum([(1/n)*(sqrt(1-x**2)) for x in numpy.arange((n-1)*(1/n), 1/n)])

n = int(input("Inserire in quanti rettangolini si vuole dividere il segmento [0, 1]: "))
print(f"Area totale dei rettangolini: {integrale(n)}")
print(f"Il valore dell'integrale diviso pigreco è {integrale(n)/pi}")
print("Più è alto il numero di parti in cui viene diviso il segmento più è piccolo il rapporto, quindi l'area è più accurata.")


#### Versione corretta da chatgpt, che utilizza la funzione 'linspace' visto che i float possono essere imprecisi e causare errori.
# from math import sqrt, pi
# import numpy as np

# def integrale(n):
#     base = 1 / n
#     x_values = np.linspace(0, 1 - base, n)  # Genera esattamente n punti da 0 a 1-dx
#     return sum((base * sqrt(1 - x**2)) for x in x_values)

# n = int(input("Inserire in quanti rettangolini si vuole dividere il segmento [0, 1]: "))
# print(f"Il valore dell'integrale diviso pigreco è {integrale(n)/pi}")