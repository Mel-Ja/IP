import random

# ej 1 Codificar en Python las siguientes funciones sobre secuencias.
"""(1)
problema pertenece (in s:seq<Z>, in e:Z) : Bool {
    requiere: { True }
    asegura: { (res=True) <-> existe un i que pertenece a Z tal que 0 <= i < |s| y s[i]=e }
}

Implementar al menos 3 formas distintas éste problema
"""

def pertenece_while (s: list[int], e: int) -> bool:
    res: bool = False
    controlador: int = 0
    tamanio_lista = len(s)
    while controlador < tamanio_lista and not res:
        if s[controlador] == e:
            res= True
            return res
        else: controlador += 1
    
    return res

def pertenece_while2 (s: list[int], e: int) -> bool:
    i: int = len(s)-1
    while i >= 0:
        if s[i] == e:
            return True
        i -= 1
    return False

def pertenece_for (s: list[int], e: int) -> bool:
    longitud_lista: int = len(s)
    for posicion in range(0, longitud_lista, 1):
        if s[posicion] == e:
            return True
        
    return False


def pertenece_for2 (s: list[int], e:int) -> bool:
    for elemento_actual in s:
        print("El actual:", elemento_actual)
        if elemento_actual == e:
            return True
    
    return False

def pertenece_funciones(s: list[int], e: int) -> bool:
    if len(s) == 0:
        return False
    elif s.pop() == e:
        return True
    else:
        return pertenece_funciones(s, e)



# print("Pertenece 4 a lista [1,2,3,4]? ->", pertenece_for([1,2,3,4], 4))
# print("Pertenece 4 a lista [1,2,3,4]? ->", pertenece_for2([1,2,3,4], 4))
# print("Pertenece 4 a lista [1,2,3,4]? ->", pertenece_funciones([1,2,3,4], 2))
print("Pertenece 4 a lista [1,2,3,4]? ->", pertenece_while2([1,2,3,4], 2))


"""(2)
problema divide_a_todos(in s:seq<Z>, in e:Z) : Bool {
    requiere: { e != 0}
    asegura: { (res = true) <-> (para todo i∈Z si  0 <= i < |s| -> s[i] mod e = 0 ) }
}

"""

def divide_a_todos(lista: list[int], e: int) -> bool:
    for numero in lista:
        if numero % e != 0:
            return False
        
    return True

print("2 divide a cada ele de [2,4,8,10]? ->", divide_a_todos([2,4,8,10], 2))
print("3 divide a cada ele de [2,4,8,10]? ->", divide_a_todos([2,4,8,10], 3))

""" (3)
problema suma_total (in s:seq(Z)) : Z {
    requiere: { True }
    asegura: { res es la suma de todos los elementos de s  }
}

(+) No usar la función sum() nativa
"""

def suma_total (lista_numeros: list[int]) -> int:
    dimension_lista_numeros: int = len(lista_numeros) 
    suma_total: int = 0
    i: int = 0
    while i < dimension_lista_numeros:
        suma_total += lista_numeros[i]
        i +=1

    return suma_total

print("Suma de todos los elementos de [1,2,3,4] ->", suma_total([1,2,3,4]))
print("Suma de todos los elementos de [2,4,6,8] ->", suma_total([2,4,6,8]))
print("Suma de todos los elementos de [3,3,3,3] ->", suma_total([3,3,3,3]))

""" (4)
problema maximo (in s:seq<Z>) : Z {
    requiere: { |s| > 0 }
    asegura: { res = al mayor de todos los números que aparece en s }
}
(+) No utilizar la función max() nativa

lista [1,2,3] -> tomo primer elemento lista[0] = 1 -> comparo si lista[0] >= lista[1], si lo es entonces -> comparo si lista[0] >= lista[2], si es cierto entonces devuelve lista[0], si no entonces tomo lista[1] -> comparo si lista[1] > lista[2]. Si es cierto devuelvo lista[1] si no entonces devuelvo lista[2]


tomo primer elemento y lo comparo con las otras posiciones, si primerEl es mayor a los elementos n_maximo = primerEl, sino tomo el segundo elemento y comparo con elementos restantes


def maximo(lista_numeros: list[int]) -> int:
    dimension_lista: int = len(lista_numeros)
    j:int = 0
    n_maximo: int = 0
    while j < dimension_lista:
        #itera hasta que j no sea menor a dimension lista
        # ahora quiere tomar primer elemento y compararlo con resto de la lista
        elemento_actual = lista_numeros[j]
        for numero in lista_numeros:
            #recorro cada numero en la lista, si elemento_actual es mayor al numero este lo guarda en n_maximo
            if elemento_actual > numero:
                n_maximo = elemento_actual
    
        j+=1

    return n_maximo
"""

def maximo(lista_numeros: list[int]) -> int:
    #tomo primer elemento y lo uso para comparar...
    n_maximo = lista_numeros[0]
    i: int = 1
    dimension_lista = len(lista_numeros)
    #itero desde el segundo elemento
    while i < dimension_lista:
        elemento_actual: int = lista_numeros[i]
        if elemento_actual > n_maximo:
            n_maximo = elemento_actual
        i += 1

    return n_maximo



print("Número más grande en [1,2,3,4] ->", maximo([1,2,3,4]))
print("Número más grande en [3,3,3,1] ->", maximo([3,3,3,1]))
print("Número más grande en [2,1,3,12] ->", maximo([2,1,3,12]))
print("Número más grande en [2,2,3,1] ->", maximo([2,2,3,1]))
print("Número más grande en [-2,-3,-8] ->", maximo([-2,-3,-8]))

""" (5)
problema minimo (in s: seq<Z>) : Z {
    requiere: { |s| > 0 }
    asegura: { res = al menor de todos los números que aparece en s }
}
(+) No utilizar la función min() nativa
"""


def minimo(lista_enteros: list[int]) -> int:
    n_min: int = lista_enteros[0]
    i: int = 1
    while i < len(lista_enteros):
        if lista_enteros[i] < n_min:
            n_min = lista_enteros[i]
        i += 1
    
    return n_min

print("¿Cuál es el mín entre [1,2,3,4]", minimo([1,2,3,4]))
print("¿Cuál es el mín entre [30,20,40,10]", minimo([30,20,40,10]))
print("¿Cuál es el mín entre [11,22,1,40]", minimo([11,22,1,40]))

""" (6)
problema ordenados (in s:seq<Z>) : Bool {
    requiere: { True }
    asegura: { res = true <-> (para todo i∈Z si 0<=i<(|s|-1) -> s[i] < s[i+1]}
}
"""

def ordenados(lista_numero: list[int]) -> bool:
    i: int = 0
    while i < len(lista_numero) -1:
        if lista_numero[i] >= lista_numero[i+1]:
            return False
        
        i += 1
    
    return True

print("¿Están ordenados [1,2,3,4]?", ordenados([1,2,3,4]))
print("¿Están ordenados [1,2,3,1]?", ordenados([1,2,3,1]))
print("¿Están ordenados [4,2,3,5]?", ordenados([4,2,3,5]))


""" (7)
problema pos_maximo (in s:seq<Z>) : Z {
    requiere: {True}
    asegura: { Si |s|=0, entonces res=-1; sino, res= al índice de la posición donde aparece el mayor elemento de s (si hay varios es la primera aparición) }
}

"""

def pos_maximo(lista_num: list[int]) -> int:
    res: int

    if len(lista_num) == 0:
        res = -1
    else:
        num_max: int = lista_num[0]
        posicion_num_max: int = 0
        i: int = 1
        while i < len(lista_num):
            if lista_num[i] > num_max:
                num_max = lista_num[i]
                posicion_num_max = i
            i += 1
        
        res = posicion_num_max
            
    return res

print("Posición (0 siendo el primer lugar) de num máx de [] ->", pos_maximo([]))
print("Posición (0 siendo el primer lugar) de num máx de [1,2,3,4] ->", pos_maximo([1,2,3,4]))
print("Posición (0 siendo el primer lugar) de num máx de [1,2,30,4] ->", pos_maximo([1,2,30,4]))
print("Posición (0 siendo el primer lugar) de num máx de [10,2,3,4] ->", pos_maximo([10,2,3,4]))
print("Posición (0 siendo el primer lugar) de num máx de [1,20,3,4] ->", pos_maximo([1,20,3,4]))
print("Posición (0 siendo el primer lugar) de num máx de [10,10,3,4] ->", pos_maximo([10,10,3,4]))


""" (8)
problema pos_min (in s:seq<Z>) : Z {
    requiere: {True}
    asegura: {Si |s| = 0, entonces res=-1, sino, res=índice de la posición donde aparece el menor elemento de s (si hay varios es la última aparición)}
}

"""
def pos_min(lista_num: list[int]) -> int:
    res: int

    if len(lista_num) == 0:
        res = -1
    else:
        ele_min = lista_num[0]
        pos_ele_min = 0
        for i in range(1, len(lista_num), 1):
            if lista_num[i] < ele_min:
                ele_min = lista_num[i]
                pos_ele_min = i
            res = pos_ele_min

    return res


""" (9)
Dada una lista de palabras (seq<seq<Char>>), devolver verdadero si alguna palabra tiene longitud mayor a 7. Ejemplo:
["termo", "gato", "tener", "jirafas"], devuelve falso

problema long_mayorASiete(in s: seq<seq<Char>>) : Bool {
    requiere: { True }
    asegura: { (res = true) <-> (existe i∈Z tal que ( 0 <= i < |s|-1 ) y ( |s[i]| > 7 ) ) }

}

"""

def long_mayorASiete(palabras: list[str])-> bool:
    i: int = 0
    res = False

    while i < len(palabras):
        if len(palabras[i]) > 7:
            res = True
            return res
        
        i += 1
    
    return res

""" (10) Dado un texto en formato string, devolver verdadero si es palíndromo (se lee igual en ambos sentidos), falso en caso contrario. Las cadenas de texto vacías o con 1 sólo elemento son palíndromo
problema es_palindroma(in s:seq<Char>) : Bool {
    requiere: { True }
    asegura: { (res=true) <-> (s es igual a su reverso) }
}
"""

def es_palindroma(palabra: str) -> bool:
    res:bool
    palabra= palabra.lower()

    i: int = 0
    j: int = len(palabra)-1

    while i < j:
        if palabra[i] != palabra[j]:
            res = False
            return res

        i+=1
        j-=1

    res = True

    return res

print("---")
print("¿Es 'Ana' palíndromo?", es_palindroma("Ana"))

print("---")
print("¿Es 'Elefante' palíndromo?", es_palindroma("Elefante"))
print("---")
print("¿Es 'reconocer' palíndromo?", es_palindroma("reconocer"))
print("---")
print("¿Es '' palíndromo?", es_palindroma(""))


""" (11) Recorrer una seq<Z> y devolver si hay 3 números iguales consecutivos, en cualquier posición y False en caso contrario.
problema iguales_consecutivos (in s: seq<Z>) : Bool {
    requiere: { True }
    asegura: { (res=true) <-> (existe i,j,k perteneciente a Z tal que ( 0 <= i,j,k < (|s|-1) ) y (i+2 = j+1 = k) y ( s[i]=s[j]=s[k] )  }
}

"""

def es_longitud_valida(lista_num: list[int]) -> bool:
    return len(lista_num) >= 3


def son_consecutivos(lista_num: list[int]) -> bool:
    i: int = 0
    while i < len(lista_num) - 2:
        if lista_num[i] == lista_num[i+1] == lista_num[i+2]:
            return True
        i += 1

    return False

def iguales_consecutivos(lista_num: list[int]) -> bool:
    res: bool

    if es_longitud_valida(lista_num):
        res = son_consecutivos(lista_num)
        
    else:
        res=False

    return res


print("---")
print("Hay 3 consecutivos? [2,2,2]", iguales_consecutivos([2,2,2]))
print("---")
print("Hay 3 consecutivos? [2,2]", iguales_consecutivos([2,2]))
print("Hay 3 consecutivos? [2]", iguales_consecutivos([2]))
print("Hay 3 consecutivos? []", iguales_consecutivos([]))
print("---")
print("Hay 3 consecutivos? [1,2,2,2,3]", iguales_consecutivos([1,2,2,2,3]))
print("---")
print("Hay 3 consecutivos? [1,2,3,3,4]", iguales_consecutivos([1,2,3,3,4]))
print("---")
print("Hay 3 consecutivos? [1,2,3,3,3]", iguales_consecutivos([1,2,3,3,3]))
print("---")
print("Hay 3 consecutivos? [1,2,2,3,3]", iguales_consecutivos([1,2,2,3,3]))


""" (12) Recorrer una palabra en formato string y devolver True si ésta tiene al menos 3 vocales distintas y False en caso contrario.
problema vocales_distintas(in s: seq<Char>) : Bool {
    requiere: { True }
    asegura: { (res=true) <-> ( existe i,j,k perteneciente a Z tal que (0 <= i,j,k < (|s|-1))) y (s[i] != s[j] != s[k]) y (s[i], s[j], s[k] pertenece {'a','e','i','o','u'}) }
}

"""
def esVocal(letra: str) -> bool:
    vocales: list[str] = ['a', 'e', 'i', 'o', 'u']
    return letra in vocales

def es_vocal_repetida(letra:str, mis_vocales: list[str]) -> bool:
    return letra in mis_vocales

def vocales_distintas(palabra: str) -> bool:
    res: bool = False
    palabra = palabra.lower()
    mis_vocales: list[str] = []

#    if len(palabra) < 3:
#        return res
    
    for letra in palabra:
        if esVocal(letra) and not es_vocal_repetida(letra, mis_vocales):
            mis_vocales.append(letra)
    
    if len(mis_vocales) >= 3:
        res = True
    
    return res

print("---")
print("Tiene 3 vocales distintas? 'aei' ->", vocales_distintas("aei"))
print("---")
print("Tiene 3 vocales distintas? 'maseli' ->", vocales_distintas("maseli"))
print("---")
print("Tiene 3 vocales distintas? 'arbol' ->", vocales_distintas("arbol"))
print("---")
print("Tiene 3 vocales distintas? '' ->", vocales_distintas(""))
print("---")
print("Tiene 3 vocales distintas? 'cacatua' ->", vocales_distintas("cacatua"))
print("---")
print("Tiene 3 vocales distintas? 'oso' ->", vocales_distintas("oso"))
print("---")
print("Tiene 3 vocales distintas? 'tenora' ->", vocales_distintas("tenora"))




""" (13) Recorrer una seq<Z> y devolver la posición donde inicia la secuencia de números ordenada más larga. SI hay dos subsecuencias de igual longitud devolver la posición donde empieza la primera. La secuencia de entrada es no vacía

problema pos_secuencia_ordenada_mas_larga (in s:seq<Z>) : Z {
    requiere: { |s| > 0 }
    asegura: { (res=i) <-> ( existe i,j perteneciente Z tal que (0 <= i,j < (|j|-1))) y (para todo k tal que i <= k < j -> s[k] <= s[k+1]) y j-i+1 es máximo e i es el mínimo valor que lo cumple }
}

"""

def pos_secuencia_ordenada_mas_larga (lista_numeros: list[int]) -> int:

    inicio_actual: int = 0 #posición inicio de la subsecuencia en análisis
    largo_actual: int = 1 #largo de la subsecuencia actual
    inicio_max: int = 0 #posición inicio subsecuencia más larga encontrada 
    largo_max: int = 1 #largo máximo encontrado

    # Recorro a partir del segundo elemento
    i: int = 1
    while i < len(lista_numeros):
        if lista_numeros[i] >= lista_numeros[i - 1]:
            #está ordenada ascendentemente
            largo_actual += 1
        else:
            # secuencia interrumpida porque no está ordenada ascendentemente
            if largo_actual > largo_max:
                largo_max = largo_actual
                inicio_max = inicio_actual

            inicio_actual = i
            largo_actual = 1

        i+=1
    
    if largo_actual > largo_max:
        inicio_max = inicio_actual
        largo_max = largo_actual
    
    return inicio_max

print("---")
print("posición secuencia más larga? [1,2,2,1,3,5,4,6]", pos_secuencia_ordenada_mas_larga([1,2,2,1,3,5,4,6]))
print("---")
print("posición secuencia más larga? [1,2,2,3,5,7,4,6]", pos_secuencia_ordenada_mas_larga([1,5,2,3,5,7,4,6]))


""" (14) Cantidad de dígitos impares
problema cantidad_digitos_impares (in s:seq<Z>) : Z {
    requiere: { Todos los elementos de números son mayores o iguales a 0 }
    asegura: { res es la cantidad total de dígitos impares que aparecen en cada uno de los elementos de números }
}

Por ejemplo, si la lista de números es [57, 2383, 812, 246], entonces el resultado esperado sería 5 (los dígitos impares son 5,7,3,3 y 1)

"""

def cantidad_digitos_impares(lista_num: list[int]) -> int:
    res: int = 0
    cantidad_impares: int = 0
    for numero in lista_num:
        digitos_numero = str(numero)
        for digito in digitos_numero:
            if int(digito) % 2 != 0:
                cantidad_impares +=1

    res = cantidad_impares
    return res


print("---")
print("cantidad digitos impares de [10, 21, 32, 43] ->", cantidad_digitos_impares([10, 21, 32, 43]))
print("---")
print("cantidad digitos impares de [11, 31, 33, 53] ->", cantidad_digitos_impares([11, 31, 33, 53]))
print("---")
print("cantidad digitos impares de [0, 2, 4, 3] ->", cantidad_digitos_impares([0, 2, 4, 3]))
print("---")
print("cantidad digitos impares de [0, 2, 4] ->", cantidad_digitos_impares([0, 2, 4]))


# EJ 2 - Implementar las siguientes funciones sobre secuencias pasadas por parámetro
""" (1)
problema CerosEnPosicionesPares (inout s: seq<Z>) {
    requiere: { True }
    modifica: { s }
    asegura: { ( |s|= |s@pre| ) y ( para todo i entero, con 0 <= i < |s|, si i es impar entonces s[i] = s@pre[i] y, si i es par, entonces s[i]=0 ) }
}

"""
def cerosEnPosicionesPares(lista_num: list[int]) -> None:
    for indice in range(0, len(lista_num), 2):
        lista_num[indice] = 0
    
print("---")
lista: list[int] =[1,2,3,4]
print("Antes de entrar -> [1,2,3,4]\nLuego de entrar:" )
cerosEnPosicionesPares(lista)
print(lista)
print("---")
lista = [2,4,6,8,10]
print("Antes de entrar -> [2,4,6,8,10]\nLuego de entrar:")
cerosEnPosicionesPares(lista)
print(lista)
print("---")



""" (2)
problema CerosEnPosicionesPares2 (in s: seq<Z>) : seq<Z> {
    requiere: { True }
    asegura: { (|s|=|res|) y ( para todo i entero, con 0 <= i < |res|, si i es impar entonces res[i]=s[i] y, si i es par, entonces res[i] = 0 ) }
}

"""

def CerosEnPosicionesPares2(lista_num: list[int]) -> list[int]:
    nueva_lista: list[int] = lista_num.copy()
    for posicion in range(len(nueva_lista)):
        if posicion % 2 == 0:
            nueva_lista[posicion] = 0
    
    return nueva_lista

print("[50,60,70,80] ->", CerosEnPosicionesPares2([50,60,70,80]))
print("---")
print("[100,200,300,400,500] ->", CerosEnPosicionesPares2([100,200,300,400,500]))
print("---")


""" (3) Dada una cadena de caracteres devuelva una cadena igual a la anterior, pero sin las vocales. No se agregan espacios, sino que borra la vocal y concatena a continuación

problema sin_vocales (in s:seq<Char>) : seq<Char> {
    requiere: { True }
    asegura: { res es la subsecuencia de s que se obtiene al quitarle las vocales a s }
}

"""
def sin_vocales(palabra: str) -> str:
    nueva_palabra: str = ""
    i: int = 0
    while i < len(palabra):
        if not palabra[i].lower() in ['a', 'e', 'i', 'o', 'u']:
            nueva_palabra += palabra[i]
        i+=1

    return nueva_palabra

print("Hola->",sin_vocales("Hola"))
print("Palabra->",sin_vocales("Palabra"))
print("Melany->",sin_vocales("Melany"))
print("---")

""" Programa principal para probar sin_vocales 

print("### TE DEVUELVO TU PALABRA SIN VOCALES ###")
ingreso = str(input("Ingresa tu palabra: "))


while ingreso != '0':

    print(f"Haz ingresado {ingreso}, sin vocales es: ", sin_vocales(ingreso))
    ingreso = input("Ingresa otra palabra o escribe 0 para finalizar: ")
"""


""" (4)
problema reemplaza_vocales (in s:seq<Char>) : seq<Char> {
    requiere: { True }
    asegura: { |res| = |s| }
    asegura: { Para todo i perteneciente a Z, si 0 <= i < |res| -> ( pertenece(<'a','e','i','o','u'>, s[i] ^ res[i] = '_') o (¬pertenece(<'a','e','i','o','u'>, s[i]) ^ res[i] = s[i]))  }
}

"""

def reemplaza_vocales(palabra: str) -> str:
    nueva_palabra: str = ""
    vocales: list[str] = ["a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú"]
    for posicion in range(len(palabra)):
        if palabra.lower()[posicion] in vocales:
            nueva_palabra += "_"
        else:
            nueva_palabra += palabra[posicion]
    
    return nueva_palabra


""" (5)
problema da_vuelta_str (in s:seq<Char>) : seq<Char> {
    requiere: { True }
    asegura: { |res| = |s| }
    asegura: { Para todo i ∈ Z si 0 <= i < |res| -> res[i] = s[|s|-i-1] }
}

da_vuelta_str("Hola") -> "aloH"

"""
def da_vuelta_str (palabra: str) -> str:
    res: str = ""
    for posicion in range(len(palabra), 0, -1):
        res += palabra[posicion-1]
    
    return res

def da_vuelta_str_while (palabra: str) -> str:
    res: str = ""
    i: int = len(palabra) - 1
    while i >= 0:
        res += palabra[i]
        i -= 1
    return res

print("Melany ->", da_vuelta_str_while("Melany"))
print(" ->", da_vuelta_str_while(""))
print(" 1234 ->", da_vuelta_str_while("1234"))

""" (6)
problema eliminar_repetidos (in s: seq<Char>) : seq<Char> {
    requiere: { True }
    asegura: { (|res| <= |s|) ^ ( para todo i ∈ Z si 0 <= i <= |s| -> pertenece(s[i], res)) ^ (para todo i,j ∈ Z si (0 <= i,j < |res| ^ i != j) -> res[i] != res[j]  )  }
}

"""

def eliminar_repetidos(palabra: str) -> str:
    res: str = ""
    i: int = 0
    for letra in palabra:
        if letra not in res:
            res += letra
    return res

print("Ba n ana->", eliminar_repetidos("Ba n ana"))
print("Hola todo bien->", eliminar_repetidos("Hola todo bien"))

# ej 3
""" Implementar una función para conocer el estado de aprobación de una materia a partir de las notas obtenidas por un/a alumno/a cumpliendo con la siguiente especificación:

problema resultadoMateria (in notas: seq<Z>) : Z {
    requiere: { |notas| > 0 }
    requiere: { Para todo  i ∈ Z si 0 <= i < |notas| -> 0 <= notas[i] <= 10   }
    asegura: { res = 1 <-> todos los elementos de notas son mayores o iguales a 4 y el promedio es mayor o igual a 7 }
    asegura: { res = 2 <-> todos los elementos de notas son mayores o iguales a 4 y el promedio está entre 4(inclusive) y 7 }
    asegura: { res = 3 <-> alguno de los elementos de notas es menor a 4 o el promedio es menor a 4 }
}

"""
def mayor_o_igual_4(nota: int) -> bool:
    return nota >= 4

def resultadoMateria(notas: list[int]) -> int:
    suma_notas: int = 0
    res: int = 3

    for nota in notas:
        suma_notas += nota
        if not mayor_o_igual_4(nota):
            return res
    
    promedio: float = suma_notas / len(notas)

    if promedio >= 7:
        res = 1
        return res
    elif promedio >= 4: # No hace falta 'and promedio < 7'
        res = 2            # porque si fuera >= 7, ya habría entrado al 'if' de arriba
        return res
    else:
        return res
    
print("[8, 9, 7] ->", resultadoMateria([8, 9, 7]))
print("[4, 5, 6] ->", resultadoMateria([4, 5, 6]))
print("[10, 10, 1] ->", resultadoMateria([10, 10, 1]))
print("[2,2,3] ->", resultadoMateria([2,2,3]))


#ej 4
""" Dada una lista de tuplas, que representa un historial de movimientos en una cuenta bancaria, devolver el saldo actual. Asumir que el salgo inicial es 0. Las tuplas tienen una letra que nos indica el tipo de movimiento "I" para ingreso de dinero y "R" para retiro de dinero, y además el monto de cada operación. Por ejemplo, si la lista de tuplas es [("I", 2000), ("R", 20), ("R", 1000), ("I", 300)] entonces el salgo actual es 1280.

problema saldoActual (in movimientos: seq<Char x Z>) : Z {
    requiere: { Para todo i∈Z si 0 <= i < |movimientos| -> movimientos [i]0 ∈ {"I", "R"} y movimientos[i]1 > 0 }
    asegura: { res = sumatoria desde i hasta ingresos con movimientos[i]1 - sumatoria desde i hasta retiros de movimientos[i]1 }
}

"""


def saldoActual(movimientos: list[(str, int)]) -> int:
    saldo: int = 0

    for transaccion in movimientos:
        accion: str = transaccion[0] 
        monto: int = transaccion[1]
        if accion.upper() == "I":
            saldo += monto
        elif accion.upper() == "R":
            saldo -= monto

    return saldo


print("Esta semana ingresé $2300 y retiré $1020\nSaldo actual -> ", saldoActual([("I", 2000), ("R", 20), ("R", 1000), ("I", 300)]))

# ej 5 - Analizando parámetros in y out vs resultado

""" (1)
problema pertenece_a_cada_uno_version_1 (in s: seq<seq<Z>>, in e: Z, out res: seq<Bool>) {
    requiere: { True }
    asegura: { |res| >= |s| }
    asegura: { Para todo i∈Z si 0<= i < |s| -> ( res[i]=true <-> pertenece(s[i], e) )  }
}

Nota: reutilizar la función pertenece() implementada previamente para listas

"""

def pertenece_a_cada_uno_version_1 (matriz: list[list[int]], numero: int, res: list[bool]) -> None:
    res.clear()

    for fila in matriz:
        if pertenece_for(fila, numero):
            res.append(True)
        else:
            res.append(False)

# --- Pruebas ---
listas_de_notas: list[list[int]] = [[2, 4, 6], [7, 10], [1, 4, 9], []]
numero_a_buscar: int = 4

# 1. Creamos la lista 'res' ANTES de llamar a la función.
#    Incluso puede tener "basura" o estar vacía.
mi_resultado: list[bool] = [True, True, True, True, True, True] 

print(f" 'mi_resultado' ANTES de la función: {mi_resultado}")

# 2. Llamamos a la función. NO hacemos "x = pertenece_..."
#    Simplemente la llamamos.
pertenece_a_cada_uno_version_1(listas_de_notas, numero_a_buscar, mi_resultado)

# 3. Verificamos 'mi_resultado' DESPUÉS. Ha sido modificada.
print(f" 'mi_resultado' DESPUÉS de la función: {mi_resultado}")

""" (2)

problema pertenece_a_cada_uno_version_2 (in s: seq<seq<Z>>, in e: Z, out res: seq<Bool>) {
    requiere: { True }
    asegura: { |res| = |s| }
    asegura: { Para todo i∈Z si 0<= i < |s| -> ( res[i]=true <-> pertenece(s[i], e) )  }
}

-> Implementación de la versión 1 cumple contrato asegura |res| = |s|

"""

""" (3)
problema pertenece_a_cada_uno_version_2 (in s: seq<seq<Z>>, in e: Z) : seq<Bool> {
    requiere: { True }
    asegura: { |res| = |s| }
    asegura: { Para todo i∈Z si 0<= i < |s| -> ( res[i]=true <-> pertenece(s[i], e) )  }
}

"""
def pertenece_a_cada_uno_version_2 (matriz: list[list[int]], e: int) -> list[bool]:
    res: list[bool] = []

    for fila in matriz:
        if pertenece_for(fila, e):
            res.append(True)
        else:
            res.append(False)

    return res

# ej 6
""" (1)
problema es_matriz (in s: seq<seq<>Int>) : Bool {
    requiere: { True }
    asegura: { res = true <-> [s] }
}
"""
def es_matriz (matriz: list[int]) -> bool:
    if len(s) == 0:
        return False
    elif len(s[0]) == 0:
        return False

    cant_cols: int = len(s[0])

    for fila in matriz:
        if len(fila) != cant_cols:
            return False
    
    return True

""" (2)

"""
def filas_ordenadas(filas: list[list[int]], filas_ord: list[bool]):
    filas_ord.clear()

    for fila in filas:
        if ordenados(fila):
            filas_ord.append(True)
        else:
            filas_ord.append(False)

    return filas_ord


print("[[1,2,3], [1,2,3]] ->", filas_ordenadas([[1,2,3], [1,2,3]], []))
print("[[1,2,3], [3,2,3]] ->", filas_ordenadas([[1,2,3], [3,2,3]], []))


""" (3)
"""
def columna(matriz: list[list[int]], columna: int) -> list[int]:
    res: list[int] = []
    for fila in matriz:
        res.append(fila[columna])

    return res

print("------")
print("m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] c = 1 ->", columna([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1))


""" (4)
m = [[1, 2, 3], [4, 5, 6], [10, 3, 9]] -> [True, False, True]
"""
def columna_ordenadas(matriz: list[list[int]]) -> list[bool]:
    res: list[bool] = []

    nro_cols: int = len(matriz[0])

    for indice in range(nro_cols):
        #extraigo columna en indice
        col: list[int] = columna(matriz, indice)
        #verifico si está ordenada
        esta_ordenada: bool = ordenados(col)
        #agrego resultado a la lista
        res.append(esta_ordenada)

    return res
print("------")
print("[[1, 2, 3], [4, 5, 6], [10, 3, 9]]->", columna_ordenadas([[1, 2, 3], [4, 5, 6], [10, 3, 9]]))


""" (5)
[[1,2,3],[3,2,1],[4,3,5]] -> [[1,3,4], [2,2,3],[3,1,5]]
"""

def transponer(matriz: list[list[int]]) -> list[list[int]]:
    res: list[list[int]] = []

    nro_cols = len(matriz[0])

    for indice in range(nro_cols):
        col: list[int] = columna(matriz, indice)
        res.append(col)
    
    return res

print("------")
print("[[1,2,3],[3,2,1],[4,3,5]]->", transponer([[1,2,3],[3,2,1],[4,3,5]]))

""" (6)
Para determinar un ganador verificamos 8 líneas (3 horizontales, 3 verticales y 2 diagonales)
Se puede modularizar con una función auxiliar que se encargue del chequeo, recibirá una matriz y un jugador ('X' o 'O'), devolverá True si el jugados tiene 3 en línea y False si no
"""

def hay_3_en_linea(matriz: list[list[str]], jugador: str) -> bool:
    
    # Chequeo Horizontal
    for i in range(3):
        if matriz[i][0] == jugador and matriz[i][1] == jugador and matriz[i][2] == jugador:
            return True
    
    # Chequeo Vertical
    for i in range(3):
        if matriz[0][i] == jugador and matriz[1][i] == jugador and matriz[2][i] == jugador:
            return True
    
    # Chequeo Diagonal (top-left a bottom-right)
    if matriz[0][0] == jugador and matriz[1][1] == jugador and matriz[2][2] == jugador:
        return True
    
    # Chequeo Diagonal (bottom-right a top-left)
    if matriz[0][2] == jugador and matriz[1][1] == jugador and matriz[2][0] == jugador:
        return True
    
    return False
    
    

def quien_gana_tateti(matriz: list[list[int]]) -> int:
    if hay_3_en_linea(matriz, "O"):
        return 0
    elif hay_3_en_linea(matriz, "X"):
        return 1
    else:
        return 2
    

tablero_gana_x: list[list[str]] = [
    ["X", "O", "O"],
    [" ", "X", " "],
    ["O", " ", "X"]
]

tablero_gana_o: list[list[str]] = [
    ["X", "O", "X"],
    ["X", "O", " "],
    [" ", "O", " "]
]

tablero_empate: list[list[str]] = [
    ["X", "O", "X"],
    ["O", "O", "X"],
    ["X", "X", "O"]
]

print(f"Gana X (Diagonal): {quien_gana_tateti(tablero_gana_x)}") 
print(f"Gana O (Vertical): {quien_gana_tateti(tablero_gana_o)}") 
print(f"Empate: {quien_gana_tateti(tablero_empate)}")


# ej 7 - Programas interactivos ( con función input() ) que nos permita solicitar al usuario información cuando usamos las funciones

"""(1)
Implementar una función para contruir una lista con los nombre de mis estudiantes. La función solicitará al usuario los nombre hasta que ingrese la palabra "listo", o vacío (el usuario aprieta enter sin escribir nada). Devuelve la lista con todos los nombre ingresados

"""

def contruir_lista() -> list[str]:
    lista_estudiantes: list[str] = []
    solicitud: str = input("Ingrese nombre del primer estudiante: ")

    while solicitud.lower() != "listo" and solicitud != "":
        lista_estudiantes.append(solicitud)
        solicitud = input("Ingrese otro nombre (para finalizar ingrese 'listo': ")
    
    return lista_estudiantes

print(contruir_lista())

""" (2)
Implementar una función que devuelve una lista con el historial de un monedero electrónico (por ejemplo la SUBE). El usuario debe seleccionar en cada paso si quiere:
    - "C" = Cargar créditos
    - "D" = Descontar créditos
    - "X" = Finalizar la simulación (termina el programa)
En los casos de cargar y descontar créditos, el programa debe además solicitar el monto para la operación. Vamos a asumir que el monedero comienza en cero. Para guardar la información grabaremos el historial tuplas que representes los casos de cargar ("C", monto a cargar) y descontar crédito ("D", monto a descontar)
"""

def cargar(historial: list[tuple[str, int]]) -> None:
    monto: int = int(input("Monto a ingresar: "))
    historial.append(("C", monto))

def descontar(historial: list[tuple[str, int]]) -> None:
    monto: int = int(input("Monto a descontar: "))
    historial.append(("D", monto))

def hacer_movimientos(historial: list[tuple[str, int]]) -> None:
    entradas_validas: list[str] = ["C", "D", "X"]

    movimiento: str = input("Ingrese 'C' para cargar o 'D' para descontar o 'X' para finalizar: ").upper()

    while movimiento != "X":

        if movimiento == "C":
            cargar(historial)

        elif movimiento == "D":
            descontar(historial)

        else:
            print("Entrada inválida. Intente nuevamente")
        
        movimiento: str = input("'C' para cargar o 'D' para descontar o 'X' para finalizar: ").upper()



def historial_movimientos() -> list[tuple[str, int]]:
    monto_billetera: int = 0
    historial: list[tuple[str, int]] = []
    
    hacer_movimientos(historial)

    return historial

historial_final = historial_movimientos()
print("Historial de movimientos:")
print(historial_final)

""" (3)
Juego "7 y medio" -> deberá generar un número aleatorio entre 0 y 12 (excluyendo 8 y 9) y deberá luego de preguntarle al usuario si desea seguir sacando otra "carta" o plantarse. En este último caso el programa debe terminar.
Los números aleatorios obtenidos deberán sumarse según eo número obtenido salvo por las "figuras" (10,11, 12) que sumarán medio punto cada una.
El programa debe ir acumulando valores y si se pasa de 7.5 debe informar que el usuario ha perdido.
Al finalizar la función devuelve el historial de "cartas" que hizo que el usuario gane o pierda
Para generar números pseudo-aleatorios entre 1 y 12 utilizaremos la función random.randint(1,12). Al mismo tiempo, la función random.choice() puede ser de gran ayuda a la hora de repartir cartas
"""

"""
¿qué estados necesito para que el juego funcione?
    puntaje_actual: float = 0.0
    historial_cartas: list[int] = []
    jugando: bool = True

-> Creamos un "mazo" como una lista, con random.choice saco una carta...
    mazo: list[int] = [0,1,2,3,4,5,6,7,10,11,12]
-> Usamos random.choice() para sacar una carta cumpliendo que no sea ni 8 ni 9


funcion jugar_7_y_medio():
    puntaje = 0.0
    historial = []
    jugando = True
    mazo = [0,1,2,3,4,5,6,7,10,11,12]

    mientras (jugando==True):
        // Sacar carta
        carta_nueva = random.choice(mazo)
        historial.append(carta_nueva)

        // Calcular puntaje de esa carta
        si (carta_nueva >= 10):
            puntos_carta = 0.5
        sino:
            puntos_carta = carta_nueva
        puntaje += puntos_carta

        // Mostrar estado
        print("Sacaste: {carta_nueva}. Puntaje actual: {puntaje}.format(carta_nueva, puntaje))

        // Chequear estado del juego (Lose / Win / Continue)
        si (puntaje > 7.5):
            print("Perdiste, te pasaste de 7.5")
            jugando = False
        sino si (puntaje == 7.5):
            print("7 y medio ¡Ganaste!")
            jugando = False
        sino:
            //preguntar al usuario
            desicion = input("Deseas sacar otra carta (s) o plantarte (p)?")

            si (decision.lower() == "p"):
                print("Te plantaste con", puntaje)
                jugando = False
   
    //fin del bucle
    return historial

"""

def convertir_carta_a_puntos(carta: int) -> float:
    if carta >= 10:
        return 0.5
    else:
        return float(carta)

def jugar_siete_y_medio() -> list[int]:
    puntaje_actual: float = 0.0
    historial_cartas: list[int] = []
    jugando: bool = True
    mazo: list[int] = [0,1,2,3,4,5,6,7,10,11,12]
    print("Inicia el juego 7 medio. Inicias con 0 puntos")

    while jugando:
        #saco carta
        carta: int = random.choice(mazo)
        historial_cartas.append(carta)

        #calculo puntaje
        puntos: float = convertir_carta_a_puntos(carta)
        puntaje_actual += puntos

        #muestro estado
        print("Sacaste un", carta)
        print("Puntaje actual:", puntaje_actual)

        #Chequeo estado del juego
        if puntaje_actual > 7.5:
            print("Perdiste, te pasaste de 7.5")
            jugando = False
        elif puntaje_actual == 7.5:
            print("¡7 y medio! Ganaste")
            jugando = False
        else:
            decision: str = input("¿Sacar otra carta (s) o plantarte (p): ").lower()

            if decision == "p":
                print("Te plantaste con", puntaje_actual)
                jugando = False

    #fin del juego
    print("Juego finalizado")
    return historial_cartas

historial_partida = jugar_siete_y_medio()
print(f"El historial de cartas de la partida fue: {historial_partida}")


""" (4)
Analizar la fortaleza de una contraseña. Solicitar al usuario que ingrese un texto que será su contraseña. Armar una función que tenga de parámetro de entrada un string con la contraseña a analizar, y la salida otro string con tres posibles valores: VERDE, AMARILLA y ROJA. Nota: en python la ñ/Ñ es considerado carácter especial y no se comporta como cualquier letra. String es seq<Char>. Consejo: para ver si una letra es mayúscula se puede ver si está ordenada entre A y Z
    - La contraseña será VERDE si:
        a) la longitud es mayor a 8 caracteres
        b) tiene al menos 1 letra minúscula
        c) tiene al menos 1 letra mayúscula
        d) tiene al menos 1 dígito numérico (0..9)
    - La contraseña sera ROJA si:
        a) la longitud es menor a 5 caracteres
    - En caso contrario será AMARILLA
"""
def es_minuscula(caracter: str) -> bool:
    return caracter >= 'a' and caracter <= 'z'

def es_mayuscula(caracter: str) -> bool:
    return caracter >= 'A' and caracter <= 'Z'  

def es_digito(caracter: str) -> bool:
    return caracter >= '0' and caracter <= '9'

def analizar_fortaleza(password: str) -> str:
    #check ROJA
    longitud: int = len(password)
    if longitud < 5:
        return "ROJA"
    
    #inicializo flags
    tiene_minuscula: bool = False
    tiene_mayuscula: bool = False
    tiene_digito: bool = False

    #recorro password y capturo flags
    for caracter in password:
        if es_minuscula(caracter):
            tiene_minuscula = True
        elif es_mayuscula(caracter):
            tiene_mayuscula = True
        elif es_digito(caracter):
            tiene_digito = True
    
    #check VERDE
    es_verde: bool = (longitud > 8 and tiene_minuscula and tiene_mayuscula and tiene_digito)

    if es_verde:
        return "VERDE"
    else:
        return "AMARILLA"

print("Hola ->", analizar_fortaleza("Hola"))
print("hola_2 ->", analizar_fortaleza("Hola_2"))
print("Hola2 ->", analizar_fortaleza("Hola2"))
print("Hola2_Hola ->", analizar_fortaleza("Hola2_Hola"))