'''
    Estruturas logicas: And (e), or (ou), not (não), is (é)
    Operadores unários: not, is
    Operadores binarios: and, or
'''
# Para AND (verdadeiro), ambos os valores precisam ser True
# Para OR (verdadeiro), um dos valores precisam ser True

ativo = False
logado = True

if ativo and logado:
    print("Bem vindo o usuario.")
else:
    print("Voce precisa ativar a sua conta, Cheque o seu e-mail.")


# Para NOT (verdadeiro), o valor booleano é invertido (FALSE)


if not ativo:
    print("Voce precisa ativar a sua conta, Cheque o seu e-mail.")
else:
    print("Bem vindo usuario.")


# Para IS (verdadeiro), o valor booleano é True
if ativo:
    print("Voce precisa ativar a sua conta, Cheque o seu e-mail.")
else:
    print("Bem vindo usuario.")


print(ativo is True)
