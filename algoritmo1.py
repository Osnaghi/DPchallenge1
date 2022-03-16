# 1. CONSIGNA:
#Pide un número por teclado e indica si es un número primo o no.

def es_primo():
    # Se pide al usuario que ingrese un numero
    numero = input('Introduzca un número entero: ')
    # Se convierte el tipo de la variable a numero entero. Ya que input() devuelve un string.
    numero = int(numero)

    # Se descartan los números menores que 1

    if numero > 1:

        # Se comprueba que el numero no sea divisible sin resto por los numeros menores

        for i in range(2, numero):
            if (numero % i) == 0:
                
                print (numero, 'no es un número primo')
                break
        else:
      
            # Si no se cumplen las condiciones anteriores quiere decir que el número si es primo
                
            print (numero, 'es un número primo')
    else:
        print (numero, 'no es un número primo')
        

if __name__ == "__main__":
    es_primo()