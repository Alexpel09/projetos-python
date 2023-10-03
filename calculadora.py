# 1. Solicite ao usuário que insira dois números.
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# 2. Solicite ao usuário que escolha uma operação.
print("Escolha uma operação:")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

escolha = input("Digite o número da operação desejada: ")

# 3. Realize a operação com base na escolha do usuário.
if escolha == '1':
    resultado = num1 + num2
    operacao = "adição"
elif escolha == '2':
    resultado = num1 - num2
    operacao = "subtração"
elif escolha == '3':
    resultado = num1 * num2
    operacao = "multiplicação"
elif escolha == '4':
    if num2 != 0:
        resultado = num1 / num2
        operacao = "divisão"
    else:
        print("Erro: Não é possível dividir por zero.")
        resultado = None
else:
    print("Opção inválida")
    resultado = None

# 4. Exiba o resultado ou uma mensagem de erro.
if resultado is not None:
    print(f"O resultado da {operacao} é: {resultado}")
