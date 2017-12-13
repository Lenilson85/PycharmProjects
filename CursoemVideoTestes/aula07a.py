n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

# \n quebra linha dentro de um print
# , end = ' ' dentro do () do print não deixa quebra a linha

print('A soma é {},\n o produto é {} e a \ndivisão é {:.3f}'.format(s, m, d), end=' ')
print('Divisão inteira {} e potência {}'.format(di, e))
