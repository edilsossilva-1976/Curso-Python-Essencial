'''
TIPO BOOLEANO
É um tipo de dados que retorna 2 valores (True/False)

'''
ativo = True
print(f"Tipo da classe: {type(ativo)}")
print(f"Status: {ativo}")

'''
OPERAÇÕES BASICAS
'''
# NEGAÇÃO (NOT) - Se o valor booleano for True, o resultado será False
print(f"Status: {not ativo}")
logado = False

# OU (or) - é uma operação binaria, dependendo de 2 valores.
# Para resultado booleano True, 1 dos valores tem que ser verdadeiro
print("\nOperações com OR (ou)")
print(f"Ambos True: {True or True}")
print(f"True or False: {True or False}")
print(f"False or True: {False or True}")
print(f"Ambos False: {False or False}")

print()
print(f"5 > 6: {5 > 6}")
print(f"5 < 6: {5 < 6}")
print(f"5 == 6: {5 == 6}")
print(f"5 >= 6: {5 >= 6}")
print(f"5 <= 6: {5 <= 6}")

# Outra operação binária que depende de 2 valores.
# Para resultado booleano True, 2 valores tem que ser verdadeiro
print("\nOperações com AND (e)")
print(f"Ambos True: {True and True}")
print(f"True and False: {True and False}")
print(f"False and True: {False and True}")
print(f"Ambos False: {False and False}")
