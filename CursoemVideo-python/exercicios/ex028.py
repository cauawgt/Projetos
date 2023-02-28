import random
from time import sleep

num_escolhido = random.randint(0, 5)
print('-=-' * 20)
print('Pensei em um número entre 0 e 5')
print('-=-' * 20)
entrada = int(input('Tente advinhar: '))
print('PROCESSANDO...')
sleep(2)
if entrada == num_escolhido:
    print('OOOH! Você me venceu.')
else:
    print('Você perdeu. Boa sorte na próxima!')
print('Número da maquina: {}' .format(num_escolhido))
