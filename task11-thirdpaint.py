print('Esse programa vai calcular a quantidade de tinta necessária para pintar sua casa')
error = 'Ocorreu um erro, certifique-se que os dados foram inseridos corretamente (dica: use ponto em vez de vírgula)'
c = float(2.37)
i = 1
area = {}

while True:
    try:
        msg1 = int(input('Quantas paredes tem na sua casa? '))
        break
    except ValueError:
        print(error)

while i<=msg1:
    while True:
        try:
            width = float(input(f'Insira aqui a LARGURA em metros da parede {i}: '))
            height = float(input(f'Insira aqui a ALTURA da em metros parede {i}: '))
            break
        except ValueError:
            print(error)
    area[i] = width*height

    i = i+1
total = sum(area.values())
total2 = total/c

print(f'A área total a ser pintada é {total}m^2')
print(f'Considerando que um litro de tinta rende {c}m^2; \nSerá precio {total2:.2f}L de tinta')



