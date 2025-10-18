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
print("### TE DEVUELVO TU PALABRA SIN VOCALES ###")
ingreso = str(input("Ingresa tu palabra: "))

while ingreso != '0':

    print(f"Haz ingresado {ingreso}, sin vocales es: ", sin_vocales(ingreso))
    ingreso = input("Ingresa otra palabra o escribe 0 para finalizar: ")

""" (4)
problema reemplaza_vocales (in s:seq<Char>) : seq<Char> {
    requiere: { |res| = |s| }
    asegura: { Para todo i perteneciente a Z, si 0 <= i < |res| -> ( pertenece(<'a','e','i','o','u'>, s[i] ^ res[i] = '_') o (¬pertenece(<'a','e','i','o','u'>, s[i]) ^ res[i] = s[i])  }
}

"""