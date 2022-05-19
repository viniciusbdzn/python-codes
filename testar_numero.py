#numero = eval(input('Digite um número: '))
#
#if numero%2 == 0:
#    print(f'O número {numero} é par.')
#else:
#    print(f'O número {numero} é ímpar.')

#for numero in range(1, 11, 1):
#    if numero%2 == 0:
#        print(f'O número {numero} é par.')
#    else:
#        print(f'O número {numero} é ímpar.')

soma_par = 0
cont_pares = 0

for numero in range(1, 11, 1):
    if numero%2 == 0:
        soma_par = soma_par + numero
        cont_pares += 1
    else:
        continue
    media = soma_par/cont_pares

print(f'Soma dos pares = {soma_par}')
print(f'Quantidade de números pares = {cont_pares}')
print(f'Média dos pares = {media}')

        
        

