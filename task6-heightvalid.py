error='desculpe, isso não deveria ter acontecido'
print('Esse é um teste para comparar as alturas entre você e seu amigo(a)')

c1=2.0
c2=1.8
while True:
    try:
        n1=float(input('coloque aqui sua altura em metros (use ponto em vez de vírgula)'))
        n2=float(input('coloque aqui a altura em metros do seu amigo'))
        break
    except ValueError:
        print('você colocou um tipo de informação que eu não entendi, por favor, tente novamente')

md=(n1+n2)/2
dif=(n1-n2)*100
cm1=n1*100
cm2=n2*100
mm1=n1*1000
mm2=n2*1000
difc1=(c1-n1)*100
difc2=(c2-n1)*100
print(f'A sua altura é {n1}m e a altura do seu amigo é {n2}m.')
print(f'A diferença de altura entre vocês é {dif:.0f}cm.')
if dif>0:
    print('além disso, você é mais alto que seu amigo')
elif dif==0:
    print('que coincidência! Você e seu amigo têm a mesma altura!')
else:
    print('parece que seu amigo é mais alto que você, coma mais feijão!')

print(f'A média de altura de vocês dois é {md:.3f}m')
print(f'em centímetros, sua altura seria {cm1:.0f} e a do seu amigo seria {cm2:.0f}')
print(f'em milímetros, suas alturas seriam {mm1:.0f} e {mm2:.0f} respectivamente')

if n1>c1 or n1==0:
    print(f'percebi que você tem pelo menos {c1}m de altura, impressionante!')
elif n1<c1 and c2<=n1:
    print(f'sua altura é acima da média, faltam apenas {difc1:.0f}cm para você ter {c1}m de altura!')
elif n1<c2:
    print(f'você tem quase {c2}m, faltavam apenas {difc2:.0f}cm!')
else:
    print(error)

print('espero que tenha gostado desse script!')