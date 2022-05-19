escolha = input('Escolha uma opção de função: 1 ou 2: ')
if escolha == 1:
    def func1(x):
        return x + 1
elif escolha == 2:
    def func2(x):
        return x + 2

s = func1(1)
print(s)

#def taximetro(distancia, multiplicador=1):
#    largada = 3
#    km_rodado = 2
#    valor = (largada + distancia * km_rodado) * multiplicador
#    return valor
#
#pagamento = taximetro(3.5)
#print(pagamento)

