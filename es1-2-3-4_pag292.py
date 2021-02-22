class Atleta:
    
    def __init__(self, nome):
        self.nome = nome
        self.visitaMedica = False
        self.squadra = "Nessuna squadra"
    
    def scegli_squadra(self, s):
        self.squadra = s
    
    def effettua_visita(self, v): 
        self.visitaMedica = v
    
    def dati(self):
        print("Giocatore:", self.nome)
        print("Squadra:", self.squadra)
        print("Visita metica:", self.visitaMedica)

print("Come ti chiami?")
nome = input()
a1 = Atleta(nome)

print("Di quale squadra vuoi fare parte? (Lascia vuoto se non hai una squadra)")
nome_squadra = input()
a1.scegli_squadra("VBSM")

print("Hai effettuato la visita medica? (Rispondi con 1 o 2)")
print("1. Sì")
print("2. No")
visita = int(input())
if visita == 1:   
   a1.effettua_visita(True)

a1.dati()