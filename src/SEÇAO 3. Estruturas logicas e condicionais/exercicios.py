from math import sqrt

'''
Exercicios
'''

'''
1.Faca um programa que receba 2 numeros inteiros e mostre qual deles é maior.
'''
print("NUMERO MAIOR OU MENOR:")
inteiro1: int = int(input("Digite um valor inteiro: "))
inteiro2: int = int(input("Digite outro numero: "))

maior = inteiro1
if inteiro2 > maior:
    maior = inteiro2
elif inteiro2 == maior:
    print("Os valores são iguais.")
else:
    print(f"O maior valor digitado é: {maior}")


'''
2.Faca um programa que leia 1 numero inteiro fornecido pelo usuario. Se esse
numero for positivo, calcule a raiz quadrada do numero e apresente-a. Se o
numero for negativo, mostre uma mensagem dizendo que o numero é inválido.
'''
print()
print("RAIZ QUADRADA DE UM NUMERO:")
valor: int = int(input("Digite um valor: "))

if valor > 0:
    print(f"Raiz quadrada de {valor}: {sqrt(valor)}")
else:
    print("Numero inválido...")


'''
3.Faça um programa que recebe um inteiro e informe se este é par ou impar.
'''
print()
print("NUMERO PAR OU IMPAR:")
inteiro: int = int(input("Informe um numero: "))

if inteiro % 2 == 0:
    print("O numero digitado é: par")
else:
    print("O numero digitado é: impar")
