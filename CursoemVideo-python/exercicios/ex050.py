soma = 0
cont = 0
for c in range(0, 6):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        cont += 1
        soma += num
print('Quantidade de pares: {}\nSoma: {}' .format(cont, soma))
