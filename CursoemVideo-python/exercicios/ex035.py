print('CONDIÇÃO DE EXISTÊNCIA DE UM TRIÂNGULO')
a = float(input('Informe o comprimento de um lado: '))
b = float(input('Informe o comprimento de outro lado: '))
c = float(input('Informe o comprimento do ultímo lado: '))

if (a < (b + c)) and (b < (a + c)) and (c < (a + b)):
    print('Triângulo existe')
else:
    print('Não é possível existir um triângulo')
