# 3. CONSIGNA:
#Por teclado se ingresa el valor hora de un empleado. Posteriormente se ingresa el
# nombre del empleado, la antigüedad y la cantidad de horas trabajadas en el mes. Se
# pide calcular el importe a cobrar teniendo en cuenta que al total que resulta de
# multiplicar el valor hora por la cantidad de horas trabajadas. Además, si el empleado
# tiene más de 10 años de antigüedad hay que sumarle la cantidad de años trabajados
# multiplicados por $30. Imprimir en pantalla el nombre, la antigüedad y el total a cobrar.

def empleado():

    # Se pide al usuario ingresar los datos del empleado

    valor_hora = int(input('Ingrese el valor de la hora de trabajo: '))
    nombre = input('Ingrese el nombre del empleado: ')
    antiguedad = int(input('Ingrese la antigüedad del empleado: '))
    cantidad_hs = int(input('Ingrese cantidad de horas trabajadas: '))

    # Se evalua la antiguedad del empleado y se calcula el importe total a cobrar
    # Si es mayor a 10 años se le suma el importe por antiguedad (30 por la cantidad de años)
    if antiguedad > 10:

        importe = valor_hora * cantidad_hs + 30 * antiguedad
    else:
        importe = valor_hora * cantidad_hs
    print(f'Empleado: {nombre} \nAntigüedad: {antiguedad} \nImporte a cobrar: ${importe}')

if __name__ == "__main__":
    empleado()