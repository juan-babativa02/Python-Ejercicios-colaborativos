'''Escribir un programa que muestre por pantalla la tabla de multiplicar del
1 al 10.'''

for numero in range(1,11):
    print(f"La tabla del {numero}")

    for i in range(1,11):
        mult=numero*i
        print(f"{numero} x {i} = {mult}")