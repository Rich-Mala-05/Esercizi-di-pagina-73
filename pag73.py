#primo esercizio
print("Primo esercizio:")
print ("Quanti voti ha preso il primo candidato?")
votiprimocandidato = int(input())
print ("E il secondo?")
votisecondocandidato = int(input())
totale = votiprimocandidato + votisecondocandidato
percentualevotiprimocandidato = round(float(votiprimocandidato/totale*100), 2)
percentualevotisecondocandidato = round(float(votisecondocandidato/totale*100), 2)
print ("Percentuale voti primo candidato:", percentualevotiprimocandidato)
print ("Percentuale voti primo candidato:", percentualevotisecondocandidato)
if percentualevotiprimocandidato > percentualevotisecondocandidato:
    print("Il vincitore delle elezioni e' il primo candidato!")
elif percentualevotiprimocandidato < percentualevotisecondocandidato:
    print("Il vincitore delle elezioni e' il secondo candidato!")
else:
    print("Le elezioni terminano in pareggio")
print()
print()
print()
#secondo esercizio
print("Secondo esercizio:")
print("Nome primo candidato")
nomeuno = input()
print("Nome secondo candidato")
nomedue = input()
print("Punteggio primo candidato")
punteggiouno = int(input())
print("Punteggio secondo candidato")
punteggiodue = int(input())
print()
print("Ordine alfabetico:")
if nomeuno.upper() < nomedue.upper():
    print(nomeuno)
    print(nomedue)
else:
    print(nomedue)
    print(nomeuno)
print()
print("Ordine decrescente per punteggio:")
if punteggiouno < punteggiodue:
    print(nomeuno,"(",punteggiouno,")")
    print(nomedue,"(",punteggiodue,")")
elif punteggiouno > punteggiodue:
    print(nomedue,"(",punteggiodue,")")
    print(nomeuno,"(",punteggiouno,")")
else:
    print("I 2 candidati hanno ottenuto lo stesso punetggio.")
print()
print()
print()
#terzo esercizio
print("Terzo esercizio:")
numerostipendi = 0
totalemoney = 0
while True:
    print("Inserire stipendio dipendente")
    stipendio = int(input())
    if stipendio == -1:
        break
    else: 
        numerostipendi = numerostipendi + 1
        totalemoney = totalemoney + stipendio
print("La media degli stipendi e':",round(float(totalemoney/numerostipendi),2))
print()
print()
print()
#quarto esercizio
print("Quarto esercizio:")
print("Numero veicoli transitati oggi")
passaggi = int(input())
totalepassaggi = 0
giorni = 0
while passaggi != 0:
    giorni = giorni + 1
    totalepassaggi = totalepassaggi + passaggi
    print("Numero veicoli transitati oggi")
    passaggi = int(input())
print("Sono transitati",totalepassaggi,"veicoli in",giorni,"giorni")


    