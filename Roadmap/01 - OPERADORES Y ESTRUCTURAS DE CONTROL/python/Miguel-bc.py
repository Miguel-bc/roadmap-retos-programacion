
"""
/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */
"""

# Aritméticos
# + - * / // % **
# Suma / Resta / Multiplicacion / Division / Division Entera / Modulo / Potencia

A = float(input("Introduce el primer numero:"))
B = float(input("Introduce el segundo numero:"))

print("La suma es:", A+B)
print("La resta es:", A-B)
print("La multiplicacion es:", A*B)
print("La division es:", A/B)
print("La division entera es:", A//B)
print("El resto de la división es:", A%B)
print("El primer numero elevado al segundo es:", A**B)

# Relacionales
# == != < <= > >=

if A == B:
    print("Los numeros son iguales")
else:
    print("Los numeros son distintos") 
    
if A > B:
    print("El primer numero es mayor")
elif A < B:
    print("El segundo numero es  mayor")
else:
    print("Ningun numero es mayor que otro")

lista_1 = [1,2,3,4,5]
lista_2 = [1,2,3,4,9]

print(lista_1 != lista_2)

# Logicos
# and not

# Pertenencia
# in not in

i=0

while i < len(lista_1):
    print("Probando Lista", lista_1[i])
    i+=1
    
valor = 9

if valor in lista_1:
    print("El valor 9 esta en la lista_1")
elif valor in lista_2:    
        print("El valor 9 esta en la lista_2")
else:
    print("El valor 9 no esta en la lista_2")

# Identidad 
# is is not

# Asignacion
# += -= *= /= //= %= **=

