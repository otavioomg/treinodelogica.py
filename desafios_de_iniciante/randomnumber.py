import random

numero_secreto = random.randint(1, 100)
tentativas = 0
acertou = False
print("Bem-vindo ao jogo de adivinhação!")
print("Estou pensando em um número entre 1 e 100.")

# numero = int(input("Adivinhe um número de 1 a 100: "))
# tentativas += 1

while True:
    numero = int(input("Adivinhe um número de 1 a 100: "))
    tentativas += 1
    if tentativas > 0:
        print("Tente de novo!")
    if numero == numero_secreto:
        print("Parabéns você conseguiu em", tentativas, "tentativas!")
        acertou == True
        break
    elif numero < numero_secreto:
        print("número maior")
    else:
        print("número menor")
    