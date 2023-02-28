n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
m = (n1 + n2) / 2

if m >= 7:
    print('APROVADO! Parabéns pelo ótimo resultado.')
    print('Média: {}' .format(m))
elif (m >= 5) and (m <= 6.9):
    print('RECUPERAÇÂO! Estude mais.')
    print('Média: {}'.format(m))
else:
    print('REPROVADO! Infelizmente não atingiu a média necessária.')
    print('Média: {}'.format(m))
