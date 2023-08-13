# Escreva um programa que solicite ao usuário um número e verifique se ele é positivo, negativo ou
# igual a zero.

while True:
    
    num1 = int(input('Digite um número: '))
    if num1 % 2 == 0:
        print('O numero digitado é par')
    elif num1 ==0:
        print('O numero digitado é igual a zero')
    else:
        print('O número digitado é impar')
    break