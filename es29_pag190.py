print("Inserire il proprio reddito")
reddito = int(input())
if reddito <= 15000:
    imposta = reddito*0.23
elif reddito > 15000 and reddito <= 28000:
    imposta = (reddito-15000)*0.27 + 3450
elif reddito > 28000 and reddito <= 55000:
    imposta = (reddito-28000)*0.38 + 6960
elif reddito > 55000 and reddito <= 75000:
    imposta = (reddito-55000)*0.41 + 17220
elif reddito > 75000:
    imposta = (reddito-75000)*0.43 + 25420
print("L'imposta è:", imposta)

