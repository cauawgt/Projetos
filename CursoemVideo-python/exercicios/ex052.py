num = int(input('Digite um número: '))
cont_d = 0
for c in range(1, num+1):
    if num % c == 0:
        cont_d += 1
    print('{}' .format(c), end=' ')

if cont_d == 2:
    print('\n{} foi divisível {} vezes, por isso é primo.' .format(num, cont_d))
else:
    print('\n{} foi divisível {} vezes, por isso não é primo.' .format(num, cont_d))

