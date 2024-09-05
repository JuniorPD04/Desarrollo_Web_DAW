# horas = float(input('Introduzca Horas: '))
# tarifa = float(input('Introduzca su tarifa: '))

# salario = horas * tarifa

# print("Salario: "+ str(salario))

# x = -20
# if x > 0:
#     print('Hola, x es positivo')
# else:
#     print('Hola x, no es positivo')

# print('Terminó')

# Bloque try except
# edad = int(input('¿Cuál es tu edad?'))

# Ejercicio 1: Reescribe el programa del cálculo del salario para darle al empleado
# 1.5 veces la tarifa horaria para todas las horas trabajadas que excedan de 40.
# Introduzca las Horas: 45
# Introduzca la Tarifa por hora: 10
# Salario: 475.0

# horas = float(input('Introduzca Horas: '))
# tarifa = float(input('Introduzca su tarifa: '))
# if horas > 40:
#     salario = 40 * tarifa
#     horas_e = horas - 40
#     salario += horas_e * tarifa * 1.5
# else:
#     salario = horas * tarifa
# print("Salario: "+ str(salario))

# try:
#     horas = float(input("Ingresa las horas trabajadas: "))
#     tarifa = float(input("Ingresa la tarifa por hora: "))
#     salario = 40 * tarifa + (horas - 40) * tarifa * 1.5 if horas > 40 else horas * tarifa
#     print("Salario: " + str(salario))
# except ValueError:
#     print("Error: Ingresa un número válido para las horas y la tarifa.")


# puntuacion = input('Ingresa una puntuación entre 0.0 y 1.0: ')
# try:
#     puntuacion = float(puntuacion)
#     if puntuacion <=1 and puntuacion>=0:
#         if puntuacion>=0.9:
#             print('Sobrealiente')
#         elif puntuacion>=0.8:
#             print('Notable')
#         elif puntuacion>=0.7:
#             print('bien')
#         elif puntuacion>=0.6:
#             print('Sufi')
#         else:
#             print('te falta :c')
#     else:
#         print('No has ingresado un valor válido')
# except ValueError: 
#     print('Escribe numerito porfa')

# Crear un programa donde se pregunte si desea generar una nueva bolilla de bingo

# B 1-15
# I 16 -30
# N 31 - 45
# G 46 - 60
# O 61 - 75

# import random

# def generarBingo(confirmacion):
#     letra = random.choice('BINGO')
#     if confirmacion.upper() == 'S':
#         if letra.upper() == 'B':
#             numero = random.randint(1, 15)
#             numero = f'B-{numero}'
#             return numero
#         if letra.upper()== 'I':
#             numero = random.randint(16, 30)
#             numero = f'I-{numero}'
#             return numero
#         if letra.upper() == 'N':
#             numero = random.randint(31, 45)
#             numero = f'N-{numero}'
#             return numero
#         if letra.upper() == 'G':
#             numero = random.randint(46, 60)
#             numero = f'G-{numero}'
#             return numero
#         if letra.upper() == 'O':
#             numero = random.randint(61, 75)
#             numero = f'O-{numero}'
#             return numero
#     else:
#         mensaje = 'No se generó, gracias'
#         return mensaje

# letra = input('Quieres generar nuevo número? Ingresa sí (S) o no (N): ')
# print(generarBingo(letra))

import random

def generarBingo(confirmacion):
    letra = random.randint(1,5)
    if confirmacion.upper() == 'S':
        if letra == 1:
            numero = numero * (letra-1) + 1
            numero = f'B-{numero}'
            return numero
        if letra.upper()== 'I':
            numero = random.randint(16, 30)
            numero = f'I-{numero}'
            return numero
        if letra.upper() == 'N':
            numero = random.randint(31, 45)
            numero = f'N-{numero}'
            return numero
        if letra.upper() == 'G':
            numero = random.randint(46, 60)
            numero = f'G-{numero}'
            return numero
        if letra.upper() == 'O':
            numero = random.randint(61, 75)
            numero = f'O-{numero}'
            return numero
    else:
        mensaje = 'No se generó, gracias'
        return mensaje

letra = input('Quieres generar nuevo número? Ingresa sí (S) o no (N): ')
print(generarBingo(letra))
