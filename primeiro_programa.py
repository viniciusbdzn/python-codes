print("Hello World")
#nome = input("Digite seu nome: ")
#print(list(nome))

#numero = eval(input("Digite um numero: "))
#numero +=2
#print(numero)

#peso = eval(input("Informe seu peso: "))
#altura = eval(input("Informe sua altura: "))
#imc = peso / (altura * altura)
#print(imc)

#Formatando saída de dados no "print"
horas = 23
minutos = 34
segundos = 12
print(str(horas) + ' :', str(minutos) + ' :', str(segundos))

print('{} : {} : {}'.format(horas, minutos, segundos))

print(f'{horas} : {minutos} : {segundos}')

#pra dar espaçamento na impressão
print('{:5}, {:7}'.format(50, 500))
print('{:10.5}'.format(33/7))

seq = [2, 4, 1, 3, 5]
print(seq)

texto = "Linguagem Python"
print(texto[0:4])
print(texto[3:11])
print(texto[::-1])
