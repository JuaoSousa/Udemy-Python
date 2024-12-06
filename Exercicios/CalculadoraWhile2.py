while True:
    try:
        # Entrada de Dados
        numero1 = input("Digite o primeiro número: ")
        numero2 = input("Digite o segundo número: ")

        # Conversão de string para float
        num1_float = float(numero1)
        num2_float = float(numero2)

        # Menu com os operadores
        print("\n * Menu dos Operadores * \n")
        print("[1] Soma (+)")
        print("[2] Subtração (-)")
        print("[3] Multiplicação (*)")
        print("[4] Divisão (/)")
        print("[5] Sair")

        operador = input("Escolha uma opção: ")

        # Realizando a operação
        if operador == '1':
            print(f"Resultado de {num1_float} + {num2_float} = {num1_float + num2_float}")
        elif operador == '2':
            print(f"Resultado de {num1_float} - {num2_float} = {num1_float - num2_float}")
        elif operador == '3':
            print(f"Resultado de {num1_float} * {num2_float} = {num1_float * num2_float}")
        elif operador == '4':
            if num2_float == 0:
                print("Erro: Não é possível realizar divisão por zero!")
            else:
                print(f"Resultado de {num1_float} / {num2_float} = {num1_float / num2_float}")
        elif operador == '5':
            print("Encerrando a calculadora. Até logo!")
            break
        else:
            print("Opção inválida! Por favor, escolha uma opção válida do menu.")

    except:
        print("Um ou ambos dos números digitados são invalidos.")