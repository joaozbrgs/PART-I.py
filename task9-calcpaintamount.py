print('Esse código vai calcular o quanto de tinta será necessário para pintar sua casa')
error=('Ocorreu um erro inesperado')
i=int(1)

while True:
    try:
        msg1=int(input('quantas paredes tem na sua casa?'))
        break
    except ValueError:
        print('insira uma quantidade válida')

numeros = {1, 3, 'matheus'}
paredes={}
while i<=msg1:
    wall=float(input(f'insira a área da parede {i}: '))
    paredes[i]=wall

    paredes[0]['largura'] = wall
    paredes[0]['altura'] = 1

    i=i+1

print(paredes)

paredes = [
    {
        'largura': 2.5,
        'altura': 2
    },
    {
        'largura': 2,
        'altura': 3
    },
    {
        'largura': 4,
        'altura': 5
    },
]

print((paredes[0]['largura'] )*(paredes[0]['altura']))