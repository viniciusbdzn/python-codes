#c = range(1, 4)
#print(list(c))
#
#for item in range(9, 0, -1):
#    print(item)

#nome = input('Entre com seu nome: ')
#for letra in nome:
#    print(letra)

#pessoas = ['João', 'Valentina', 'Enzo', 'Lucas', 'Felipe']
#for listaNome in pessoas:
#    print(listaNome)
#
#print(pessoas)

#word = input('Entre com uma palavra: ')
#while word != 'sair':
#    word = input('Digite "sair" pra sair do while: ')
#print('Você digitou "sair" e agora está fora do laço')

#usando "break"
#while True:
#    palavra = input('Entre com uma palavra: ')
#    if palavra == 'sair':
#        break
#print('Você digitou "sair" e agora está fora do laço.')

#while True:
#    print('Você está no primeiro laço')
#    opcao1 = input('Deseja sair dele? Digite "SIM" para isso.')
#    if opcao1 == 'SIM':
#        break
#    else:
#        print('Você está no segundo laço.')
#        opcao2 = input('Deseja sair dele? Digite "SIM" para isso.')
#        if opcao2 == 'SIM':
#            break
#        print('Você saiu do segundo laço.')
#print('Você saiu do primeiro laço.')

#usando "continue"
#for num in range(1, 11):
#    if num == 5:
#        continue #break irá interromper toda a execução
#    else:
#        print(num)
#print('Laço encerrado')

#usando "pass" em estrutura de controle e repetição
for num in range (1, 11):
    if num % 2 == 2:
        pass
    else:
        print(num)
print('Laço encerrado.')