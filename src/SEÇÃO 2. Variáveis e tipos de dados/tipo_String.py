'''
TIPO STRING
É um tipo string sempre que estiver entre aspas ('x', "x", \'''x\''', """x""")"
# Acima, a barra invertida foi colocada para evitar erro no IDEpelo PEP8.

Por exemplo:
'uma string', '123', 'j', 'True', '42.6j'
"uma string", "123", "j", "True", "42.6j"
'''
# '''uma string''', '''123''', '''j''', '''True''', '''42.6j'''
nome = 'Geek Universe'
nome2 = "Geek Universe"
nome3 = '''Geek Universe'''
nome4 = """Geek Universe"""

print(f"Nome: {nome}")
print(type(nome))

print(f"Nome2: {nome2}")
print(type(nome2))
print(f"Nome3: {nome3}")
print(type(nome3))
print(f"Nome4: {nome4}")
print(type(nome4))

# Aninhamento de aspas
nomeBar = "Gina's Bar"
print(f"Tipo de dado: {type(nomeBar)}")
print(nomeBar)

# Variação de caixa
print(f"Nome minusculo: {nome.lower()}")
print(f"Nome MAIUSCULO: {nome.upper()}")
print(f"Nome split: {nome.split()}")

# Slicing (fatiamento)
print()
print(f"Fatiamento [0:4]: {nome}: {nome[0:4]}")
print(f"Fatiamento [5:15]: {nome}: {nome[5:15]}")

# Gerar substrings de Strings:
print(f"String {nome} = Lista: {nome.split()}")

# Acesso aos substrings com o split:
print("Acesso aos substrings")
print(f"split[0]: {nome.split()[0]}")
print(f"split[1]: {nome.split()[1]}")

print(f"Tamanho da String: {len(nome)} letras")

# Imprimir a string invertida:
print("String invertida.")
print(f"{nome[::-1]}")

# Substituir substrings
# Substituir G por P:
print(f"Letra substituida: {nome.replace('G', 'P')}")
print(f"Letras substituidas: {nome.replace('e', 'y')}")

