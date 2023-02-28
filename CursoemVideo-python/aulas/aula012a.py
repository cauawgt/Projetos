# CONDIÇÔES ANINHADAS

nome = str(input('Qual é o seu nome? '))

if nome == 'Caua':
    print('Lindo nome.')
elif nome == 'Caua Wallacy': # elif pode ser usado diversas vezes
    print('Muito específico, hein... ')
else:
    print('Nome normal')

print('Tenha um bom dia, {}!' .format(nome))
