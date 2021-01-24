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

contatore = 1
for i in nazioni:
    print(contatore, i)
    contatore += 1
print("Inserire numero nazione della quale si vuole conoscere la capitale")
numero = int(input())
if numero > 0 and numero < 48:
    print("Nazione:", nazioni[numero-1])
    print("Capitale:", dizionario[nazioni[numero-1]])
else:
    print("Il numero inserito non è valido")