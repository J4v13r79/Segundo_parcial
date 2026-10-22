from Ejercicios.Ejercicio1_cine import leerCantidad, calcularSubtotal, calcularDescuento, mostrarCompra
from Ejercicios.Ejercicio2_combustible import leerDatos,leerDatos, calcularRendimiento, calcularCosto, mostrarResultados


def ejecutarEjercicio1():
    cantidad_boletos = leerCantidad()
    subtotal = calcularSubtotal(cantidad_boletos)
    descuento_aplicado = calcularDescuento(subtotal, cantidad_boletos)
    total_a_pagar = subtotal - descuento_aplicado
    mostrarCompra(cantidad_boletos, subtotal, descuento_aplicado, total_a_pagar)

def ejecutarEjercicio2():
    distancia, litros = leerDatos()
    rendimiento = calcularRendimiento(distancia, litros)
    costo = calcularCosto(litros)
    mostrarResultados(distancia, litros, rendimiento, costo)
 

def mostrarMenu():
    print()
    print("Elija el caso que deseee llevar a cabo") 
    print("1. costo de los boletos") 
    print("2. rendimiento del combustible") 

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