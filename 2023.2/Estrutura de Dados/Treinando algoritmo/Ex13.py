# Escreva um programa que solicite ao usuário um número e exiba a tabuada desse número, de 1 a
# 10.

numero = int(input('Digite um número: '))
print(f'Tabuada do {numero}')
for i in range(1,11):
    resultado = i * numero
    print(f'{numero} X {i} = {resultado}')
