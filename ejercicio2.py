# Ejercicio 2
# Complete el siguiente codigo para recorrer la lista `x` e imprima
# los numeros impares y que pare de imprimir al encontrar un numero mayor a 800
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


x = np.int_(np.random.random(100)*1000)

num = 0
while(num<800):
   for equis in x:
        if(equis%2 != 0):
            print(equis)
            num = equis




