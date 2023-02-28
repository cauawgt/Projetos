from time import sleep

valor_casa = float(input('Informe o valor da casa: R$'))
salario_comprador = float(input('Informe seu salário: R$'))
anos_pag = int(input('Em quantos anos pretende financiar: '))

prest_mensal = valor_casa / (anos_pag * 12)
print('-=-' * 20)
print('Analisando...')
print('-=-' * 20)
sleep(3)

if prest_mensal > (0.3 * salario_comprador):
    print('Empréstimo negado! A Prestação mensal de R${:.2f} EXCEDEU 30% do seu salário.' .format(prest_mensal))
else:
    print('Parábens! Empréstimo Bancário CONCEDIDO.\nPrestação Mensal: R${:.2f}' .format(prest_mensal))
print('--FIM--')
