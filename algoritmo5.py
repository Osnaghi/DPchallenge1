# 5. CONSIGNA:
# Pedir al usuario que ingrese un número repetidamente hasta que ingrese un -1 y en ese
# caso se terminará el programa.
# Al terminar, mostrará lo siguiente:
# a. – mayor número introducido
# b. – menor número introducido
# c. – suma de todos los números
# d. – suma de los números pares

def numeros():

    # Se crea lista/array vacío

    numeros = []

    # Mediante bucle while se pide al usuario ingresar un número. El bucle solo finaliza cuando se ingresa "-1".

    while True:

        numero = input('Introduzca un número, para finalizar ingrese "-1": ' )

        numero = int(numero)

        if numero == -1:

            break
        
        else:

            # Se agrega el numero ingresado a la lista/array

            numeros.append(numero)

    # Se ordenan los numeros de menor a mayor

    numeros.sort()

    # Se filtra lista para obtener numeros pares

    pares = list(filter(lambda num : (num % 2 == 0),numeros))

    # Se crean variables con los valores a mostrar

    # El número mayor ahora se encuentra al final de la lista, debido a que usamos el método sort
    a = numeros[len(numeros) - 1]
    # El número menor se encuentra al principio de la lista
    b = numeros[0]
    # La suma de todos los números
    c = sum(numeros)
    # La suma de los números pares
    d = sum(pares)

    # Se muestran valores en consola
    print(a, 'Mayor número introducido')
    print(b, 'Menor número introducido')
    print(c, 'Suma de todos los números')
    print(d, 'Suma de los números pares')

if __name__ == "__main__":
    numeros()