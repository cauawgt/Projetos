from datetime import date
from time import sleep
print('DATA DE NASCIMENTO')
ano_nasc = int(input('Ano: '))

idade = date.today().year - ano_nasc
print('-=-' * 20)
print('ANALISANDO...')
print('-=-' * 20)
sleep(1)
if idade == 18:
    print('O cidadão completará ou já completou {} anos nesse ano de {}' .format(idade, date.today().year))
    print('e DEVERÁ REALIZAR O ALISTAMENTO MILITAR! ')
elif idade < 18:
    ano_de_alist = (ano_nasc + 18)
    print('O cidadão ainda não completou 18 anos')
    print('Sua idade atual é {} anos e deverá realizar o alistamento militar no ano de {}' .format(idade, ano_de_alist))
    print('Intervalo de {} ano(s) até lá! Estamos Aguardando.' .format(ano_de_alist - date.today().year))
else:
    ano_de_alist = (ano_nasc + 18)
    print('Você deve IMEDIATAMENTE realizar o alistamento militar de forma presencial!')
    print('Já excedeu {} ano(s) do tempo limite' .format((ano_de_alist - date.today().year) * -1))
