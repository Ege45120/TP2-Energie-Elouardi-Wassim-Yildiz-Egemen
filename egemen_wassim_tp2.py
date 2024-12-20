import csv
import matplotlib.pyplot as plt
table=[]
hc =[]

with open("RTE_2022.csv",newline='') as csvfile:
    reader=csv.reader(csvfile,delimiter=',')
    for row in reader:
        table.append(row)
del table[0]
for i in range(len(table)):
    heure = table[i][3]
    consommation = table[i][4]
    if consommation == '':
        consommation = '0'
    hc.append(heure.replace(":", "."))
    hc.append(float(consommation))
print(hc)

conso_0a5h = []
conso_5a10h = []
conso_10a15h = []
conso_15a20h = []
conso_20a0h = []


chiffre = len(hc)


for k in range(0, len(hc), 2):  
    consommation = hc[k + 1]
    if hc[k] != '':
        heure = float(hc[k])
    else:
        heure = 0.0 
    consommation = hc[k + 1] 
    
    if 0 <= heure < 5:
        conso_0a5h.append(consommation)
    if 5 <= heure < 10:
        conso_5a10h.append(consommation)
    if 10 <= heure < 15:
        conso_10a15h.append(consommation)
    if 15 <= heure < 20:
        conso_15a20h.append(consommation)
    if 20 <= heure < 24:
        conso_20a0h.append(consommation) 


print(conso_0a5h)
print(conso_5a10h)
print(conso_10a15h)
print(conso_15a20h)
print(conso_20a0h)


a = sum(conso_0a5h)/len(conso_0a5h)
b = sum(conso_5a10h)/len(conso_5a10h)
c = sum(conso_10a15h)/len(conso_10a15h)
d = sum(conso_15a20h)/len(conso_15a20h)
e = sum(conso_20a0h)/len(conso_20a0h)


consoma = []
heure = ["De minuit à 5h", "De 5h à 10h", "De 10h à 15h", "De 15h à 20h", "De 20h à 0h"]
consoma.append(a)
consoma.append(b)
consoma.append(c)
consoma.append(d)
consoma.append(e)

plt.plot(heure,consoma)
plt.show()











