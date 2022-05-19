peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))

def calcularImc() :
    imc = peso / (altura * altura)
    if imc >= 18.5 and imc <= 24.9:
        print(f'Seu imc é {imc}. Parabéns, você está no seu peso ideal!')
    elif imc < 18.5:
        print(f'Seu imc é {imc}. Cuidado, você está desnutrido!')
    elif imc >=25 and imc <= 29.9:
        print(f'Seu imc é {imc}. Você está com sobrepeso!')
    elif imc >= 30 and imc <= 39.9:
        print(f'Seu imc é {imc}. Você está com obesidade! ')
    elif imc >= 40:
        print(f'Seu imc é {imc}. Você está com obesidade mórbida, está quase explodindo de tão obeso!')
    else:
        print('Erro! Dados digitados inválidos!')

calcularImc()