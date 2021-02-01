prenotazioni = []
contatore = 1
while True:
    print("Inserire nome e cognome partecipante", contatore, "(Scrivere STOP per terminare)")
    nome = input()
    contatore += 1
    if nome != "STOP":
        prenotazioni.append(nome)
    else:
        break
for e in prenotazioni:
    print("Si vuole inviare la lettera di conferma a", e,"? (rispondi 1 o 2)")
    print("1. Si")
    print("2. No")
    conferma = input()
    if conferma == "1":
        print("Lettera inviata!")
        prenotazioni.remove(e)
    else:
        print("Lettera non inviata")
print("Ecco l'elenco dei partecipanti che non hanno ricevuto la lettera di conferma", prenotazioni)