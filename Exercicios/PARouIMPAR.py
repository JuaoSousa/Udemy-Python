"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input("Digite um número inteiro: ")

try:
    numero_int = int(numero)
    
    if numero_int % 2 == 0:
        print(f"{numero_int} é um número Par")

    else:
        print(f"{numero_int} é um número Impar")
    

except:
    print(f"'{numero}' não é um número inteiro!")