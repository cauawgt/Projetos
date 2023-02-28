valor_normal = float(input('Preço das Compras: R$'))
print('FORMA DE PAGAMENTO: ')
print('[1] - à vista dinheiro/cheque ')
print('[2] - à vista no cartão ')
print('[3] - em até 2x no cartão ')
print('[4] - 3x ou mais no cartão ')
form_pag = float(input('Informe a opção: '))

if form_pag == 1:
    novo_valor = valor_normal * 0.9 # 10% de desconto
    print('Valor a pagar: R${}' .format(novo_valor))
elif form_pag == 2:
    novo_valor = valor_normal * 0.95 # 5% de desconto
    print('Valor a pagar: R${}' .format(novo_valor))
elif form_pag == 3:
    print('Valor a pagar: R${}' .format(valor_normal))
elif form_pag == 4:
    n_parcela = int(input('Quantas parcelas: '))
    novo_valor = valor_normal * 1.2 # 20% de juros
    valor_parc = novo_valor / n_parcela
    print('Compra parcelada em {}x de R${}\nValor a pagar: R${}' .format(n_parcela, valor_parc, novo_valor))
else:
    print('Não temos essa opção. Tente novamente!')