'''
LOOP WHILE
Serve para iterar sobre sequencias

Sintaxe:
while expressao_booleana:
    execução do loop, enquanto expressão booleana for verdadeira.

Expressão booleanan é toda expressao onde o resultado pode ser
verdadeiro ou falso
'''

# Exemplo 1
numero = 1
while numero < 10:
    print(numero, end=" ")
    numero += 1  # linha importante para evitar o loop infinito


# Exemplo 2
print()
resposta = ""
while resposta != 'sim':
    resposta = input("Já acabou Jessica? ")
print("Já acabei.")
