from random import choice

a1 = str(input('Informe o primeiro aluno: '))
a2 = str(input('Informe o segundo aluno: '))
a3 = str(input('Informe o terceiro aluno: '))
a4 = str(input('Informe o quarto aluno: '))
escolhido = choice([a1, a2, a3, a4])
print('O aluno sorteado foi {}.' .format(escolhido))


