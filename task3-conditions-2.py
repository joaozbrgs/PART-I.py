import math
import statistics
from datetime import datetime

def s_or_n_valid(prompt):
    error1 = 'Digite "s" para SIM e "n" para NÃO'
    error2 = 'Digite uma resposta válida'

    while True:
        try:
            msg = str(input(prompt))
            if msg.lower().strip() == 's' or msg.lower().strip() == 'n':
                break
            else:
                print(error1)
        except ValueError:
            print(error2)

    return msg


msg1 = s_or_n_valid('Você gostaria de testar esse código? [s/n]: ')

if msg1 == 's':
    print('Obrigado por usar')
elif msg1 == 'n':
    print('Que pena, tenha um bom dia')
else:
    print('ERRO')








# erro = 'Insira um resposta válida'
# erro2 = 'Responda "s" para SIM ou "n" para NÃO'

# #Navegação no código
# a1 = 'Aprovação de Empréstimo'
# a2 = 'Alistamento'
# a3 = 'Status de Aprovação'
# x1 = print(f'Essa é uma integração de alguns códigos. Qual deles você gostaria de testar?\n\n{a1}')

# #Aprovação condicional de empréstimos
# x2 = print('\nOk, antes preciso saber algumas informações:')
# item1 = str(input('\nO que deseja comprar? -> '))
# price1 = float(input(f'\nInsira o preço do(a) {item1} -> '))
# income1 = float(input(f'Insira sua renda mensal (podem ser valores fictícios) -> '))
# inst1 = int(input('Em quantos anos pretende pagar? -> '))
# inst1 *= 12

# #Valor de cada parcela
# b1 = price1/inst1
# if income1 * .3 < b1:
#     print(f'Desculpe, mas as parcelas de {b1} são incompatíveis com sua renda')
# else:
#     print(f'Meu parabéns! Seu salário de {income1} é compatível com as parcelas de {b1}, portanto seu empréstimo foi aprovado!')


#Situação de alistamento
# age1 = int(input('Insira seu ano de nascimento: '))
# cyear1 = datetime.now().year
# c1 = cyear1 - age1


# if c1 > 18 and c1 < 110:
#     print('Você já passou do tempo de alistamento')
# elif c1 == 18:
#     print('Você deve se alistar esse ano!')
# elif c1 < 18 and c1 > 0:
#     print(f'Faltam {18-c1} anos para você se alistar')
# elif c1 >= 110:
#     print(f'Você tem {c1} anos né, aham sei...')
# elif c1 < 0:
#     print(f'Faltam {c1} anos pra você nascer (Benjamin Button?)')

#Status de aprovação
# d1 = input('Quer saber sua situação em qual matéria? -> ')
# per = int(input(f'Quantos períodos avaliativos você teve em {d1}? -> '))
# grades={}

# for i in range(0,per):
#     n = int(input(f'Qual sua nota no período {i+1}: '))
#     grades[i] = n
#     i+=1

# ns = list(grades.values())
# mean = statistics.mean(ns)
# print(f'\n{ns}\n{mean}')

#