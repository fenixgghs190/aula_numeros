idade = int(input('Idade: '))
peso = int(input('Peso: '))
altura = float(input('Altura: '))
ano = int(input('Ano de nascimento: '))

'''
Cálculo IMC
'''

imc = int(peso / (altura * altura))

'''
Verificar se o ano é bisexto e idade é múltiplo de 7
'''

print('Seu imc é: {}'.format(imc))
print('Idade dividido por 7: {}'.format(idade/7))
print('Ano dividido por 4: {}'.format(ano/4))


