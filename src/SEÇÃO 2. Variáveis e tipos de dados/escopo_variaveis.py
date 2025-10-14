'''

ESCOPO DE VARIAVEIS
É o alcance de visualização de uma variavel.
Caso de escopos: globais e locais.

* Variaveis globais: o reconhecimento das variaveis são reconhecidas
a todo o arquivo.
* Variaveis locais: o reconhecimento das variaveis estao delimitadas
às funções ou blocos onde foram declaradas.
'''
# Para declarar uma variavel: Sintaxe: <variavel> = <valor>
numero: int = int(input("Digite um numero inteiro: "))  # variavel global
print(numero)

'''
    Python é uma linguagem de tipagem dinamica. O que significa que ao
declarar-mos uma variavel, o tipo é inferido pela linguagem ao atribuirmos
um valor a ela.
'''

if numero > 10:
    novo = numero + 10
    print(novo)

print(f"Imprimir novo numero: {novo}")  # Esta linha vai retornar um erro
