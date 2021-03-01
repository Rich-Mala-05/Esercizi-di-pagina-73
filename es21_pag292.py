class Motociclo:

    def __init__(self, modello, cilindrata, alimentazione, tempi_motore, prezzo):
        self.modello = modello
        self.cilindrata = cilindrata
        self.alimentazione = alimentazione
        self.tempi_motore = tempi_motore
        self.prezzo = prezzo

    def info(self):
       print("Modello:", self.modello)
       print("Cilindrata:", self.cilindrata, "cc")
       print("Alimentazione:", self.alimentazione)
       print("Tempi_motore:", self.tempi_motore)
       print("Prezzo:", self.prezzo, "$")

class Ciclomotore(Motociclo):
    def _init_(self, modello, cilindrata, alimentazione, tempi_motore, prezzo):
        super()._init_(modello, cilindrata, alimentazione, tempi_motore, prezzo)

modello = input("Qual è il modello del motociclo? ")
cilindrata = int(input("Qual è la cilindrata? (cc) "))
alimentazione = input("Qual è l'alimentazione? ")
tempi_motore = int(input("Quanti tempi ha il motore? (2 o 4) "))
prezzo = int(input("Qual è il prezzo del veicolo? "))

M1 = Motociclo(modello, cilindrata, alimentazione, tempi_motore, prezzo)

M1.info()

C1 = Ciclomotore(modello, cilindrata, alimentazione, tempi_motore, prezzo)

C1.info()