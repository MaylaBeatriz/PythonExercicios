#faça um programa que leia um número inteiro e mostre na tela o seu antecessor e sucessor.

numero = int(input('Digite um número inteiro: '))
antecessor = numero - 1
sucessor = numero + 1
print('Antecessor: {} - '.format(antecessor), 'Número informado: ', numero, ' - Sucessor: {}'.format(sucessor))
