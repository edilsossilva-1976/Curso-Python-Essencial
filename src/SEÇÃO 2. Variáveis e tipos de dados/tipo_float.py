'''
TIPO NUMERICO FLOAT (Ponto flutuante)
* Conhecido também como tipo real, decimal
* O separador de casas decimais é o ponto.

Ao declarar variaveis tipo float, usa-se: valor = 1.44 e não valor = 1.44

'''
valor = 1.44
print(type(valor))
print(valor)

# Declaração de multiplos atribuição de variaveis
valor1, valor2 = 1.36, 44.0
print(f"valor1: {valor1}")
print(f"valor2: {valor2}")

# Converter um float para um int
# OBS: Ao converter valores para inteiro, perde-se as casas decimais (precisão)
resultado = int(valor)
print(f"Resultado da conversão para int: {resultado}")

# Converter int para float:
numFloat = 2.65
numInt = int(numFloat)
print(numFloat)
# Trabalhando com numeros complexos
complexo = 5j
print(complexo)
