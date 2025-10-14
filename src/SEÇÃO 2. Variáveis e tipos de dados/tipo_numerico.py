'''
TIPO NUMERICO

    Em Python, os tipos numéricos principais são int (inteiros),
float (números de ponto flutuante ou decimais) e complex (números complexos).
    O tipo numerico int (Inteiro): Representa números inteiros, positivos ou
negativos, sem casas decimais (ex: 10, -5, 0).
    O tipo numerico float (Ponto flutuante): Representa números com casas
decimais (ex: 3.14, -2.5).
    O tipo numerico complex (Complexo): Representa números complexos, que são
compostos por uma parte real e uma parte imaginária, indicada pelo sufixo j
(ex: 3+2j).


'''
# Visualizar tipos de dados inteiros
numero = 42
print(type(numero))
# Todo numero inteiro retornara em type: <class 'int'>

# Visualizar tipos de dados float (ponto flutuante)
numero = 4.2
print(type(numero))
# Todo numero racional retornara em type: <class 'float'>

# Visualizar tipos de dados complex (complexos)
numero = 4 + 2j
print(type(numero))
# Todo numero complexo retornara em type: <class 'complex'>

numeroGrande = 1_000_000_000  # Facilita a visualização
print(numeroGrande)
