n1 = int(input('Informe um número: '))
n2 = int(input('Informe outro número: '))
print('Comparando...')
if n1 > n2:
    print('{} é maior que {}' .format(n1, n2))
elif n2 > n1:
    print('{} é maior que {}' .format(n2, n1))
else:
    print('Os dois valores informados são iguais')
print('--FIM--')
