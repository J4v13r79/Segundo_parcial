'''Un conductor necesita conocer el rendimiento de combustible de su vehículo y el costo de un recorrido. El 
usuario deberá proporcionar la distancia recorrida en kilómetros y la cantidad de litros consumidos. El 
precio por litro será de $24.00. '''


# ENTRADAS: 
# Distancia recorrida (float positivo).
# Litros consumidos (float positivo).

#SALIDAS:
#rendimiento de combustible (float con dos decimales).
#costo del recorrido (float con dos decimales).

# REGLAS Y SUPUESTOS: 
#PRECIO_LITRO = 24.00
# no usar mas de 2 decimas. 

# ALGORITMO: 
# 1. Solicitar la distancia recorrida y los litros consumidos.
# 2. si litros consumidos > 0
#         rendimiento = distancia / litros
# 3. costo = litros * PRECIO_LITRO

# CASOS DE PRUEBA: 
#1. 10L , 120km: rendimiento = 12.00 km/L, costo = 240.00
#2. 20L , 250km: rendimiento = 12.50 km/L, costo = 480.00
#3. 15L , 180km: rendimiento = 12.00 km/L, costo = 360.00
#4. 25L , 300km: rendimiento = 12.00 km/L, costo = 600.00

# RESTRICCIONES PARA EL AGENTE: 
# 1. La única biblioteca externa permitida es tabulate. 
# 2. El codigo debe coincidir con los casos de prueba
# 3. no debe inclur funciones complejas como loops

# CONTRATO DE FUNCIONES: debe incluri cada una de esta como funciones
#   leerDatos: pide al usuario la distancia recorrida y los litros consumidos
#   calcularRendimiento : calcula el rendimiento de combustible en km/L
#   calcularCosto: calcula el costo del recorrido en pesos
#   mostrarResultados: muestra los resultados al usuario

def leerDatos():
    distancia = float(input("Ingrese la distancia recorrida en kilómetros: "))
    litros = float(input("Ingrese la cantidad de litros consumidos: "))
    return distancia, litros

def CalcularRendimiento():
    