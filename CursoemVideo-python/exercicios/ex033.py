from time import sleep
n1 = float(input('Digite o 1 número: '))
n2 = float(input('Digite o 2 número: '))
n3 = float(input('Digite o 3 número: '))
print('Analisando...')
sleep(2)

if (n1 >= n2) and (n1 >= n3):
    print('Maior: {}' .format(n1))
elif (n2 >= n1) and (n2 >= n3):
    print('Maior: {}' .format(n2))
else:
    print('Maior: {}' .format(n3))

if (n1 <= n2) and (n1 <= n3):
    print('Menor: {}' .format(n1))
elif (n2 <= n1) and (n2 <= n3):
    print('Menor: {}' .format(n2))
else:
    print('Menor: {}' .format(n3))
