'''
In Svezia i bambini giocano spesso utilizzando un linguaggio un po' particolare detto
"rovarsprakel", che significa "linguaggio dei furfanti": consiste nel raddoppiare ogni
consonante di una parola e inserire una "o" nel mezzo. Ad esempio la parola
"mangiare" diventa "momanongogiarore".

Scrivi un programma in grado di tradurre una parola o frase passata tramite input in "rovarsprakel".

Dopo aver tradotto una frase, il programma dovrà chiedre all'utente se intende
tradurne un'altra, e in caso di risposta positiva, dovrà attendere l'iserimento di una
nuova parola da parte dell'utente.
'''
while True:
    print("Parola italiana")
    parola = input()
    vocali = ["a","e","i","o","u"]
    nuovaparola = ""
    for i in parola:
        stato = vocali.count(i)
        if stato == 0:
            index = parola.index(i)
            nuovaparola = nuovaparola + i + "o" + i.lower()
        else:
            nuovaparola = nuovaparola + i
    print("La nuova parola è:",nuovaparola)
    print("Vuoi tradurre ancora?")
    print("1 = Sì")
    print("2 = NO")
    risposta = input()
    if risposta == "1":
        print("Benissimo!")
    else:
        print("Peccato")
        break