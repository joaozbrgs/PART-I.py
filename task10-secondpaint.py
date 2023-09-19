print('Esse código vai calcular a quantidade de tinta necessária para criar pintar sua casa')
error='Ocorreu um erro, digite um número válido (use ponto em vez de vírgula)'
paint1 = float(2.37)
i=int(1)
paredes={}

while True:
    try:
        msg1 = int(input('Quantas paredes tem na sua casa? '))
        break
    except ValueError:
        print(error)

while i <= msg1:
    try:
        width = float(input(f'Coloque aqui a LARGURA da parade {i}: '))
        height = float(input(f'Coloque aqui a ALTURA da parede {i}: '))
    except ValueError:
        print(error)        
    paredes[i] = {'largura':width, 'altura':height }
    i = i + 1

print((paredes[1]['largura'])*(paredes[1]['altura']))
