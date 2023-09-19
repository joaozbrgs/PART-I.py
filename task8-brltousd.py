print('Esse código vai calcular quantos dólares você pode comprar com o dinheiro que você tem guardado hoje')
error='Isso não deveria ter acontecido'
usd=float(5)

while True:
    try:
        n1=float(input('Insira aqui quantos reais você tem para investir: '))
        break
    except ValueError:
        print('Por favor, insira um uma quantidade válida (dica: talvez você estja usando vírgula em vez de ponto)')

print(f'Com R${n1}, você pode comprar ${n1/usd:.2f} dólares!')