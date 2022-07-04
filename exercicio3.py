Dia = []
Volume = []
quarta = 0
soma = 0
somaT = 0

for i in range(15):
    dia = input("Digite o dia da semana: ")
    Dia.append(dia)
    vol = float(input("Digite o volume de chuvas: "))
    Volume.append(vol)
    somaT += vol
    if dia == "quarta-feira" or dia == "Quarta-feira":
        quarta += 1
        soma += vol

media = soma / quarta

print("A media do volume de chuvas de quarta feira é:", media)

print("A soma de total dos volumes de chuva é:", somaT)
