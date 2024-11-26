'''
Calculador de IMC
'''

# ... os tres pontos significa "Ellipsis", utilizamos quando não temos um codigo ja definido, então deixamos em "aberto".

nome = 'Joao Pedro'

altura = 1.8

peso = 78

imc = peso / (altura * 2) #Altura elevado a 2

linha_1 = f'{nome} tem altura igual a: {altura:.2f} '

linha_2 = f'O IMC de seu corpo eh igual a: {imc:.2f} '

print(linha_1)

print(linha_2)
