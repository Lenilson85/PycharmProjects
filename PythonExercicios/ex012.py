print('Exercício Python 012: \nFaça um algoritmo que leia o preço de um produto \ne mostre seu novo preço, com 5% de desconto. \n')

preço = float(input('Digie o valor do produto R$:'))

desconto = preço * 5 / 100

preçonovo = preço - desconto

print('\nO valor do produto com 5% de desconto é: R$ {:.2f}'.format(preçonovo))
