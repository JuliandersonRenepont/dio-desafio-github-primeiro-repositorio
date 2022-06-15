"""
    Dada uma sequência de números inteiros diferentes de zero,
    terminada por um zero, calcular a sua soma.
    Por exemplo, para a sequência: 12   17   4   -6   8   0
"""
def main():
    n = int(input("Digite um inteiro: "))
    soma = 0
    while n != 0:
        soma += n
        n = int(input("Digite um inteiro: "))
    print("A soma é: ", soma)
main()    
