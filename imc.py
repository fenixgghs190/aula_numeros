idade = input('Digite sua idade: ')
peso = input('Digite seu peso: ')
altura = input('Digite sua altura: ')
ano = input('Digite o ano de seu nascimento: ')

'''
Cálculo IMC
'''

imc = str(peso) / (str(altura) * str(altura))

'''
Verificar se o ano é bisexto e idade é múltiplo de 7
'''

print('Seu imc é {}'.format(imc))
print('Idade dividido por 7: {}'.format(idade/7))
print('Ano dividido por 4: {}'.format(ano/4))


