elenco_partecipanti = []
elenco_lanci = []
print("Numero partecipanti")
numero = int(input())
for i in range(numero):
    print("Nome concorrente n°",i+1)
    nome = input()
    print("Lancio giocatore n°,",i+1,"(dai un valore in metri)")
    lancio = round(float(input()),2)
    elenco_partecipanti.append(nome)
    elenco_lanci.append(lancio)
posizione = elenco_lanci.index(max(elenco_lanci))
print("Il vincitore è",elenco_partecipanti[posizione],"con un lancio di",elenco_lanci[posizione],"metri")