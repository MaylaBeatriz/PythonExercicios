#desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média.

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print('A média do aluno é {:.2f}'.format(media))
