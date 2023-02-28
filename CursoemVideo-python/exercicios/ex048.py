s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c # s = s + c (Acumulador)
        cont += 1 # (Contador)
print('Números ímpares e múltiplos de 3 no intervalo de 1 até 500')
print('Quantidade: {}' .format(cont))
print('Soma: {} ' .format(s))
