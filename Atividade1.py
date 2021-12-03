print("***********************************")
print("Sua Média :D")
print("***********************************", "\n")

print("Alo mundo", "\n")
nota1 = input("Digite a primeiro nota:")
nota2 = input("Digite a segunda nota:")
nota3 = input("Digite a terceira nota:")
nota4 = input("Digite a quarta nota:")
n1 = float(nota1)
n2 = float(nota2)
n3 = float(nota3)
n4 = float(nota4)

media = (n1+n2+n3+n4)/4
print("Sua média é:", media)
if(media >= 7):
    print("Você está na média! Parabens! :D")
else:
    print("Você está abaixo da média! Hora de melhorar.")
