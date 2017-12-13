print('Exercício Python 013: \n Faça um algoritmo que leia o salário de um funcionário \n e mostre seu novo salário, com 15% de aumento. \n')

salario = float(input('Qual o salario do funcionario? R$ '))

novosalario = salario + (salario * 15 /100)

print('Seu novo salario com aumento de 15% é: R$ {:.2f}'.format(novosalario))
