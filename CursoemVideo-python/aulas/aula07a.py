# nome = str(input('Qual é seu nome? '))
# print('Prazer em te conhecer, {:=^20}.' .format(nome))

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
r = n1 % n2
p = n1 ** n2
print('a soma é {}\no produto é {}\na divisão é {:.3f}' .format(s, m, d), end='') # \n quebra - end= '' não quebra
print('\na divisão inteira é {}\no resto é {}\na potenciação é {}' .format(di, r, p))
