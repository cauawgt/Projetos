frase = str(input(('Digite uma frase: '))).upper()
junto = frase.replace(' ', '')
inverso = junto[::-1]
if junto == inverso:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')
