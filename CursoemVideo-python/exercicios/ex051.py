print('Progressão Aritmética (P.A')
a1 = int(input('Primeiro termo: '))
n = int(input('Posição do ultímo termo: '))
r = int(input('Razão: '))
an = a1 + n * r
for c in range(a1, an, r):
    print(c, end=' ')
