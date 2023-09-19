print('Esse código vai te mostrar a tabuada de 1 a 10 de qualquer número inteiro!')
error='Isso não deveria ter acontecido'
n=1

while True:
     try:
        n1=float(input('Coloque aqui seu número: '))
        break
     except ValueError:
        print('Insira um número inteiro!')        

print(f'Essa é a tabuada de {n1}:')
while n<=10:
    print(f'{n1} x {n} = {n1*n}')
    n=n+1