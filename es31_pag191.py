zone = ["Nord", "Centro", "Sud", "Isole"]
fatturati = []
for e in zone:
    print("Inserire fatturato zona", e)
    fatturato = int(input())
    fatturati.append(fatturato)
print("Fatturato totale:", sum(fatturati))
for index in range(4):
    print("Percentuale fatturato fona", zone[index], round(fatturati[index]*100/sum(fatturati),2),"%")