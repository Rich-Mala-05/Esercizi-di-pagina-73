'''
Scivi un programma che data in igress una lista A contenente n parole restituisca in output
una lista B di interi che rappresentano la lunghezza delle parole contenute in A.
'''
A = []
B = []
print("Scrive le tue parole (per fermarti scrivi STOP)")
parola = input()
while parola != "STOP":
    A.append(parola)
    parola = input()
for i in A:
    lettere = len(i)
    B.append(lettere)
print(B)