'''
Organizza con un dizionario i dati sui conti correnti correnti bancari con numero del conto e saldo. Fornito poi
il numero di conto, il programma visualizza il saldo oppure un messaggio nel caso in cui il conto  non sia
presente nella mappa
'''
conti = {"a101":12765, "b101":5678, "c101":678997, "a102":6755, "b102":0, "c102":56, "a103":897, "b103":1936, "c103":5782}

contatore = 1
codici = []
print("Ecco i codici di conto")
for i in conti:
    print(contatore, i)
    contatore += 1
    codici.append(i)
print("Inserire numero corrispondente al codice di conto del quale si vuole conoscere l'importo")
numero = int(input())
if numero < 10 and numero > 0:
    print("Conto:", codici[numero-1])
    print("Importo:", conti[codici[numero-1]])
else:
    print("Il numero inserito non è valido")