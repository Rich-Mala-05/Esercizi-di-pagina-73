elenco = []
print("Inserisci uno alla volta i nomi delle città (per concludere la lista inserire '-1')")
nome = input()
while nome != '-1':
    elenco.append(nome)
    print("Hai inserito", len(elenco), "nome/i")
    nome = input()
print("Valore da verificare dell'escursione termica")
valore = round(float(input()),0)
contatore = 0
for i in elenco:
    print("Città:", i)
    massima = round(float(input("Temperatura massima ")),0)
    minima = round(float(input("Temperatura minima ")),0)
    if valore > (massima-minima):
        contatore = contatore + 1
        print()
    else:
        print()
print("Il numero di città che hanno avuto un'escursione termica maggiore di", valore, "gradi è", contatore)        