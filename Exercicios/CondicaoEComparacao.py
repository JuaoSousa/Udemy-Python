'''
Faça um programa que leia dois numeros e mostre qual o maior entre eles
'''

primeiro_numero = int(input('Digite o primeiro valor: '))
segundo_numero = int(input('Digite o segundo valor: '))

if primeiro_numero > segundo_numero:
    print(f"Primeiro numero {primeiro_numero} é maior que o segundo numero {segundo_numero}")

elif segundo_numero > primeiro_numero:
    print(f"Segundo numero {segundo_numero} maior que o primeiro numero {primeiro_numero}")

else:
    print("Numeros Iguais")

print("Fim do programa")