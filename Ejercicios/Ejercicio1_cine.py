'''Un cine necesita desarrollar un programa que permita determinar el importe de una compra de boletos. 
Cada boleto cuesta $75.00. El usuario deberá indicar cuántos boletos desea comprar. Cuando se adquieran 4 
boletos o más, se aplicará un descuento del 10% sobre el subtotal. Para compras menores a 4 boletos, no se 
aplicará descuento. '''


# ENTRADAS: 
#Cantidad de boletos a comprar (entero positivo).

#SALIDAS:
#Total a pagar (decimal con dos decimales).

# REGLAS Y SUPUESTOS: 
#PRECIO_BOLETO = 75.00
#DESCUENTO = 0.10
# no usar mas de 2 decimas. 

# ALGORITMO: 
# 1. Solicitar la cantidad de boletos a comprar.
# 2. si cantidad de boletos >= 4
#           cantidad de boletos * 75 * 0.9
#    sino
#           cantidad de boletos * 75

# CASOS DE PRUEBA: 
#1. 1 boleto: 1 * 75 = 75.00
#2. 3 boletos: 3 * 75 = 225.00
#3. 4 boletos: 4 * 75 * 0.9 = 270.00
#4. 5 boletos: 6 * 75 * 0.9 = 405

# RESTRICCIONES PARA EL AGENTE: 
# 1. La única biblioteca externa permitida es tabulate. 
# 2. El codigo debe coincidir con los casos de prueba
# 3. no debe inclur funciones complejas como loops

# CONTRATO DE FUNCIONES: debe incluri cada una de esta como funciones
#  leerCantidad : leer la canidad de boletos a comprar
#  calcularSubtotal : calcular el subtotal de la compra
#  calcularDescuento : calcular el descuento a aplicar
#  mostrarCompra : mostrar los detalles de la compra

def leerCantidad():
    cantidad = int(input("Ingrese la cantidad de boletos a comprar: "))
    return cantidad

def calcularSubtotal(cantidad_boletos):
    PRECIO_BOLETO = 75.00
    subtotal = cantidad_boletos * PRECIO_BOLETO
    return subtotal

def calcularDescuento(subtotal, cantidad_boletos):
    DESCUENTO = 0.10
    if cantidad_boletos >= 4:
        descuento_aplicado = subtotal * DESCUENTO
    else:
        descuento_aplicado = 0
    return descuento_aplicado

def mostrarCompra(cantidad_boletos, subtotal, descuento_aplicado, total_a_pagar):
    print("Detalles de la compra:")
    print(f"Cantidad de boletos: {cantidad_boletos}")
    print(f"Subtotal: {subtotal:.2f}")
    print(f"Descuento: {descuento_aplicado:.2f}")
    print(f"Total a pagar: {total_a_pagar:.2f}")
