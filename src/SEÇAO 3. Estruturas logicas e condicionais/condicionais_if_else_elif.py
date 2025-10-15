'''
ESTRUTURAS CONDICIOANIS IF, ELSE, ELIF

'''
import os

idade: int = int(input("Digite a sua idade: "))
if idade < 12:
    print(f"Criança: {idade}")
elif idade < 18:
    print(f"Adolescente: {idade}")
else:
    print(f"Adulto: {idade}")

input("Clique para sair")
os.system('cls')
