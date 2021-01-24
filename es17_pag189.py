nazioni = ["Albania", "Andorra", "Armenia", "Austria", "Azerbaigian", "Belgio", "Bielorussia", "Bosnia ed Erzegovina", "Croazia", "Bulgaria", "Cipro", \
"Vaticano","Danimarca", "Estonia", "Finlandia", "Francia", "Germania", "Grecia", "Irlanda", "Islanda", "Italia", "Kazakistan", "Lettonia", "Liechtenstein", "Lituania", \
"Lussemburgo", "Macedonia", "Malta", "Moldavia", "Monaco", "Montenegro", "Norvegia", "Polonia", "Portogallo", "Regno Unito", "Repubblica Ceca", "Romania", "Russia", "San Marino", \
"Serbia", "Slovacchia", "Slovenia", "Spagna", "Svezia", "Svizzera", "Turchia", "Ungheria"]

capitali = ["Tirana", "Andorra la Vella", "Erevan", "Vienna", "Baku", "Bruxelles", "Minsk", "Sarajevo", "Zagabria", "Sofia", "Nicosia",\
"Città del Vaticano", "Copenaghen", "Tallinn", "Helsinki", "Parigi", "Berlino", "Atene", "Dublino", "Reykjavík", "Roma", "Nur-Sultan", "Riga", "Vaduz", "Vilnius",\
"Lussemburgo", "Skopje", "La Valletta", "Chișinău", "Monaco", "Podgorica", "Oslo", "Varsavia", "Lisbona", "Londra", "Praga", "Bucarest", "Mosca", "San Marino", \
"Belgrado", "Bratislava", "Lubiana", "Madrid", "Stoccolma", "Berna", "Ankara", "Kiev"]


dizionario = {}
for i in nazioni:
    dizionario[i] = capitali[nazioni.index(i)]

dizionario_due = {}
for e in dizionario:
    dizionario_due[dizionario[e]] = e

contatore = 1
for f in capitali:
    print(contatore, f)
    contatore += 1
print("Inserire numero capitale della quale si vuole conoscere la nazione")
numero = int(input())
if numero > 0 and numero < 48:
    print("Capitale:", capitali[numero-1])
    print("Nazione:", dizionario_due[capitali[numero-1]])
else:
    print("Il numero inserito non è valido")