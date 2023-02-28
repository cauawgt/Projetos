salario = float(input('Informe o seu salário: R$'))
print('Analisando...')
if salario > 1250:
    novo_salario = salario * 1.1
    print('Você recebeu um aumento de 10%\nSalário: R${:.2f}' .format(novo_salario))
else:
    novo_salario = salario * 1.15
    print('Você recebeu um aumento de 15%\nSalário: R${:.2f}' .format(novo_salario))
print('--FIM--')
