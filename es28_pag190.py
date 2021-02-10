dati = {}
contatore_uno = 1
while True:
    print("Inserire STOP per fermare")
    print("Inserire nome città", contatore_uno)
    città = input()
    if città != "STOP":
        print("Inserire cap città", contatore_uno)
        cap = int(input())
        dati[cap] = città
        contatore_uno += 1
    else:
        break
print("Ecco le città:")
contatore_due = 1
for e in dati:
    print(contatore_due, dati[dati[contatore_due-1]])
    contatore_due += 1
print("Inserire numero di città")
numero_città = int(input(""))
if numero_città > contatore_uno or numero_città < 1:
    print("Numero di città non inserito in elenco")
else:
    print("Città:", dati[dati[numero_città-1]])
    print("Cap:", dati[numero_città-1])

print("Ecco i CAP:")
contatore_tre = 1
for e in dati:
    print(contatore_tre, dati[dati[contatore_tre-1]])
    contatore_tre += 1
print("Inserire numero corrispondente al CAP (non il numero di CAP)")
numero_cap = int(input(""))
if numero_cap > contatore_uno or numero_cap < 1:
    print("Numero di città non inserito in elenco")
else:
    print("Città:", dati[dati[numero_cap-1]])
    print("Cap:", dati[numero_cap-1])