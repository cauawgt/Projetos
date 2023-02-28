d = float(input('Qual a distância da sua viagem em KM? '))
if d <= 200:
    p = d * 0.5
    print('Preço da passagem: R${}' .format(p))
else:
    p = d * 0.45
    print('Preço da passagem: R${}'.format(p))
print('Boa viagem!')
