temp = []
contador = 0 

while True:
    Temp = float(input("Digite a temperatura: "))
    temp.append(Temp)
    if Temp < 0:
        break

tempM = float(input("Digite a temperatura minima: "))

for i in temp:
    if i > tempM:
        contador +=1

print("%.0f dias superaram a temperatura minima" % (contador))