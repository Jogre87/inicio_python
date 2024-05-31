# Operadores y Estructuras de Datos

var_1 = 25
var_2 = 15
sum = var_2 + var_2

print(sum)

print(f"SUMA: 50 + 20 = {50 + 20}") # Las Llaves ejecutan el operador la "f" al inicio es una manera de imprimir cadena de texto
print(f"RESTA: 50 - 20 = {50 - 20}")
print(f"MULTIPLICAR: 50 * 20 = {50 * 20}")
print(f"DIVIDIR: 50 / 20 = {50 / 20}")
print(f"MODULO: 10 % 3 = {10 % 3}") # Modulo se representa con % y equivale al resto de una division 
print(f"EXPONENTE: 3 ** 4 = {3 ** 4}")
print(f"DIVISION ENTERA : 10 // 3 = {10 // 3}") # En la division entera, no se imprimiran los decimales, solo numero entero redondeado

# Operadores de Comparacion (LAS RESPUESTAS SON BOOLEANAS SIEMPRE "TRUE / FALSE")
print(f"IGUALDAD: 50 == 20 es {50 == 20}") # Este Operador tambien sirve para comparar texto
print(f"DESIGUALDAD: 50 != 20 es {50 != 20}") # 
print(f"MAYOR QUE: 50 > 20 es {50 > 20}")
print(f"MENOR QUE: 50 < 20 es {50 < 20}")
print(f"MAYOR O IGUAL QUE: 50 >= 20 es {50 > 20}")
print(f"MENOR O IGUAL QUE: 50 <= 20 es {50 < 20}")

# Operadores Logicos (LAS RESPUESTAS SON BOOLEANAS SIEMPRE "TRUE / FALSE")
print(f"AND: 35 + 25 == 60 and 25 - 10 == 15 es {35 + 25 == 60 and 25 - 10 == 15}") # La respuesta es basada en ambas condiciones 
print(f"OR: 35 + 25 == 60 OR 25 - 10 == 15 es {35 + 25 == 60 or 25 - 10 == 35}") # La respuesta va en funcion de solo una de las dos condiciones
print(f"NOT: not 14 + 5 == 20 es {not 14 + 5 == 20}") # Este operador es una negacion anticipada 

# Operadores de Asigancion 
my_number = 15 #esto es una asigancion 
print(my_number)
my_number += 1 #suma y asignacion
print(my_number) 
my_number -= 1 #resta y asignacion
print(my_number)
my_number *= 2 #multiplica y asignacion
print(my_number)
my_number /= 4 #division y asignacion
print(my_number)
my_number %= 5 #modulo y asignacion
print(my_number)
my_number **= 5 #exponente y asignacion
print(my_number)
my_number //= 5 #division entera y asignacion
print(my_number)

# Operadores de Identidad
my_new_number = my_number
print(f"my_number is my_new_number es {my_number is my_new_number}")
print(my_new_number)
print(my_number)

#Operadores de Pertenencia (sirven para determinar si un objeto pertenece o no a un conjunto)

print(f"'u' in 'universo' {'u' in 'universo'}") #Operador in determina si esta dentro del conjunto
print(f"'u' not in 'jaula' {'u' not in 'jaula'}") #Operador not in determina si no esta dentro del conjunto

#Operadores de bit
a = 12
b = 6
print(f"AND: 12 & 6 = {12 & 6}") #Operador AND compara bit a bit si ambos son 1 resultado es 1  de lo contrario es 0
print(f"OR: 12 | 6 = {12 | 6}") #Operador OR compara bit a bit si ambos uno de los dos bits es 1 el resultado es 1 de lo contrario es 0
print(f"XOR: 12 ^ 6 = {12 ^ 6}") #Operador XOR compara bit a bit si ambos son diferentes resultado es 1  de lo contrario es 0
print(f"NOT: ~12 = {~12}") #Operador NOT invierte bit a bit
print(f"Desplazamineto derecha: 12 >> 3 = {12 >> 3}") #Desplaza dos bit el valor binario
print(f"Desplazamiento Izquierda: 12 << 3 = {12 << 3}") #Cubre con ceros el dezplasamiento






