import re

pattern_in = re.compile(r"(0|-?[1-9][0-9]*)")
milhar = input("Digite uma milhar: ")

if pattern_in.match(milhar):
    lista =[]
    num = int(milhar)
    for i in num:
        i // 10
    
else:
    print(milhar,"Não é um número inteiro")
    milhar = int(input("Digite uma milhar: "))
    
