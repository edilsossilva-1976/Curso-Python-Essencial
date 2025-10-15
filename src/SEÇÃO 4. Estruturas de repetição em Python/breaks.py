'''
Saindo de loops com Break
Funciona igualmente as liguagens C e Java forçando a saida de um bloco de codigo.
'''
# Exemplo 1:
for numero in range(1, 11):
    if numero == 6:
        break  # Saida do loop
    else:
        print(numero)
print("Saí do loop!")


# Exemplo 2?
while True:
    comando = input("Digite 'S' para sair: ")
    if comando == 'S':
        break
print("Saí do loop")
