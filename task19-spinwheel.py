import pandas as pd
import random as rd
import tkinter as tk

print('Esse programa é uma roleta da sorte que vai sortear o vencedor')
error = 'Desculpe, isso não deveria ter acontecido'

list1 = ['JOAO', 'PEDRO', 'JOSE', 'AUGUSTO', 'TATI']

n1 = rd.sample(list1,5)

print(len(list1))


frase = input('digite algo')
print((frase.lower()).strip())