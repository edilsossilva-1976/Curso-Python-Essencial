'''
EXERCICIOS:
3. Faça um programa que declare um inteiro, inicialize-o com 0, incremente-o
de 1000 em 1000, imprimindo seu valor na tela, até que seu valor seja 1000_000
(cem mil).
'''
# 1.Faça um programa que determine e mostre os 5 primeiros múltiplos de 3,
# considerando numeros maiores que 0.

print("\n5 PRIMEIROS MULTIPLOS DE 5\n")
contador: int = 0
indice: int = 1
while contador < 5:
    if indice % 3 == 0:
        print(f"O numero {indice} é multiplo de 3.")
        contador += 1
    indice += 1


# 2.Faça um programa que utilize o comando while para mostrar na tela uma 
# contagem regressiva, iniciando em 10 e terminando em 0. Mostre tambem uma 
# mensagem "FIM" apos a contagem.

print("\nCONTAGEM REGRESSIVA\n")
contador: int = 10
while contador >= 0:
    print(contador)
    contador -= 1
print("Fim")


# 3. Faça um programa que declare um inteiro, inicialize-o com 0, incremente-o
# de 1000 em 1000, imprimindo seu valor na tela, até que seu valor seja 
# 100_000 (cem mil)
print("\nCONTAGEM de 1000 em 1000 até 100_000\n")
for n in range(0, 100_001, 1000):
    print(n)
