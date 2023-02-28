from random import choice
from emoji import emojize

print('JOKENPÔ - DESAFIO')
print('-' * 20)
print(emojize('[1] - Pedra :white_large_square:'))
print(emojize('[2] - Papel :page_facing_up:'))
print(emojize('[3] - Tesoura :scissors:'))
opc = int(input('Qual sua opção: '))
print('-' * 20)
opc_computador = choice(['Pedra', 'Papel', 'Tesoura'])

if opc == 1:
    if opc_computador == 'Pedra':
        print('DEU EMPATE!')
        print('Sua escolha: Pedra')
        print('Escolha da Máquina: {}' .format(opc_computador))
    elif opc_computador == 'Papel':
        print('VOCÊ PERDEU!')
        print('Sua escolha: Pedra')
        print('Escolha da Máquina: {}'.format(opc_computador))
    elif opc_computador == 'Tesoura':
        print('VOCÊ GANHOU!')
        print('Sua escolha: Pedra')
        print('Escolha da Máquina: {}'.format(opc_computador))
elif opc == 2:
    if opc_computador == 'Pedra':
        print('VOCÊ VENCEU!')
        print('Sua escolha: Papel')
        print('Escolha da Máquina: {}' .format(opc_computador))
    elif opc_computador == 'Papel':
        print('DEU EMPATE!')
        print('Sua escolha: Papel')
        print('Escolha da Máquina: {}'.format(opc_computador))
    elif opc_computador == 'Tesoura':
        print('VOCÊ PERDEU!')
        print('Sua escolha: Papel')
        print('Escolha da Máquina: {}'.format(opc_computador))
elif opc == 3:
    if opc_computador == 'Pedra':
        print('VOCÊ PERDEU!')
        print('Sua escolha: Tesoura')
        print('Escolha da Máquina: {}' .format(opc_computador))
    elif opc_computador == 'Papel':
        print('VOCÊ VENCEU!')
        print('Sua escolha: Tesoura')
        print('Escolha da Máquina: {}'.format(opc_computador))
    elif opc_computador == 'Tesoura':
        print('VOCÊ EMPATE!')
        print('Sua escolha: Tesoura')
        print('Escolha da Máquina: {}'.format(opc_computador))
else:
    print('Não existe essa opção.')