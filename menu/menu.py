'''Crear un menu de opciones donde podamos seleccionar cualquera de los dos ejercicios'''

def mostrar_menu():
    print("Seleccione una opción:")
    print("1. Ejercicio 1")
    print("2. Ejercicio 2")
    print("3. Salir")

def obtener_opcion():
    opcion = input("Ingrese el número de la opción deseada: ")
    return opcion