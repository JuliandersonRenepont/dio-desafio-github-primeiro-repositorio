n = int(input("Digite um número: "))

aux = 1

for i in range(aux, n+1):
    if i % 2 == 1:
        impar = i
        print("Os números {} são ímpares:".format(impar))
    elif i % 2 == 0:
        par = i
        print("Os números {} são ímpares:".format(par))
        
        
print(impar)
print(par)
