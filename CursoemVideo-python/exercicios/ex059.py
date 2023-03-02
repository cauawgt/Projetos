parar = 0
while parar != 5:
    print('')
    n1 = float(input('Informe um valor: '))
    n2 = float(input('Informe um outro valor: '))
    print('-' * 22)
    print('[1] - Somar')
    print('[2] - Multiplicar')
    print('[3] - Maior')
    print('[4] - Menor')
    print('[5] - Sair do programa')
    print('-' * 22)
    opc = int(input('Informe a opção: '))
    print('')
    if opc == 1:
        soma = n1 + n2
        print('A soma entre {} e {} vale {}' .format(n1, n2, soma))
    elif opc == 2:
        produto = n1 * n2
        print('O produto entre {} e {} vale {}' .format(n1, n2, produto))
    elif opc == 3:
        if n1 > n2:
            print('{} é maior que {}' .format(n1, n2))
        else:
            print('{} é maior que {}' .format(n2, n1))
    elif opc == 4:
        if n1 < n2:
            print('{} é menor que {}' .format(n1, n2))
        else:
            print('{} é menor que {}' .format(n2, n1))
    elif opc == 5:
        parar = 5
        print('Programa encerrado!')
    else:
        print('Opção não identificada. Tente novamente!')
