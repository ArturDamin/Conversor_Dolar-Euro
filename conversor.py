print("******************")
print("Conversor de Reais")
print("******************")

print("Escolha sua Moeda")
moeda = int(input("(1)Dolar (2)Euro : "))

dolar = 5.14
euro = 5.82

real = int(input("Valor em real: R$"))

if(moeda == 1):
    resultado_realdolar = real / dolar
    print("{:.2f}".format(resultado_realdolar))
elif(moeda == 2):
    resultado_realeuro = real / euro
    print("{:.2f}".format(resultado_realeuro))
