i = input('Inicio: ')
f = input('Fim: ')
p = input('Passo: ')

try:
    i_int = int(i)
    f_int = int(f)
    p_int = int(p)
    for c in range( i_int, f_int+1, p_int):
        print(c)

except:
    print("Os valores inseridos não são válidos!")
   
