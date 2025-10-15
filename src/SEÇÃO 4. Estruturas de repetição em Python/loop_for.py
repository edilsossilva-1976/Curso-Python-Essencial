'''
Estruturas de repetição (loop): for
sintaxe:
for item in iteravel:
    execução do loop

Com for, utilizamos loops para iterar sobre sequencias ou valores iteráveis.

Exemplos de iteráveis:
    *   String:
            nome = "Geek Universe"
    *   Lista:
            lista = [1, 3, 5, 7, 9]
    *   Range:
            numeros = range(1, 10 (<10))
'''

nome = "Geek University"
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)  # Tem que transformar em uma lista

# Iterando com uma String:
for letra in nome:
    print(letra, end=", ")

# Iterando sob uma lista:
print()
for numero in lista:
    print(numero, end=", ")

# Iterando sob um range:
print()
for numero in range(1, 10):
    print(numero, end=", ")

# Enumerate: adiciona um contador a um iterável e o retorna como um objeto
# enumerado.
print()
for valor in enumerate(nome):
    print(valor, end="\n")

print()
for index, palavra in enumerate(nome):
    print({index}-{palavra}, end=" ")


# Receber iteração do usuario:
print()
print("Receber iterações do usuario:")
qtd = int(input("Digite o numero de repetições: "))
for n in range(1, qtd + 1):
    print(f"Imprimindo: {n}")

# Imprimindo emoji na tela
print()
emoji = '\U0001F605'
for num in range(1, 10):
    print(f'{emoji * num}')
