'''
entrada = input('Digite o nome da sua cidade: ')
dividir = entrada.lower().split()
n_santo = 'santo' in dividir[0]
print('
Sua Cidade começa com a palavra Santo? {} ' .format(n_santo))
'''

cid = str(input('Em que cidade você nasceU? ')).strip()
print(cid[:5].upper() == 'SANTO')
