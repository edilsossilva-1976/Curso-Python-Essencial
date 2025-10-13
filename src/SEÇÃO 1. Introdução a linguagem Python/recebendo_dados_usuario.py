'''
    Recebendo dados do usuario
    input() --> Todo dado recebido via input é do tipo String

    Em Python, String é tudo que estiver entre:    Exemplos:
    * Aspas simples -----------------------------> 'Angelina'
    * Aspas duplas; -----------------------------> "Angelina"
    * Aspas simples triplex; --------------------> \'''Angelina\'''
    * Aspas duplas triplas; ---------------------> """Angelina"""
'''

# Entrada de dados
# print("Qual o seu nome? ")
# nome = input()  # Input() --> entrada

# Simplificando as linhas acima...
nome = input("Qual o seu nome? ")

# Exemplo de print 'antigo 2.x'
# print("Seja bem vindo(a) %s" % nome)

# Exemplo de print 'moderno 3.x'
# print("Seja bem vindo(a) {0}".format.nome())

# Exemplo de print 'mais atual 3.7'
print(f"Seja bem vindo(a) {nome}")

print("Qual sua idade?")
idade = input()

# Processamento
# Saida
# Exemplo de print 'antigo 2.x'
# print("A %s tem %s anos" % (nome, idade))

# Exemplo de print 'mais atual 3.7'
print(f"A {nome} tem {idade} anos.")

'''
#int idade => Cast

Cast é a 'conversão' de um tipo de dado por outro.
'''

print(f"A {nome} nasceu em {2025 - int(idade)}")
