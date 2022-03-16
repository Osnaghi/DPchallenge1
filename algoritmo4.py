# 4. CONSIGNA:
# Generar un número aleatorio comprendido entre 0 y 1000. Pedir, a continuación, al
# usuario adivinar el número escogido por el ordenador. Para ello, debe introducir un
# número comprendido entre 0 y 1000. Se compara el número introducido con el
# calculado por el ordenador y se muestra en la consola "es mayor" o "es menor" en
# función del caso. Se repite la operación hasta que el usuario encuentra el número.

from random import seed
from random import choice

def adivina():

    # Se genera la lista de numeros del 0 al 1000

    numeros = [i for i in range(0, 1001)]

    #Se elije un numero de la lista al azar

    numero_elegido = choice(numeros)

    # Mediante un bucle se le solicita al usuario que adivine el numero hasta que acierte. 
    
    while True:

        # Se pide al usuario que ingrese un número.

        intento = int(input('Adivine un numero del 0 al 1000: '))

        if  intento == numero_elegido:
            print('Ha encontrado el numero')

            # Si el usuario adivina, se finaliza el bucle.

            break
        
        # Se informa si el numero ingresado es mayor o menor según el caso.

        elif intento > numero_elegido:
            print('es mayor')

        else:
            print('es menor')

if __name__ == "__main__":
    adivina()
