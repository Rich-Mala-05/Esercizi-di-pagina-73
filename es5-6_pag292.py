class Prodotto:
    
    def __init__(self, tipo, peso, marca, taglia, stagione):
        self.tipo = tipo
        self.peso = peso
        self.marca = marca
        self.taglia = taglia
        self.stagione = stagione

    def assegna_prezzo(self):
        print("Hai chiesto alla cassiera quanto costa questo capo di abbigliamento")
        prezzi = [100,120,135,150,165,180]
        import random
        self.prezzo = random.choice(prezzi)
        print("Lei ti rispondere che costa", self.prezzo, "$")
    
    def info(self):
        print("Tipo:", self.tipo)
        print("Peso:", self.peso)
        print("Marca:", self.marca)
        print("Taglia:", self.taglia)
        print("Stagione:", self.stagione)
        print("Prezzo:", self.prezzo)

tipo1 = input("Quale capo di abbigliamento stai cercando? ")
peso1 = int(input("Indica il peso in grammi dell'indumento che cerchi "))
marca1 = input("Quale marca cerchi ")
taglia1 = input("Di che taglia hai bisogno? (S, M, L) ")
stagione1 = input("Cerchi un prodotto per l'inverno o per l'estate? ")

p1 = Prodotto(tipo1, peso1, marca1, taglia1, stagione1)

p1.assegna_prezzo()

p1.info()

