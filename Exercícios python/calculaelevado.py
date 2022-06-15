"""
Dados números inteiros n e k, com k >= 0,
calcular n elevado a k. Por exemplo, dados os números 3 e 4
o seu programa deve escrever o número 81.
"""
def main():
    n = int(input("Digite um número inteiro: "))
    k = int(input("Digite um número inteiro: "))

    while k >= 0:
        quad = n ** k
    print(quad)
main()    
    
