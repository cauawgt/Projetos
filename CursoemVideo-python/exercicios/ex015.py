d = int(input('Quantos dias alugados? '))
km = float(input('Quantos KM rodados? '))
c_d = 60 * d
c_km = 0.15 * km
c_total = c_d + c_km
print('Total a pagar: R${}' .format(c_total))
