# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
# de um triângulo, calcule e mostre o comprimento da hipotenusa. Dica: módulo math.
import math

a = float(input('Informe o cateto oposto: '))
b = float(input('Informe o cateto adjacente: '))
hipotenusa = math.hypot(a, b)

print('O valor da hipotenusa é {}'.format(hipotenusa))
