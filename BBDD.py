import mysql.connector as mysqlc




class Municipal:
    
    def __init__(self, nombre = '', apellido = '', telefono = '', email = '', salario = '', antiguedad = '', puesto = '', municipalidad = ''):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.email = email
        self.salario = salario
        self.antiguedad = antiguedad
        self.puesto = puesto
        self.municipalidad = municipalidad
        self.crearConeccion()
        self.__db = None
    

    # CONSULTAS A LA BASE DE DATOS

    cursor_create = cursor_read = None

    def crearConeccion(self):
        self.__db = mysqlc.connect(
            host="localhost",
            user="newuser",
            password="newuser",
            database="municipales"
        )
        return self.__db

    def leer_todos(self):

        self.crearConeccion()

        cursor_read = self.__db.cursor(dictionary=True)

        sql_select = "SELECT * FROM empleados"

        try:
            cursor_read.execute(sql_select)
            resultado = cursor_read.fetchall()
            self.__db.commit()
        except Exception as err:
            return err

        return resultado

    def leer_filtrados(self):

        self.crearConeccion()
        cursor_read = self.__db.cursor(dictionary=True)
        sql_select = "SELECT nombre, apellido, telefono, email, puesto, municipalidad "
        sql_select += "FROM empleados WHERE salario > 70000 AND (antiguedad BETWEEN  10 AND 15)"

        try:
            cursor_read.execute(sql_select)
            resultado = cursor_read.fetchall()
            self.__db.commit()
        except Exception as err:
            return err

        return resultado

    def insertar(self, datos):
        self.crearConeccion()
        cursor_create = self.__db.cursor()

        sql_insert = "INSERT INTO empleados (nombre, apellido, telefono, email, salario, antiguedad, puesto, municipalidad)"
        sql_insert += "  VALUES (%s , %s, %s, %s , %s, %s, %s, %s)"

        try:
            cursor_create.execute(sql_insert, datos)
            self.__db.commit()
        except Exception as err:
            return err

        return "agregado correctamente"

    # METODOS

    def insertar_empleado(self):
        datos = [self.nombre, self.apellido, self.telefono, self.email, self.salario, self.antiguedad, self.puesto, self.municipalidad]
        self.insertar(datos)
    
    def recibir_todos(self):
        diccionario = self.leer_todos()
        return diccionario

    def recibir_filtrados(self):
        diccionario = self.leer_filtrados()
        return diccionario

# METODO DE LA APP
def agregar():
    # Toma los datos e instancia una clase, llamando a un metodo de la clase se cargan los datos en la Base de Datos
    datos_ingreso = input('Ingrese los datos del empleado separados por comas(nombre, apellido, telefono, email, salario, antiguedad, puesto, municipalidad): ')
    datos = datos_ingreso.split(", ")
    nombre = datos[0]
    apellido = datos[1]
    telefono = datos[2]
    email = datos[3]
    salario = datos[4]
    antiguedad = datos[5]
    puesto = datos[6]
    municipalidad = datos[7]
    nuevo_empleado = Municipal(nombre, apellido, telefono, email, salario, antiguedad, puesto, municipalidad)
    nuevo_empleado.insertar_empleado()

def ver_todos():
    todos = Municipal().recibir_todos()
    print(todos)

def ver_filtrados():
    filtrados = Municipal().recibir_filtrados()

    print(filtrados)


# CLI DE LA APP


def cli():
    menu = '\n_EMPLEADOS MUNICIPALES_ \n'
    menu += '-----------------------\n'
    menu += '1. Agregar empleados\n'
    menu += '2. Mostrar empleados\n'
    menu += '3. Mostrar empleados con salario mayor a $70.000\n   y entre 10 y 15 años de antiguedad\n'
    menu += '4. Salir\n'
    opcion = ''
    
    while opcion != '4':
        print(menu)
        opcion = input('Seleccione opcion: ')
        if opcion == '4':
            print('Programa finalizado')
        elif opcion == '1':
            agregar()
        elif opcion == '2':
            ver_todos()
        elif opcion == '3':
            ver_filtrados()

if __name__ == "__main__":
    cli()

# DATOS FICTICIOS
# Juan, Rodriguez, 346516546, afaadgag, 80000, 10, mantenimiento, rosario
# Jose, Mendez, 346589756, adafagag, 75000, 12, administrativo, santa fe
# Manuel, Romero, 34658456, adgasgadga, 70000, 10, administrativo, reconquista
# Manuela, Romero, 34658456, adgasgadga, 75000, 9, administrativa, reconquista




    