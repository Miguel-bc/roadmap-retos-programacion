"""
* DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */
"""

def multiplo(A:str, B:str) -> float:
    lista = list(range(1,101))
    numeros = 0       
    for i in range(0,100):
        cadena = ""
        if lista[i] % 3 == 0:
            cadena = "El número es múltiplo de 3."
            numeros += 1
        if lista[i] % 5 == 0:
            cadena = "El número es múltiplo de 5."
            numeros += 1
        if lista[i] % 5 == 0  and lista[i] % 3 == 0:
            cadena = "El número es múltiplo de 3 y 5."
            numeros += 1          
            
        if cadena == "":
            print(lista[i])
        else:
            print(cadena)   
    
    return(numeros)
                    
            
print(multiplo("Multiplo de 3","Multiplo de 5"))
