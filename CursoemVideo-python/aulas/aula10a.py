tempo = int(input('Quantos anos tem seu carro? '))

if tempo <= 3:
    print('Seu carro está novinho!')
else:
    print('Tá velho, hein...')

# Condição simplificada
# print('carro novo' if tempo <= 3 else 'carro velho')
print('--FIM--')

nome = str(input('Qual é o seu nome? '))
if nome == 'Caua':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é comum')
print('Bom dia, {}' .format(nome))

n1 = float(input('Informe a primeira nota do {}: ' .format(nome)))
n2 = float(input('Informe a segunda nota do {}: ' .format(nome)))
m = (n1 + n2) / 2
if m >= 7:
    print('Parabens! Você está aprovado')
else:
    print('Infelizmente você não atingiu a média necessária.')