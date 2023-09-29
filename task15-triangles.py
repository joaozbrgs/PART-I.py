#Definir se um triângulo existe

#Se ele existe, definir se ele é isoceles, equiláteros ou escaleno

print('Esse é um programa para cálculo de triângulos \nSerão feitos os seguinte cálculos:')
print('Definir se o triângulo existe; \nDefinir o tipo de triângulo (isóceles, escaleno ou equilátero); \nDefinir os três ângulos do triângulo;\n')

t1 = {}
for i in range(0,3):
    t1[i] = int(input(f"Insira o comprimento do lado {i+1}: "))

t1 = list(t1.values())
sort1 = sorted(t1)

la = sort1[0]
lb = sort1[1]
lc = sort1[2]

while True:
    if (la + lb) < lc:
        print('\nEsse triângulo é impossível \n')
        break
    else:
        print('Esse triângulo é possível')

    if la == lb == lc:
        print('Esse triângulo é equilátero')
        break
    elif la == lb and la != lc:
        print('Esse triângulo é isóceles')
        break
    elif la == lc and la != lb:
        print('Esse triângulo é isóceles')
        break
    elif lb == lc and lb != la:
        print('Esse triângulo é isóceles')
        break
    elif la != lb != lc:
        print('Esse triângulo é escaleno')
        break
    else:
        print('ERRO')


if la == lb == lc:
        print('Como o triângulo é equilátero, os ângulos são: 30°, 30° e 30°')

#Usar lei dos cossenos para determinar os demais ângulos caso seja isóceles ou escaleno (from math import cos)

