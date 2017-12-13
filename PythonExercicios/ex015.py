print('Exercício Python 015: '
      '\nEscreva um programa que pergunte a quantidade de Km percorridos por '
      '\num carro alugado e a quantidade de dias pelos quais ele foi alugado. '
      '\nCalcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.\n')

valordiaria = float(60)
valorkm = float(0.15)

kmpercorrido = float(input('Informe o total de KM pecorrido com o carro: '))
quantdiaria = float(input('Informe a quantidade de dias que esteve com o carro: '))

totalkm = kmpercorrido * valorkm
totaldiaria = valordiaria * quantdiaria
total = totaldiaria + totalkm

print('Conforme {:.0f} dias e {}KM pecorridos, teve um custo de R${:.2f} sobre os dias de aluguel e '
      'R${:.2f} sobre os KMs pecorridos.\n'.format(quantdiaria, kmpercorrido, totaldiaria, totalkm))

print('Total a pagar: R${:.2f} + R${:.2f} = R${}'.format(totalkm, totaldiaria, total))


