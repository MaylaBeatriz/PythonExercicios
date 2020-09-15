#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

celsius = float(input('Digite a temperatura em Celsius: '))
celsius_em_fahrenheit = 9 * celsius / 5 + 32
print('A temperatura de {:.1f}°C equivale a {:.1f}°F'.format(celsius, celsius_em_fahrenheit))
