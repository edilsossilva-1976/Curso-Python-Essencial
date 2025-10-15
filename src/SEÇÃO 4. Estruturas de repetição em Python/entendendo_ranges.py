'''
ENTENDENDO RANGES
-Precisamos entender o loop for para usar o ranges
-Precisamos conhecer o range para trabalhar melhor com loops for

- Ranges são utilizados para gerar sequencias numericas especificadas

* Formas gerais:
- Forma 1:
range(valor_de_parada)
OBS: Valor de parada não inclusive (inicio padrao 0, e passo sempre de 1 em 1)

- Forma 2:
range(valor_inicio, valor_de_parada)
OBS: Valor de parada não inclusive (inicio especificado pelo usuario, e passo
1 em 1)

- Forma 3:
range(valor_inicio, valor_de_parada, passo)
OBS: Valor de parada não inclusive (inicio especificado pelo usuario, e passo
especificado pelo usuario)

- Forma 4 (3 inversa):
range(valor_inicio, valor_de_parada, passo)
OBS: Valor de parada não inclusive (inicio especificado pelo usuario, e passo
especificado pelo usuario)

'''

# Forma 1:
for num in range(11):
    print(num)  # 1 num por linha

print()
for num in range(11):
    print(num, end=", ")  # Imprimindo tudo em uma linha

# Forma 2:
print()
for num in range(1, 11):  # Inicio especificado
    print(num, end=", ")  # 1 num por linha

# Forma 3:
print()
for num in range(5, 50, 2):  # Inicio especificado
    print(num, end=", ")  # 1 num por linha
    
# Forma 4:
print()
for num in range(10, -1, -1):  # De 10 a 0
    print(num, end=", ")
