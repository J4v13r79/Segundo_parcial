from Ejercicios.Ejercicio1_cine import leerCantidad, calcularSubtotal, calcularDescuento, mostrarCompra
from Ejercicios.Ejercicio2_combustible import leerDatos,


def ejecutarEjercicio1():
    cantidad_boletos = leerCantidad()
    subtotal = calcularSubtotal(cantidad_boletos)
    descuento_aplicado = calcularDescuento(subtotal, cantidad_boletos)
    total_a_pagar = subtotal - descuento_aplicado
    mostrarCompra(cantidad_boletos, subtotal, descuento_aplicado, total_a_pagar)

def ejecutarEjercicio2():
 print("Ejecutando Ejercicio 2: Comisión de ventas")
 


def mostrarMenu():
    print()
    print("PRÁCTICA: DESARROLLO GUIADO POR ESPECIFICACIÓN") 
    print("1. Importe de viaje en taxi") 
    print("2. Comisión de ventas") 

    print("0. Salir") 
 
 
def menus(): 
    opcion = "" 
    while opcion != "0": 
        mostrarMenu() 
        opcion = input("Seleccione una opción: ") 
        if opcion == "1": 
            ejecutarEjercicio1() 
        elif opcion == "2": 
            ejecutarEjercicio2() 
        elif opcion != "0": 
            print("Opción no válida.")