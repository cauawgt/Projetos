parar = 0
while parar != 1:
    sexo = str(input('Informe seu sexo [M/F]: ')).upper()
    if sexo == 'M' or sexo == 'F':
        parar = 1
    else:
        print('Não identificamos essa opção. Tente novamente!')
print('Finalizado')

