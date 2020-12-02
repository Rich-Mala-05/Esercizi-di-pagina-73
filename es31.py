print("Numero decimale")
decimale = int(input())
cifre = []
binario = ""
quoziente = decimale
if quoziente != 0:    
    while quoziente != 0:
        resto = quoziente%2
        quoziente = int(quoziente/2)
        cifre.append(resto)
    cifre.reverse()
    for i in cifre:
        binario = binario + str(i)
else:
    binario = 0  
print('Metodo Malavasi:',binario)
print("Metodo python:  ", bin(int(decimale))[2:])