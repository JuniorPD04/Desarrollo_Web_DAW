# import math

# int_senal = 7
# int_ruido = 9

# relacion = int_senal / int_ruido
# decibelios = 10 * math.log10(relacion)
# print(decibelios)

# print(math.sqrt(2))

# print(2**0.5)

# import random
# print(random.random()) # para números entre 0 y 1
# print(random.choice('CHOISE'))

# Sesion 5
# def muestra_algo ():
#     print('Ore wa')
#     print('Kaisoku ni naru hotokoda')
#     return 'Hola'

# resultado = muestra_algo()
# print(resultado)

# def sumar(a,b):
#     return a+ b

# c = sumar(20,10)
# print(c)

# import random

# def generarBingo(numero_letra):
#     factor = numero_letra - 1 
#     ini = (factor)*15 + 1
#     ff = ini + 14

#     numero = random.randint(ini, ff)

#     if not(1 <= numero_letra <= 5):
#         mensaje = 'No se generó, gracias'
#         return mensaje
    
#     if numero_letra == 1:
#         numero = f'B-{numero}'
#         return numero
#     if numero_letra == 2:
#         numero = f'I-{numero}'
#         return numero
#     if numero_letra == 3:
#         numero = f'N-{numero}'
#         return numero
#     if numero_letra == 4:
#         numero = f'G-{numero}'
#         return numero
#     if numero_letra == 5:
#         numero = f'O-{numero}'
#         return numero

# numero = int(input('¿Quieres generar un nuevo número? Ingresa un número del 1 al 5: '))
# print(generarBingo(numero))

# import random

# def generarBingo(numero_letra):
#     factor = numero_letra - 1 
#     ini = (factor)*15 + 1
#     ff = ini + 14

#     numero = random.randint(ini, ff)

#     if not(1 <= numero_letra <= 5): return 'No se generó, gracias'
    
#     if numero_letra == 1: numero = f'B-{numero}'
#     if numero_letra == 2: numero = f'I-{numero}'
#     if numero_letra == 3: numero = f'N-{numero}'
#     if numero_letra == 4: numero = f'G-{numero}'
#     if numero_letra == 5: numero = f'O-{numero}'
    
#     return numero

# # numero = int(input('¿Quieres generar un nuevo número? Ingresa un número del 1 al 5: '))
# print(generarBingo(random.randint(1,5)))

# n = 5
# while n > 0:
#     print(n)
#     n = n - 1
# print('¡Despegueeee!')

# while True:
#     rpta = input('>> ')
#     if rpta[0] == '#':
#         continue
#     if rpta == 'fin':
#         break
#     print(rpta)

# print('qlq holi')    

# amigos = ['Fabs', 'Luis', 'Leo', 'Gabo', 'Hunter']
# for amigo in amigos:
#     print(amigo)

# contador = 0
# amigos = ['Fabs', 'Luis', 'Leo', 'Gabo', 'Hunter']
# for amigo in amigos:
#     print(amigo)
#     contador += 1

# print(f'Cantidad de integrantes: {contador}')

# mayor = None
# for valor in [3, 31, 12 ,9 , 'aiaiiaia', 15]:
#     print(valor)

# mayor = None
# for valor in [3, 31, 12 ,9 , 220, 15]:
#     if mayor is None or valor > mayor:
#         mayor = valor
# print(mayor)

# cadena = 'BlueLabel'
# print(cadena[0:8])

# print('a' in 'banana')
# print('h' in 'banana')

fruta = 'banana'
# print(dir(fruta))

# help(str.upper)

# fruta2 = fruta.upper()
# print(fruta2)

# banda = 'Radiohead'
# indice = banda.find('h')
# print(indice)

# indice = banda.find('a')
# print(indice)

# indice = banda.find('Radio')
# print(indice)

# indice = banda.find('a', 3)
# print(indice)

# print(banda.startswith('R'))

# print(banda.startswith('r'))

# edad = 18
# print('Mi edad es %d' %edad)

# manejador = open('UNIDAD_I/todoPython/textito.txt')
# for linea in manejador:
#     print(linea)

# try:
#     with open('UNIDAD_I/todoPython/textito.txt', 'r') as manejador:
#         for linea in manejador:
#             print(linea)
# except FileNotFoundError:
#     print("El archivo 'textito.txt' no se encuentra.")

with open('UNIDAD_I/todoPython/textito.txt') as fsal:
    print(fsal)
