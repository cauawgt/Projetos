''' Minha Resposta

nome_completo = str(input('Digite seu nome completo: '))
print(nome_completo.upper())
print(nome_completo.lower())

let_tot = len(nome_completo.replace(' ', ''))
print('Quantidade de letras: {}' .format(let_tot))

nome_div = nome_completo.split()
print('Quantidade de letras no primeiro nome: {}' .format(len(nome_div[0])))
'''


nome = str(input('Digite seu nome Completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}' .format(nome.upper()))
print('Seu nome em minúsculas é {}' .format(nome.lower()))
print('Seu nome tem ao todo {} letras' .format(len(nome) - nome.count(' ')))
# print('Seu primeiro nome tem {} letras' .format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras' .format(separa[0], len(separa[0])))
