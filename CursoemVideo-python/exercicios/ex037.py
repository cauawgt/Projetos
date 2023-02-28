from time import sleep

num = int(input('Informe um número: '))
print('')
print('Opções de Conversão de base: ')
print('1 - Binário')
print('2 - Octal')
print('3 - Hexadecimal')
print('')
opc_escolhida = int(input('Digite a opção desejada: '))
print('Convertendo...')
sleep(1)
print('')


if opc_escolhida == 1:
    print('{} equivale a {} em binário.' .format(num, bin(num)[2:]))
elif opc_escolhida == 2:
    print('{} equivale a {} em octal' .format(num, oct(num)[2:]))
elif opc_escolhida == 3:
    print('{} equivale a {} em hexadecimal' .format(num, hex(num)[2:]))
else:
    print('Não identificamos essa opção no Banco de Dados. Tente novamente.')
