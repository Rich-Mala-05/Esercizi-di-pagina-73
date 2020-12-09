'''
Scrivi un programma che a scelta dall'utente calcoli l'area di un quadrato, rettangolo, triangolo o cerchio.
'''
print("Quale area vuoi calcolare?")
print("1 = quadrato")
print("2 = rettangolo")
print("3 = triangolo")
print("4 = cerchio")
figura = input()
if figura == "1":
    print("Scrivi la misura del lato del quadrato in cm")
    latoquadrato = round(float(input()),2)
    print("L'area del quadrato è",latoquadrato**2,"cm2")
elif figura == "2":
    print("Scrivi la misura dei lati del rettangolo in cm")
    latolungo = round(float(input()),2)
    latocorto = round(float(input()),2)
    print("L'area del rettangolo è",latolungo*latocorto,"cm2")
elif figura == "3":
    print("Scrivi la misura della base del triangolo in cm")
    base = round(float(input()),2)
    print("Scrivi la misura dell'altezza del triangolo in cm")
    altezza = round(float(input()),2)
    print("L'area del triangolo è",(altezza*base)/2,"cm2")
else:
    print("Scrivi la misura del raggio del cerchio in cm")
    raggio = round(float(input()),2)
    print("L'area del cerchio è",(raggio**2)*3.14,"cm2")