frase = 'Curso em Video Python'
print(len(frase)) # comprimento
print(frase.count('o')) # conta uma certa letra
print(frase.count('o', 0, 13)) # conta com fatiamento
print(frase.find('deo'))
print(frase.find('Android')) # -1 significa que não existe
print('Curso' in frase)

# TRANFORMAÇÃO
print(frase.replace('Python', 'Java'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize()) # Só o primeiro em maiúscula
print(frase.title()) # title é diferente de capitalize

frase2 = '   Aprenda Python  '
print(frase2.strip()) # remove espaços inuteis
print(frase2.rstrip()) # remove espaços inuteis apenas do lado direito
print(frase2.lstrip()) # remove espaços inuteis apenas do lado esquerdo

# Divisão
print(frase.split()) # dividir uma string em uma lista

# Junção
print(''.join(frase))





