rubrica = {
    "Alberto Giampietri":39493839,
    "Alberto Zelioli":7402559120,
    "Alessandra Quartieri":3667930185,
    "Arianna Gambini":2930571834,
    "Davide Buglione":3895031945,
    "Pit":8394016345,
    "Fedeculo":1234567890}
nomi = ["Alberto Giampietri",
        "Alberto Zelioli",
        "Alessandra Quartieri",
        "Arianna Gambini",
        "Davide Buglione",
        "Pit",
        "Fedeculo"]
print("Rubrica:")
contatore = 1
for e in rubrica:
    print(contatore, e)
    contatore += 1
print("Scrivere il numero di rubrica della persona di cui si vuole conoscere il numero di telefono")
numero = int(input())
if numero > 7 or numero < 1:
    print("Non è stato possibile trovare questo numero")
else:
    print("Nome:", nomi[numero-1])
    print("Numero ti telefono:", rubrica[nomi[numero-1]])