from time import sleep

print('Analisando Triângulo v2.0')
a = float(input('Informe o primero lado: '))
b = float(input('Informe o segundo lado: '))
c = float(input('Informe o terceiro lado: '))
print('-=-' * 20)
print('ANALISANDO')
print('-=-' * 20)
sleep(1)
if (a < b + c) and (b < a + c) and (c < a + b):
    print('EXISTE!')
    if a == b == c:
        print('É um Triãngulo Equilátero, ou seja, todos os lados iguais. ')
    elif ((a == b) and a != c) or ((a == c) and a != b) or ((b == c) and b != a):
        print('É um Triângulo Isósceles, ou seja, dois lados iguais e um diferente.')
    else:
        print('É um triângulo Escaleno, ou seja, todos os lados diferentes.')
else:
    print('Não é possível existir um triãngulo com esses comprimentos!')
