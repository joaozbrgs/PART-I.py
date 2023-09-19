error='Desculpe, não posso te ajudar'

day=int(input('que dia é seu aniversário?'))
        

month=int(input('que mês é o seu aniversário?'))
year=int(input('que ano é o seu aniversário?'))
message=input(f'Você nasceu em {day}/{month}/{year}. Isso está correto?')
if message=='sim':
    message2=input('Gostaria de saber sua idade?')
else:
    print(error)
if message2=='sim':
    day2=int(input('que dia é hoje?'))
    month2=int(input('em que mês estamos?'))
    year2=int(input('em que ano estamos?'))
    message3=input(f'Hoje é dia {day2}/{month2}/{year2}?')
else:
    print(error)

if message3=='sim' and month > month2:
    print('Você têm',year2 - year - 1, 'anos!')
elif message3=='sim' and month < month2:
    print('Você têm',year2-year, 'anos!')
elif message3=='sim' and month == month2 and day > day2:
    print('Você têm',year2 - year - 1, 'anos!')
elif message3=='sim' and month == month2 and day < day2:
    print('Você têm',year2 - year, 'anos!')
elif message3=='sim' and month == month2 and day == day2:
    print('Feliz Aniversário! Você está fazendo',year2-year, 'anos!')

else:
    print(error)
