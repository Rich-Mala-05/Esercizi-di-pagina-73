'''
Scrivi un programma a cui viene passata una parola e riconosce se si tratta di un
palindromo (parole che si leggono uguali anche al contrario) oppure meno
'''
print("Scrivi una parola")
parola = input()
parolaupper = parola.upper()
nuovaparola = ""
lettere = []
for i in parolaupper:
    lettere.append(i)
lettere.reverse()
for e in lettere:
    nuovaparola = nuovaparola + e
if nuovaparola == parolaupper:
    print("La parola", parola, "è palindroma")
else:
    print("La parola", parola, "non è palindroma")