import math

c_op = float(input('Informe o cateto oposto: '))
c_ad = float(input('Informe o cateto adjacente: '))
# h = ((c_op**2) + (c_ad**2)) ** (1/2)
h = math.hypot(c_op, c_ad)
print('hipotenusa vale {:.2f}' .format(h))

