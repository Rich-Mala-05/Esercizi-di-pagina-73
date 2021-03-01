class Triangolo:
    def __init__(self, lato1, lato2, base):
        self.lato1 = lato1
        self.lato2 = lato2
        self.base = base

    def perimetro_t_scaleno(self):
        return self.lato1 + self.lato2 + self.base

class TriangoloIsoscele(Triangolo):
    def __init__(self, lato1, base):
        super().__init__(lato1, base, base)

    def perimetro_t_isoscele(self):
        return self.lato1 * 2 + self.base

class TriangoloEquilatero(TriangoloIsoscele):
    def __init__(self, lato1):
        super().__init__(lato1, lato1)

    def perimetro_t_equilatero(self):
        return self.lato1**3

lato1 = round(float(input("Quanto è lungo il primo del triangolo scaleno in cm? ")),2)
lato2 = round(float(input("Quanto è lungo il secondo del triangolo scaleno in cm? ")),2)
base = round(float(input("Quanto è lunga la base del triangolo scaleno in cm? ")),2)
t_s_1 = Triangolo(lato1, lato2, base)
t_i_1 = TriangoloIsoscele(lato1, base)
t_e_1 = TriangoloEquilatero(lato1)

def info():
    print("Perimetro triangolo scaleno:", t_s_1.perimetro_t_scaleno(), "cm")
    print("Perimetro triangolo isoscele:", t_i_1.perimetro_t_isoscele(), "cm")
    print("Perimetro triangolo equilatero:", t_e_1.perimetro_t_equilatero(), "cm")

info()