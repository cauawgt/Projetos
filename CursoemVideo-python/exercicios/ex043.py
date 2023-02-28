p = float(input('Peso: KG'))
h = float(input('Altura: m'))

imc = p / (h ** 2)

print('')
if imc < 18.5:
    print('IMC: {:.1f}' .format(imc))
    print('Abaixo do peso')
elif imc < 25:
    print('IMC: {:.1f}'.format(imc))
    print('Peso ideal')
elif imc <= 30:
    print('IMC: {:.1f}'.format(imc))
    print('Sobrepeso')
elif imc <= 40:
    print('IMC: {:.1f}'.format(imc))
    print('Obesidade')
else:
    print('IMC: {:.1f}'.format(imc))
    print('Obesidade Mórbida')
