print('Teste de manipulaçã de textos e númetos')
erro = 'Favor inserir os dados no formato correto'

while True:
    n1 = str(input('1- Qual o seu nome completo? ')).strip()
    if all((char.isalpha()) or (char.isspace()) for char in n1):
        n1 = n1.title()
        break
    else:
        print(erro)

print('Analisando nome...\n')
print(f'Seu nome em maiúscula é {n1.upper()}')
print(f'Seu nome em minúscula é {n1.lower()}')
l1 = n1.split()
print(f'seu nome tem ',len(n1) - n1.count(' '), 'letras')
print(f'Seu primeiro nome é {l1[0]}')
print(f'Seu primeiro nome tem {len(l1[0])} letras')
print(f'Seu último nome é {l1[-1]} e tem {(len(l1[-1]))} letras')

while True:
    try:
        n2 = int(input('\n2- Digite um número entre 0 e 999: '))
        break
    except ValueError:
        print('Tem que ser inteiro')
print('lista de cada algarismo em ordem decrescente: \n')
while n2 > 0:
    l3 = n2 % 10
    print(l3)
    n2 = n2 // 10

while True:
    n3 = input('\nQual o nome da sua cidade: ')
    if all(char2.isalpha() or char2.isspace() for char2 in n3):
        break             
    else:
        print(erro)
n3 = n3.upper().strip()
l4 = n3.split()
print(f'O nome da sua cidade em maiúsculo é {n3}')
print('Nome da cidade começa com "Santo": ', ((n3.startswith('SANTO'))))  