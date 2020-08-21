#escreva um programa que leia um valor em metros e o exiba convertido para centímetros e milímetros.

metro = float(input('Digite o valor em metros: '))
centimetro = metro * 100
milimetro = metro * 1000
print('{:.2f} metros equivale a {:.2f} centímetros e {:.2f} milímetros.'.format(metro, centimetro, milimetro))
