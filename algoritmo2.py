# 2. CONSIGNA:
#Escribe una aplicación que solicite al usuario que ingrese una contraseña cualquiera.
#Después se le pedirá que ingrese nuevamente la contraseña, con 3 intentos. Cuando
#acierte ya no pedirá más la contraseña y mostrará un mensaje diciendo “Felicitaciones,
#recordás tu contraseña”. Si falla luego de 3 intentos se mostrará el mensaje “Tenes que
#ejercitar la memoria”. Los mensajes quedarán en pantalla a la espera que el usuario
#presione una tecla, luego de esto se cerrará el programa.

def comprobar_password():
    # Se pide al usuario que ingrese la contraseña
    password0 = input('Ingrese su contraseña: ')

    # Mediante un bucle for se pide al usuario que reingrese la contraseña hasta 3 veces, saliendo del bucle si lo hace correctamente

    for i in range(0, 3):
        password1 = input('Vuelva a ingresar su contraseña: ')
        if password0 == password1:
            print('Felicitaciones, recordas tu contraseña')
            break
        
    else:
        print('Tenes que ejercitar la memoria')

if __name__ == "__main__":
    comprobar_password()