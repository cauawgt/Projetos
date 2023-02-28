from datetime import date
from time import sleep

cont_maioridade = 0
cont_menoridade = 0
for c in range(1, 8):
    ano_nascimento = int(input('Informe ano de nascimento da {} pessoa: ' .format(c)))
    if date.today().year - ano_nascimento >= 21:
        cont_maioridade += 1
    else:
        cont_menoridade += 1
print('Aguarde...')
sleep(2)
print('')
print('Foram registradas {} pessoas.' .format(cont_menoridade + cont_maioridade))
print('Dessas pessoas, {} atingiram a Maioridade, enquanto {} ainda são menores de idade' .format(cont_maioridade, cont_menoridade))
