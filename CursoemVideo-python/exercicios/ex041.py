from datetime import date

nasc = int(input('Informe a data de nascimento: '))
idade = date.today().year - nasc

if idade <= 9:
    print('atleta MIRIM')
elif idade <= 14:
    print('atleta INFANTIL')
elif idade <= 19:
    print('atleta JÚNIOR')
elif idade <= 25:
    print('atleta SÊNIOR')
else:
    print('atleta MASTER')
