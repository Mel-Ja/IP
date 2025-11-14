from queue import LifoQueue as Pila    
from queue import Queue as Cola
from typing import TextIO
import random

# PILAS

#ej 1
"""
problema generar_nros_al_azar (in cantidad: Z, in desde: Z, in hasta: Z) : Pila[Z] {
    requiere: {cantidad >= 0}
    requiere: {desde ≤ hasta}
    asegura: {El tamaño de res es igual a cantidad}
    asegura: {Todos los elementos de res son valores entre desde y hasta (ambos inclusive), seleccionados aleatoriamente con probabilidad uniforme}
}


Para generar números en un rango con probabilidad uniforme, pueden usar la función random.randint(<desde>, <hasta>) que devuelve un número en el rango indicado. Recuerden importar el módulo random con `import random`. Además, pueden usar la clase `LifoQueue()` que es un ejemplo de una implementación básica de una pila:

from queue import LifoQueur as Pila
p = Pila() #crea una pila
p.put(1) #apila un 1
elemento = p.get() # desapila último elemento que ingreso
p.empty() #devuelve True si y sólo si la pila está vacía

"""

def generar_random(desde: int, hasta: int) -> int:
    nro_random: int = random.randint(desde, hasta)
    return nro_random

def generar_nros_al_azar(cantidad: int, desde: int, hasta: int) -> Pila[int]:
    pila_nros_al_azar: Pila[int] = Pila()

    for i in range(cantidad):
        pila_nros_al_azar.put(generar_random(desde, hasta))


    return pila_nros_al_azar

"""
pila_resultado = generar_nros_al_azar(10, 5, 20)
print("10 numeros entre 5 y 20 ->", pila_resultado) # print no muestra el contenido, muestra objeto Pila

# Para verificar el contenido, desapilo:
print("Contenido de la pila (desapilando):")
while not pila_resultado.empty():
    print(pila_resultado.get())

print(pila_resultado.empty())
"""



# ej 2
"""
problema cantidad_elementos(in p: Pila) : Z {
    requiere: {True}
    asegura: {res es igual a la cantidad de elementos que contiene p}
}

-> No se puede usar la función LifoQueue.qsize(). Tenes en cuenta que, al usar get() para recorrer la pila, se modifica el parámetro de entrada, ya que los elementos se eliminar al accederse. Dado que la especificación lo define como de tipo in, debe restaurarse posteriormente

"""

def cantidad_elementos(pila: Pila) -> int:
    pila_aux: Pila = Pila()
    cant_ele_pila: int = 0

    while not pila.empty():
        elemento = pila.get()
        pila_aux.put(elemento)
        cant_ele_pila += 1

    while not pila_aux.empty():
        elemento = pila_aux.get()
        pila.put(elemento)

    return cant_ele_pila

"""
print("--------------------")

mi_pila = Pila()
mi_pila.put(1)
mi_pila.put(2)
mi_pila.put(3)
resultado = cantidad_elementos(mi_pila)
print(resultado)
"""

# ej 3
"""
"""

def buscar_el_maximo(p: Pila[int]) -> int:
    pila_aux: Pila[int] = Pila()
    
    primer_elemento: int = p.get()
    num_max: int = primer_elemento
    pila_aux.put(primer_elemento)
    
    while not p.empty():
        elemento: int = p.get()
        if elemento > num_max:
            num_max = elemento

        pila_aux.put(elemento)
    
    while not pila_aux.empty():
        elemento: int = pila_aux.get()
        p.put(elemento)
    
    return num_max

"""
mi_pila = Pila()
mi_pila.put(10)
mi_pila.put(5)
mi_pila.put(99)
mi_pila.put(420)
mi_pila.put(1)

print("--------------------")

max_obtenido = buscar_el_maximo(mi_pila)
print("max encontrado en mi_pila=[10,5,99,420,1]:", max_obtenido)
"""

# ej 4
"""
[(str, int)] -> (str, int)

[("Juan", 4), ("Ana", 10), ("Pedro", 7), ("Mica", 9)]


"""
def buscar_nota_max(p: Pila[tuple[str, int]]) -> tuple[str, int]:
    pila_aux: Pila[tuple[str, int]] = Pila()

    primera_tupla: tuple[str, int] = p.get()
    max_tupla: tuple[str, int] = primera_tupla

    pila_aux.put(primera_tupla)

    while not p.empty():
        tupla_actual: tuple[str, int] = p.get()

        if tupla_actual[1] > max_tupla[1]:
            max_tupla = tupla_actual
        
        pila_aux.put(tupla_actual)
    
    while not pila_aux.empty():
        p.put(pila_aux.get())
    
    return max_tupla

"""
print("--------------------")

pila_alumnos: Pila[tuple[str, int]] = Pila()

pila_alumnos.put(("Juan", 4))   
pila_alumnos.put(("Pedro", 7))
pila_alumnos.put(("Ana", 10))
pila_alumnos.put(("Mica", 9))

tupla_ganadora = buscar_nota_max(pila_alumnos)
print(f"La tupla con la nota máxima es: {tupla_ganadora}")
"""


# ej 5

def esta_bien_balanceada(s: str) -> bool:
    """
    Verifica si los paréntesis en un string 's' están correctamente balanceados usando una Pila.

    Requiere: s solo tiene números, espacion, '()', '+', '-', '*', '/'
    Asegura: res = true <-> ( conteo de '(' == conteo de ')' ) y ( para todo prefijo, conteo de ')' <= conteo '(' )

    Guardo en una pila los paréntesis de apertura que están "esperando" ser cerrados

    """

    pila_aper: Pila[str] = Pila()

    for caracter in s:
        if caracter == '(':
            pila_aper.put(caracter)

        elif caracter == ')':
            #Si encuentro un ')' pero la pila está vacía entonces está de más en este prefijo
            if pila_aper.empty():
                return False
            else:
                pila_aper.get()
    
    #Al final del recorrido, la pila debería estar vacía, si no lo está, entonces quedaron paréntesis sin cerrar

    if pila_aper.empty():
        return True
    else:
        return False

"""
print("--------------------")

print("1 + (2 x 3 = (20 / 5)) ->", esta_bien_balanceada("1 + (2 x 3 = (20 / 5))"))
print("1 + ) 2 x 3 ( () ->", esta_bien_balanceada("1 + ) 2 x 3 ( ()"))
"""
# ej 6
"""
evaluar_exp("2 3 +") -> 2 + 3 -> 5 

1. dividir expresión en tokens (operandos y operadores) usando espacion como delimitadores
2. recorrer cada token -> si es un operando entonces lo agrego a la pila
                    -> si es un operador, saca los dos operandos uperiores de la pila, aplícale el operando y luego coloca el resultado en la pila

expresion = "3 5 + 5 * 2 -" #output esperado: 33

-es 3 un operador? no, entonces lo meto en la pila_operador (pila_operador = [3])
-es 5 un operador? no, entonces lo temro en la pila_operador (pila_operador = [3, 5])
-es + un operador? si, lo guardo en operador_actual 
-Saco de la pila los elementos. Sale el último que entro, el 5 y lo meto en pila_para_operar
-¿la pila está vacia? no, ahora tomo el 3 y lo meto en pila_para_operar
-¿pila está vacía? si, entonces sale último elemento que entro en pila_para_operar

"""
def es_operador(caracter: str) -> bool:
    return caracter in ['+', '-', '*', '/']


def operar(op1: str, op2: str, operador_actual: str) -> str:
    op1 = float(op1)
    op2 = float(op2)

    if operador_actual == '+':
        return str(op1 + op2)
    elif operador_actual == '-':
        return str(op1 - op2)
    elif operador_actual == '*':
        return str(op1 * op2)
    else:
        return str(op1 / op2)
    
def tokenizar(s: str) -> list[str]:
    """
    Separa un string en una lista de "tokens" usando el espacio ' ' como delimitador
    """
    lista_tokens: list[str] = []
    token_actual: str = ""

    for caracter in s:
        if caracter == " ":
            #si es un espacio entonces ya tenemos un token formado, lo guardamos
            lista_tokens.append(token_actual)
            token_actual = ""
        else:
            #caracter es una letra o número
            token_actual = token_actual + caracter

    # al final del bucle queda el último token sin guardar, ya que no vuelve a haber un espacio (donde se mete el token actual en la lista)
    lista_tokens.append(token_actual)

    return lista_tokens


def evaluar_expresion(s: str) -> float:
    pila_operando: Pila = Pila()
    lista_tokens: list[str] = tokenizar(s)

    for token in lista_tokens:
        if es_operador(token):
            op2: str = pila_operando.get()
            op1: str = pila_operando.get()
            resultado: str = operar(op1, op2, token)

            pila_operando.put(resultado)

        else:
            pila_operando.put(token)

   
    
    resultado: str = pila_operando.get()

    return float(resultado)
"""
print("--------------------")

expresion = "3 4 + 5 * 2 -"
print(f"Resultado de '{expresion}': {evaluar_expresion(expresion)}")

expresion_2 = "10 2 / 3 +"
print(f"Resultado de '{expresion_2}': {evaluar_expresion(expresion_2)}")
"""

# ej 7

"""
pila(1,2,3), p2('uno', 'dos', 'tres') -> res = (1, 'uno', 2, 'dos', 3, 'tres'). p1 y p2 siguen igual, res tiene que respetar el orden original

p1_aux = (3,2,1), p2_aux = ('tres', 'dos', 'uno')
me

"""



def intercalar(p1: Pila, p2: Pila) -> Pila:
    pila_intercalada: Pila = Pila()
    p1_aux: Pila = Pila()
    p2_aux: Pila = Pila()

    while not p1.empty():
        p1_aux.put(p1.get())
        p2_aux.put(p2.get())

    while not p1_aux.empty():
        elem1 = p1_aux.get()
        elem2 = p2_aux.get()

        p1.put(elem1)
        p2.put(elem2)

        pila_intercalada.put(elem1)
        pila_intercalada.put(elem2)
    
    return pila_intercalada


# COLAS

# ej 8

def generar_n_al_azar(cantidad: int, desde: int, hasta: int) -> Cola[int]:
    nros_al_azar: Cola[int] = Cola()

    for i in range(cantidad):
        nros_al_azar.put(generar_random(desde, hasta))


    return nros_al_azar

# ej 9
def cantidad_de_elementos(c: Cola) -> int:
    cola_aux: Cola = Cola()
    cta_elementos: int = 0

    while not c.empty():
        cola_aux.put(c.get())
        cta_elementos += 1
    
    while not cola_aux.empty():
        c.put(cola_aux.get())
    
    return cta_elementos


# ej 10
def buscar_maximo(c: Cola[int]) -> int:

    c_aux: Cola[int] = Cola()
    n_max: int = c.get() #tomo primer elemento de cola LIFO
    c_aux.put(n_max)

    while not c.empty():
        elem_actual = c.get()
        if elem_actual > n_max:
            n_max = elem_actual
        c_aux.put(elem_actual)
    
    while not c_aux.empty():
        c.put(c_aux.get())
    
    return n_max

cola_maxima = Cola()
cola_maxima.put(20)
cola_maxima.put(30)
cola_maxima.put(40)
print(buscar_maximo(cola_maxima))


# ej 11
def buscar_nota_min(c: Cola[tuple[str, int]]) -> tuple[str, int]:
    c_aux: Cola[tuple[str, int]] = Cola()
    tupla_minima: tuple[str, int] = c.get()
    c_aux.put(tupla_minima)

    while not c.empty():
        tupla_actual: tuple[str, int] = c.get()

        if tupla_actual[1] < tupla_minima[1]:
            tupla_minima = tupla_actual
        
        c_aux.put(tupla_actual)

    while not c_aux.empty():
        c.put(c_aux.get())
    
    return tupla_minima

#ej 12
def intercalar_cola(c1: Cola, c2: Cola) -> Cola:
    cola_intercalada: Cola = Cola()
    c1_aux: Cola = Cola()
    c2_aux: Cola = Cola()

    while not c1.empty():
        elem1 = c1.get()
        elem2 = c2.get()

        cola_intercalada.put(elem1)
        cola_intercalada.put(elem2)

        c1_aux.put(elem1)
        c2_aux.put(elem2)


    while not c1_aux.empty():
        c1.put(c1_aux.get())
        c2.put(c2_aux.get())
    
    return cola_intercalada

# ej 13 - (1)

def armar_secuencia_de_bingo() -> Cola[int]:
    res: Cola[int] = Cola()
    numeros_generados: list[int] = []
    for numero in range(100):
        numeros_generados.append(numero)

    for i in range(100):
        indice_aleatorio: int = random.randint(0, len(numeros_generados) - 1)

        numero_sacado: int = numeros_generados.pop(indice_aleatorio)

        res.put(numero_sacado)

    return res

# (2)
"""
carton = [20, 40, 28, 19, 4, 10, 42, 11, 50, 88, 77, 30]
bolillero = 100 núneros ordenados al azar del 0 al 99, sin repetidos

numeros_salientes: list[int]

while not carton_lleno
    jugadas_min += 1

"""
def jugar_carton_de_bingo(carton: list[int], bolillero: Cola[int]) -> int:
    jugadas_min_para_llenar_carton: int = 0
    carton_lleno: int = 0
    bolillero_aux: Cola[int] = Cola()

    while carton_lleno < 12:
        sacar_numero: int = bolillero.get()
        bolillero_aux.put(sacar_numero)
        jugadas_min_para_llenar_carton += 1

        if sacar_numero in carton:
            carton_lleno += 1
    

    while not bolillero.empty():
        bolillero_aux.put(bolillero.get())

    while not bolillero_aux.empty():
        bolillero.put(bolillero_aux.get())
        
    return jugadas_min_para_llenar_carton


# ej 14
"""
[('Mel', 3, 'Clínico'), ('Tom', 1, 'Traumatólogo'), ('Key', 5, 'Clínico')]

"""


def pacientes_urgentes(c: Cola[tuple[int, str, str]]) -> int:
    cantidad_urgentes: int = 0
    c_aux: Cola = Cola()

    while not c.empty():
        paciente_actual = c.get()
        prioridad: int = paciente_actual[0]
        c_aux.put(paciente_actual)

        if prioridad < 4:
            cantidad_urgentes += 1

    while not c_aux.empty():
        c.put(c_aux.get())

    return cantidad_urgentes

# ej 15

"""
problema ordenar_por_prioridad(in c: Cola[seq<Char> x Z x bool x bool]) : Cola[seq<Char> x Z x bool x bool] {
    requiere: { True }
    asegura: { |res| = |c| }
    asegura: { res contiene los mismos elementos que c }
    asegura: { res es la unión de tres colas P, F, R }

    asegura: { P contiene todos los clientes de c donde el cuarto componente de la tupla es True }
    asegura: { F contiene todos los clientes de c donde el cuarto componente es False y el tercer componente es True }
    asegura: { R contiene todos los clientes de c donde el tercer y cuarto componente es False }

    asegura: { El orden relativo de los clientes dentro de P, F y R es el mism que tenían en c}
}

(nombre_apellido, dni, tipo_cuenta, tiene_prioridad )
[('Mel Apaza', 39500777, False, False), ('Tom tres', 23122024, False, False)]

tipos_de_cuentas = [preferencial, no preferencial]
tiene_prioridad = ['mayor a 65', 'embarazada', 'movilidad reducida']

tiene_prioridad -> preferencial -> resto

"""

def atencion_a_clientes(c: Cola[tuple[str, int, bool, bool]]) -> Cola[tuple[str, int, bool, bool]]:
    """
    Reordena una cola de clientes según las prioridades (Prioridad > Preferencias > Resto) manteniendo el orden de llegada (FIFO) dentro de cada grupo
    Restaura la cola de entrada 'c'
    """
    cola_prioridad_alta: Cola[tuple[str, int, bool, bool]] = Cola()
    cola_preferencial: Cola[tuple[str, int, bool, bool]] = Cola()
    cola_comun: Cola[tuple[str, int, bool, bool]] = Cola()
    cola_aux: Cola[tuple[str, int, bool, bool]] = Cola()
    cola_ordenada: Cola[tuple[str, int, bool, bool]] = Cola()

    while not c.empty():
        cliente: tuple[str, int, bool, bool] = c.get()
        cola_aux.put(cliente)

        tiene_prioridad: bool = cliente[2]
        es_preferencial: bool = cliente[3]

        if tiene_prioridad:
            cola_prioridad_alta.put(cliente)
        elif es_preferencial:
            cola_preferencial.put(cliente)
        else:
            cola_comun.put(cliente)

    while not cola_aux.empty():
        c.put(cola_aux.get())
    

    while not cola_prioridad_alta.empty():
        cola_ordenada.put(cola_prioridad_alta.get())

    while not cola_preferencial.empty():
        cola_ordenada.put(cola_preferencial.get())
    
    while not cola_comun.empty():
        cola_ordenada.put(cola_comun.get())
    

    return cola_ordenada

# DICCIONARIOS

#ej 16
"""

[('Mel', 8.5),('Sole', 8.0), ('Mel', 10.0)] -> {'Mel': 9.25, 'Sole': 8.0}
"""


def calcular_promedio_por_estudiante(notas: list[tuple[str, float]]) -> dict[str, list[float]]:
    notas_estudiantes: dict[str, list[float]] = {}
    promedio_estudiantes: dict[str, float] = {}

    for nota_estudiante in notas:
        nombre: str = nota_estudiante[0]
        nota: float = nota_estudiante[1]

        if nombre not in notas_estudiantes.keys():
            notas_estudiantes[nombre] = [nota]
        else:
            notas_estudiantes[nombre].append(nota)
    
    for nombre, notas in notas_estudiantes.items():
        suma_notas: float = 0.0
        promedio: float = 0.0

        for nota in notas:
            suma_notas += nota

        promedio = suma_notas / len(notas)

        promedio_estudiantes[nombre] = promedio
    
    return promedio_estudiantes


# ej 17
"""
historiales: dict[str, Pila[str]] -> {'nombre_usuario': Pila[str]}

crear un diccionarios llamado historiales, almacenará el historial de navegación de cada usuario
Claves del diccionario serán nombreUsurio y los valores serán pilas de String

historiales = { 'melUsuario': Pila['www.google.com', 'www.infobae.com'], 'tomUsuario': Pila['www.perros.com', 'wwww.noticias.com] }



"""

def visitar_sitio(historiales: dict[str, Pila[str]], usuario: str, sitio: str) -> None:
    
    if usuario not in historiales.keys():
        nueva_pila: Pila[str] = Pila()
        nueva_pila.put(sitio)
        historiales[usuario] = nueva_pila
    else:
        historiales[usuario].put(sitio)


def navegar_atras(historiales: dict[str, Pila[str]], usuario: str) -> str:
    return historiales[usuario].get()

#ej 18
""" Sistema de gestión de inventario para una tienda de ropa. Ete sistema lleva registro de los productos en el inventario y hace operaciones como agregar nuevos productos, actualizar las existencias y calcular el valor total del inventario

inventario: dict[str, dict[str, float || int] ] -> almacena toda la info de los productos {'nombreProducto': { 'precio': numero, 'cantidad': numero}}
"""

def agregar_producto(inventario: dict[str, dict[str, int | float]], nombre: str, precio: float, cantidad: int):
    """ Agrego producto *nombre* al *inventario* y le agrego su precio con *precio* y cantidad con *cantidad
    """
    inventario[nombre] = {}
    inventario[nombre]["precio"] = precio
    inventario[nombre]["cantidad"] = cantidad

def actualizar_stock(inventario: dict[str, dict[str, int | float]], nombre: str, cantidad: int):    
    inventario[nombre]['cantidad'] = cantidad

def actualizar_precio(inventario: dict[str, dict[str, int | float]], nombre: str, precio: float):
    inventario[nombre]['precio'] = precio

def calcular_valor_inventario(inventario: dict[str, dict[str, int | float]]) -> float:
    valor_total_inventario: float = 0.0

    for info_producto in inventario.values():
        precio_producto: float = info_producto['precio']
        cantidad_producto: int = info_producto['cantidad']

        valor_total_inventario += cantidad_producto * precio_producto   
    
    return valor_total_inventario

# ARCHIVOS

# ej 19
def contar_lineas(nombre_archivo: str) -> int:
    archivo: TextIO = open(nombre_archivo, "r", encoding="utf8")
    lineas: list[str] = archivo.readlines()
    archivo.close()
    return len(lineas)

def existe_palabra(nombre_archivo: str, palabra: str) -> bool:
    archivo: TextIO = open(nombre_archivo, "r", encoding="utf8")
    lineas: list[str] = archivo.readlines()
    archivo.close()

    res: bool = False
    i: int = 0
    while i < len(lineas) and not res:

        if palabra in lineas[i]:
            res = True
        
        i += 1

    return res


def apariciones_en_linea(linea: str, palabra: str) -> int:
    longitud_linea: int = len(linea)
    longitud_palabra: int = len(palabra)
    apariciones_encontradas: int = 0

    if longitud_palabra > longitud_linea:
        return 0
    

    rango_busqueda: int = len(linea) - len(palabra) + 1

    for indice_ventana in range(rango_busqueda):
        """Controla el inicio de la 'ventana'"""
        es_coincidencia: bool = True

        for indice_caracter_palabra in range(longitud_palabra):
            """"Compara letra por letra"""

            indice_linea: int = indice_ventana + indice_caracter_palabra

            caracter_linea: str = linea[indice_linea]
            caracter_palabra: str = palabra[indice_caracter_palabra]

            if caracter_linea != caracter_palabra:
                # no coincide
                es_coincidencia = False
        if es_coincidencia:
            apariciones_encontradas +=1

    return apariciones_encontradas

def cantidad_de_apariciones(nombre_archivo: str, palabra: str) -> int:
    archivo: TextIO = open(nombre_archivo, "r", encoding="utf8")
    lineas: list[str] = archivo.readlines()
    archivo.close()

    cantidad_apariciones: int = 0

    for linea in lineas:
        cantidad_apariciones += apariciones_en_linea(linea, palabra)
    return cantidad_apariciones

# ej 20
""" Se consideran como palabras todas aquellas secuencias de caracteres deliminadas por espacios en blanco
'soy key si'

soy -> long_palabra_actual = 3 -> palabras_por_longitud[3] = 1
k

"""

def tokenizar_linea(linea: str) -> list[str]:
    """Separa linea en una lista de palabras, usando ' ' y \n como delimitadores"""
    palabras: list[str] = []
    palabra_actual: str = ""

    delimitadores: list[str] = [' ', '\n']

    for caracter in linea:
        if caracter not in delimitadores:
            palabra_actual += caracter
        else:
            if palabra_actual != "":
                palabras.append(palabra_actual)
                palabra_actual = ""
        
    if palabra_actual != "":
        palabras.append(palabra_actual)

    return palabras

def agrupar_por_longitud(nombre_archivo: str,) -> dict[int, int]:
    archivo: TextIO = open(nombre_archivo, "r", "utf8")
    lineas: list[str] = archivo.readlines()
    archivo.close()

    palabras_por_longitud: dict[int, int] = {}

    for linea in lineas:
        lista_palabras: list[str] = tokenizar_linea(linea)

        for palabra in lista_palabras:
            longitud_palabra = len(palabra)
            if longitud_palabra not in palabras_por_longitud:
                palabras_por_longitud[longitud_palabra] = 1
            else:
                palabras_por_longitud[longitud_palabra] += 1

    return palabras_por_longitud


# ej 21

def la_palabra_mas_frecuente(nombre_archivo: str) -> str:
    archivo: TextIO = open(nombre_archivo, "r", "utf8")
    lineas: list[str] = archivo.readlines()
    archivo.close()

    frecuencia_de_cada_palabra: dict[str, int] = {}
    for linea in lineas:
        lista_palabras: list[str] = tokenizar_linea(linea)

        for palabra in lista_palabras:
            if palabra not in frecuencia_de_cada_palabra:
                frecuencia_de_cada_palabra[palabra] = 1
            else:
                frecuencia_de_cada_palabra[palabra] += 1


    palabra_mas_frecuente: str = ""
    frecuencia_max: int = 0
    
    for palabra, frecuencia in frecuencia_de_cada_palabra.items():
        if frecuencia > frecuencia_max:
            frecuencia_max = frecuencia
            palabra_mas_frecuente = palabra 

    return palabra_mas_frecuente

# ej 22
def es_comentario(linea: str) -> bool:
    i: int = 0

    while i < len(linea) and (linea[i] == " " or linea[i] == "\t"):
        """ sigue iterando hasta que i sea menor a la longitud de la linea y hasta que la posicion donde está de la línea no sea un espacio y tabulación, si se cuenta con algo diferente a ello entonces corte el bucle
        """
        i+=1
    
    if i == len(linea):
        """ esto significa que toda la linea eran espacios y/o tabulaciones"""
        return 0
    
    return linea[i] == "#"

def clonar_sin_comentarios(nombre_archivo_entrada: str, nombre_archivo_salida: str):
    archivo: TextIO = open(nombre_archivo_entrada, "r", encoding="utf8")
    lineas_filtradas: list[str] = []

    for linea in archivo.readlines():
        if not es_comentario(linea):
            lineas_filtradas.append(linea)

    archivo.close()

    archivo_destino: TextIO = open(nombre_archivo_salida, "w", encoding="utf-8")
    archivo_destino.truncate()

    for linea in lineas_filtradas:
        archivo_destino.write(linea)
    
    archivo_destino.close()

# ej 23
def eliminar_salto_linea(linea: str) -> str:
    long_linea: int = len(linea)
    if long_linea > 0 and linea[long_linea-1] == "\n":
        nueva_linea: str = ""
        for i in range(long_linea-1):
            nueva_linea += linea[i]
        
        return nueva_linea

    return linea

def invertir_lineas(nombre_archivo: str, nombre_salida: str):
    archivo: TextIO = open(nombre_archivo, "r", encoding="utf-8")
    lineas: list[str] = archivo.readlines()
    archivo.close()
    
    lineas_invertidas: list[str] = []
    for pos in range(len(lineas)-1, -1, -1):
        lineas_invertidas.append(lineas[pos])

    archivo_destino: TextIO = open(nombre_salida, "w", encoding="utf-8")
    archivo_destino.truncate()
    
    for pos in range(0, len(lineas_invertidas), 1):
        linea_limpia = eliminar_salto_linea(lineas_invertidas[pos])
        archivo_destino.write(linea_limpia)
        if pos < len(lineas_invertidas) - 1:
            archivo_destino.write("\n")

    archivo_destino.close()

# ej 24
def agregar_frase_al_final(nombre_archivo: str, frase: str):
    leer_archivo: TextIO = open(nombre_archivo, "r", encoding="utf-8")
    contenido_archivo: str = leer_archivo.read()
    leer_archivo.close()

    escribir_archivo: TextIO = open(nombre_archivo, "a", encoding="utf-8")

    if len(contenido_archivo) > 0 and contenido_archivo[len(contenido_archivo)-1] != "\n":
        escribir_archivo.write("\n")
    
    escribir_archivo.write(frase)
    escribir_archivo.close()

# ej 25
def sacar_salto_linea(linea: str) -> str:
    tamaño: int = len(linea)
    if tamaño > 0 and linea[tamaño-1] == "\n":
        nueva_linea: str = ""
        for pos in range(0, tamaño - 1, 1):
            nueva_linea += linea[pos]
        return nueva_linea
    return linea

def agregar_frase_al_principio(nombre_archivo: str, frase):
    archivo: TextIO = open(nombre_archivo, "r", encoding="utf-8")
    lineas: list[str] = archivo.readlines()
    archivo.close()

    escribir_archivo: TextIO = open(nombre_archivo, "w", encoding="utf-8")
    escribir_archivo.write(frase + "\n")

    for pos in range(0, len(lineas), 1):
        linea_limpia: str = sacar_salto_linea(lineas[pos])
        escribir_archivo.write(linea_limpia)
        if pos < len(lineas)-1:
            escribir_archivo.write("\n")
    
    escribir_archivo.close()

# ej 26
def es_caracter_legible(caracter: str) -> bool:
    res: bool = True

    if caracter >= 'a' and caracter <= 'z':
        return res
    elif caracter >= 'A' and caracter <= 'Z':
        return res
    elif caracter >= '0' and caracter <= '9':
        return res
    elif caracter == ' ' or caracter == '_':
        return res
    else:
        res = False
        return res


def listar_textos_de_archivo(nombre_archivo: str) -> list[str]:
    """
    Lee un archivo (incluso binario) y extrae todas las secuciencias de texto legible que tengan 5 o más caracteres
    """
    archivo = open(nombre_archivo, "rb")
    contenido_binario: bytes = archivo.read
    archivo.close()

    textos_encontrados: list[str] = []

    texto_actual: str = ""

    for byte in contenido_binario:
        #covertir el byte (que es un int) em im caracter (str)
        caracter: str = chr(byte)
        if es_caracter_legible(caracter):
            texto_actual += caracter
        else:
            #encontramos un byte no deseado
            if len(texto_actual) > 5:
                textos_encontrados.append(texto_actual)
            texto_actual = ""
    
    if len(texto_actual) >= 5:
        textos_encontrados.append(texto_actual)
    
    return textos_encontrados

#ej 27
""" 
contenido nombre_archivo_notas: nro de LU (str), materia (str), fecha (str), nota (float)

cada elemento de notas_de_estudiantes con formate CSV: LU, materia, fecha y nota
"""
def tokenizar_linea_csv(linea: str) -> list[str]:
    tokens: list[str] = []
    token_actual: str = ""

    delimitadores: list[str] = [",", "\n"]

    for caracter in linea:
        if caracter not in delimitadores:
            token_actual += caracter
        else:
            tokens.append(token_actual)
            token_actual = ""
    if token_actual != "":
        tokens.append(token_actual)
    
    return tokens

def obtener_lu_unico(lineas: list[str]) -> list[str]:
    lus_unicos: list[str] = []
    for linea in lineas:
        datos: list[str] = tokenizar_linea_csv(linea)
        if len(datos) > 0:
            lu_actual: str = datos[0]
            if lu_actual not in lus_unicos:
                lus_unicos.append(lu_actual)
    
    return lus_unicos

def promedio_estudiante(notas_de_estudiantes: list[str], lu: str) -> int:
    suma_notas: float = 0.0
    cantidad_notas: int = 0

    for linea in notas_de_estudiantes:
        datos: list[str] = tokenizar_linea_csv(linea)

        if len(datos) == 4:
            lu_actual: str = datos[0]
            if lu_actual == lu:
                nota_str: str = datos[3]
                suma_notas += float(nota_str)
                cantidad_notas += 1
    
    return suma_notas / cantidad_notas

def calcular_promedio_por_estudiante(nombre_archivo_notas: str, nombre_archivo_promedios: str):
    archivo: TextIO = open(nombre_archivo_notas, "r", encoding="utf-8")
    lineas: list[str] = archivo.readlines()
    archivo.close()

    lista_lus: list[str] = obtener_lu_unico(lineas)

    archivo_promedios: TextIO = open(nombre_archivo_promedios, "w", encoding="utf-8")
    longitud_lista_lus: int = len(lista_lus)
    for i in range(0, longitud_lista_lus, 1):
        lu_actual: str = lista_lus[i]
        promedio: float = promedio_estudiante(lineas, lu_actual)

        promedio_a_escribir: str = lu_actual + ', ' + str(promedio)
        archivo_promedios.write(promedio_a_escribir)

        if i < longitud_lista_lus - 1:
            archivo_promedios.write("\n")

    archivo_promedios.close()

