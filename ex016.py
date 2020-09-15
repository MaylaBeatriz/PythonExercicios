# Crie um programa que leia um número real qualquer pelo teclado e mostre
# na tela a sua porção inteira. Dica: módulo math.

import math

numero = float(input('Digite um número real qualquer: '))
parte_inteira = math.floor(numero)
print('A parte inteira de {} é {}'.format(numero, parte_inteira))
