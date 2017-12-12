msg1 = str('Desafio 004 - Curso em Video - Python')
msg2 = str('Crie um programa que leia algo e mostre o tipo primitivo e todas as informações possiveis!')

print(msg1)
print(msg2)

algo = input('Digite algo para que seja analisado: ')

print('Digitado é {} para tipo primitivo e {} para alfanumerico.'.format(type(algo), algo.isalnum()))
print('Digitado é {} para tipo primitivo e {} para alfa.'.format(type(algo), algo.isalpha()))
