print("Numero binario:")
binario = input()
lunghezza = len(binario)
print("Il numero inserito ha",lunghezza,"cifre")
potenza = 0
cifre = []
somma = 0
for cifra in binario:
    cifre.append(cifra)
cifre.reverse()
for potenze in cifre:
    print(potenze,"* ( 2 ^",potenza,") =",int(potenze)*(2**potenza))
    somma = somma + int(potenze)*(2**potenza)
    potenza = potenza + 1
print("Il numero binario",binario,"espresso in valore decimale diventa",somma)