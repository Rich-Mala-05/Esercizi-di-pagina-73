class Quadrato:

    def __init__(self, lato):
        self.lato = lato

    def perimetro(self):
        return self.lato*4

    def area(self):
        return self.lato**2

lato = round(float(input("Quanto è lungo il lato del quadrato in cm? ")),2)

q1 = Quadrato(lato)

print("Perimetro:", q1.perimetro(), "cm")

print("Area:", round(q1.area(),2), "cm")