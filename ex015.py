# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
# quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

quilometros_percorridos = float(input('Informe a quantidade de quilômetros percorridos: '))
dias_alugados = int(input('Por quantos dias o carro foi alugado? '))
diaria = 60 * dias_alugados
preco_quilometro = 0.15 * quilometros_percorridos
preco_final = diaria + preco_quilometro
print('O aluguel de {} dias, com {:.1f}Km rodados, ficou em R${:.2f}'.format(dias_alugados, quilometros_percorridos, preco_final))
