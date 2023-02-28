menor = 0
maior = 0
for c in range(1, 6):
    peso = float(input('Informe o peso da {} pessoa; Kg'))
    if c == 1:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('-' * 20)
print('MAIOR: Kg{}\nmenor: Kg{}' .format(maior, menor))
