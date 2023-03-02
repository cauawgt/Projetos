from time import sleep
soma_idades = 0
idade_maior_homem = 0
homem_mais_velho = ' '
cont_mulher = 0
for c in range(1, 5):
    print('{} Pessoa' .format(c))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = int(input('(1) - Masculino; (2) - Feminino: '))
    soma_idades += idade
    if sexo == 1:
       idade_maior_homem = idade
       homem_mais_velho = nome
       if idade > idade_maior_homem:
           homem_mais_velho = nome
    elif sexo == 2 and idade < 20:
            cont_mulher += 1
    else:
        homem_mais_velho = 'inexistente'
print('Analisando os dados...')
sleep(2)
print('')
print('Média de idade do grupo: {} anos' .format(soma_idades/4))
print('o homem mais velho é {}' .format(homem_mais_velho))
print('Há {} mulher(es) com menos de 20 anos.' .format(cont_mulher))
