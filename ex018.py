# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
# cosseno e tangente desse ângulo. Dica: módulo ?
import math

angulo = float(input('Informe o ângulo: '))

print('O seno de {} é {}, o cosseno é {}, e a tangente é {}.'.format(angulo, math.sin(angulo), math.cos(angulo), math.tan(angulo)))
