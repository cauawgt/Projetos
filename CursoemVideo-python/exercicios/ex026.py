entrada = str(input('Digite uma frase: ')).strip()

frase = entrada.lower()

print('A vogal "a" aparece {} na frase digitada. ' .format(frase.count('a')))
print('Primeira aparição na posição {}.' .format(frase.find('a')+1))
print('Ultíma aparição na posição {}.' .format(frase.rfind('a')+1))

