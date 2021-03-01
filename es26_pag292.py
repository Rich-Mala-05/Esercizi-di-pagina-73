class Quadrato:

    def __init__(self, lato):
        self.lato = lato

    def perimetro(self):
        return self.lato*4

    def area(self):
        return self.lato**2

class Rettangolo(Quadrato):
    def __init__(self, lato, lato2):
        super().__init__(lato)
        self.lato2 = lato2
        
    def perimetro_rettangolo(self):
        return (self.lato + self.lato2) * 2

    def area_rettangolo(self):
        return self.lato * self.lato2

lato = round(float(input("Quanto è lungo il lato del quadrato in cm? ")),2)

q1 = Quadrato(lato)

print("Perimetro quadrato:", q1.perimetro(), "cm")

print("Area quadrato:", round(q1.area(),2), "cm")

base = round(float(input("Quanto è lunga la base del rettangolo in cm? ")),2)

altezza = round(float(input("Quanto è lunga l'altezza del rettangolo in cm? ")),2)

r1 = Rettangolo(base, altezza)

print("Perimetro rettangolo:", r1.perimetro_rettangolo(), "cm")

print("Area rettangolo:", round(r1.area_rettangolo(),2), "cm")