print("-"*51)
print("Digite uma sequência de valores terminadas por zero")
print("-"*51)
soma = 0
valor = 1
contador = 1
while valor != 0:
    valor = int(input(f"\nEntre com o {contador}º valor a ser somado: "))
    soma += valor
    contador += 1
print(f"\nA soma dos valores digitados é: {soma}")    
                
