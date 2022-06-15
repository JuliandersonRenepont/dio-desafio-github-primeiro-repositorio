#Dado um número inteiro positivo n, calcular a soma dos n primeiros
# números inteiros positivos

#leia o valor de n
n = int(input("Digite o valor de N: ")) 

#inicializa a soma
soma = 0

#calcule a soma

i = 1

while i <= n:
    soma += i
    i += 1



print("A soma dos, {} primeiros inteiros positivos é: {} ".format(n,soma))
