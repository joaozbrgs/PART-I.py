import random as rd
error = 'Desculpe, eu não entendi. Por favor confira se sua resposta está no formato correto'
regras = '\nVocê começa com duas cartas; \nCada carta tem o valor entre 1 - 10; \nSeu objetivo é chegar ao valor "21", ou o mais próximo possível; \nVocê pode comprar quantas cartas quiser do baralho; \nSe o valor da soma das cartas ultrapassar 21, você perde; \nA casa também vai receber 2 cartas e comprar até chegar a 21; \nSe a casa chegar mais perto de 21 do que você sem ultrapassar, você perde; \nSe ambos tirarem o mesmo valor, ocorre um empate e nada acontece; \nVocê começa com 100 moedas e pode escolher quantas vai apostar em cada rodada; \nVocê não pode apostar mais moedas do que você possui; \n'
yorn = 'insira "s" para Sim ou "n" para Não'

deck = 4*['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
array1 = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9, '10': 10, 'J':10,'Q':10,'K':10}

def casa(deck,array1):
        casa_hand = rd.sample(deck,2)
        casa_sum = sum(array1[card1] for card1 in casa_hand if card1 in array1)

        while casa_sum < 17:
            ncard1 = rd.choice(deck)
            casa_hand.append(ncard1)
            casa_sum += array1.get(ncard1,0)

        return casa_hand, casa_sum


error1 = 'Please type "y" for Yes and "n" for No.'
error2 = 'Please type a valid answer'
while True:
    try:
        msg1 = str(input('Would you like to try this code? [y/n] '))
        if msg1.lower().strip() == 'y' or msg1.lower().strip() == 'n':
            print(regras)
            break
        else:
            print(error1)
    except ValueError:
            print(error2)

wallet = int(100)

while wallet > 0:
    while True:
        try:
            msg2 = int(input(f'Você tem {wallet} moedas. Quanto vai apostar?: '))
            if msg2 <= 0:
                print(error)
            elif msg2 > wallet:
                print(f'Você não tem moedas suficientes. Atualmente, você tem {wallet} moedas')
            else:
                break
        except ValueError:
         print(error)
    
    while True:
        hand = rd.sample(deck,2)
        sum1 = sum(array1[card] for card in hand if card in array1) 
        print(f'Suas cartas são: {hand}, sua mão está em {sum1}')

        while sum1 < 21:
            msg3 = input('Gostaria de comprar mais uma carta? [s/n]')
            if msg3.lower() == 's':
             ncard = rd.choice(deck)
             hand.append(ncard)
             sum1 += array1.get(ncard,0)
             print(f'A carta comprada foi {ncard}, a soma das suas cartas é {sum1}')
            elif msg3.lower() == 'n':
             break
            else:
             print(yorn)
        if sum1 > 21:
          wallet = wallet - msg2          
          print(f'Você perdeu! Sua carteira agora tem {wallet} moedas')
          break
        else:
            while True:
                casa_hand, casa_sum = casa(deck,array1)    

                print(f'\nSua mão deu {sum1} \nA casa obteve {casa_sum} \n')

                if sum1 == casa_sum:
                    print(f'Empate! Você continua com {wallet} moedas')
                    break
                elif sum1> casa_sum:
                    wallet = wallet + msg2
                    print(f'Você venceu! Sua carteira agora tem {wallet} moedas!')
                    break
                elif casa_sum > 21:
                    wallet = wallet + msg2
                    print(f'Você venceu! Sua carteira agora tem {wallet} moedas!')
                    break
                elif sum1 < casa_sum:
                    wallet = wallet - msg2
                    print(f'Você perdeu... Sua carteira agora tem {wallet} moedas')
                    break
        break            
    while True:
        msg4 = input('Gostaria de jogar outra rodada? [s/n] ')
        if msg4.lower() == 'n':
            break
        elif msg4.lower() != ('s' or 'n'):
            print(yorn)
        else:
            break
    if msg4 == 'n':
        break


print('Obrigado por participar!')

# print('Até essa parte, o código está ok')
