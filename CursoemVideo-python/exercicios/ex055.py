menor_peso = 1000000
maior_peso = 0
for c in range(1, 6):
    peso = float(input('Informe o peso da {} pessoa: Kg' .format(c)))
    if peso > maior_peso:
        maior_peso = peso
    if peso < menor_peso:
        menor_peso = peso
print('Maior Peso: Kg{}\nMenor Peso: Kg{}' .format(maior_peso, menor_peso))
