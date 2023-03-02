import random
print('-=-' * 20)
print('JOGO DA ADIVINHAÇÂO')
print('-=-' * 20)
f = 0
tentativas = 0
while f != 1:
    pense_maq = random.randint(0, 10)
    print('')
    n = int(input('Informe um valor entre 0 e 10: '))
    if n == pense_maq:
        print('Pensamento da máquina: {}' .format(pense_maq))
        f = 1
        tentativas += 1
    else:
        print('Pensamento da máquina: {}' .format(pense_maq))
        print('Tente novamente!')
        tentativas += 1
print('')
print('PARABÉNS!\nQuantidade de tentativas: {}' .format(tentativas))
