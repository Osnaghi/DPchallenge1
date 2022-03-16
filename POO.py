#from curses.ascii import isdigit
from random import choice
import string

class Password:

    # Constructor por defecto

    def __init__(self, contraseña = "", longitud = 8):
        self.__contraseña = contraseña
        self.__longitud = longitud

    # Segundo constructor que genera al instanciar una contraseña automáticamente con la longitud que se le asigna

    @classmethod
    def constructor(cls, longitud):
        caracteres = string.ascii_letters + string.digits
        cls.__longitud = longitud
        cls.__contraseña = cls.generarPassword(cls)
        return cls(cls.__contraseña, cls.__longitud)

    # Método para comprobar fortaleza de la contraseña

    def esFuerte(self):

        # Se crean variables para contar

        contar_may = 0
        contar_min = 0
        contar_num = 0

        # Se realiza la cuenta de cada tipo de caracter mediante un bucle for... in
        
        for caracter in self.__contraseña:
            if caracter.isupper():
                contar_may +=1
            elif caracter.islower():
                contar_min +=1
            elif caracter.isdigit():
                contar_num += 1
        
        # Se comprueban las condiciones para que la contraseña sea "fuerte"
        if contar_may > 2 and contar_min > 1 and contar_num > 3:
            return True
        else:
            return False

    # Método para generar Password con numeros y letras

    def generarPassword(self):
        caracteres = string.ascii_letters + string.digits
        self.__contraseña = ''.join(choice(caracteres) for i in range(self.__longitud))
        return self.__contraseña

    # Métodos GET

    def get_contraseña(self):
        return self.__contraseña

    def get_longitud(self):
        return self.__longitud

    # Métodos SET

    def set_longitud(self, longitud):
        self.__longitud = longitud

def app():
    password_ingresado = input('Ingrese una contraseña: ')
    long_pass_ingresado = len(password_ingresado)
    password_usuario = Password(password_ingresado, long_pass_ingresado)


    if password_usuario.esFuerte():
        print(f'El password "{password_usuario.get_contraseña()}" es fuerte')
    else:
        print(f'El password "{password_usuario.get_contraseña()}" no es fuerte')

if __name__ == "__main__":
    app()



    
