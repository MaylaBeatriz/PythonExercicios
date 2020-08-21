#crie um algoritmo que leia um número e mostre: seu dobro, triplo e raiz quadrada.

numero = int(input('Digite um número: '))
dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1/2) #pow(n, (1/2))
print('Número informado: {}'.format(numero))
print('Dobro: {}'.format(dobro), '\nTriplo: {}'.format(triplo), '\nRaiz quadrada: {:.2f}'.format(raiz))
