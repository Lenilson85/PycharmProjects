msg1 = str('Desafio 003 - Curso em Video - Python')
msg2 = str('Crie um programa que leia dois numeros e mostre a soma entre eles!')

print(msg1)
print(msg2)

n1 = float(input('Digite um valor: '))
n2 = float(input('Digite o segundo valor: '))

soma = n1+n2

resp = str('A soma entre {} e {} é igual a: {}!'.format(n1, n2, soma))

print(resp)
