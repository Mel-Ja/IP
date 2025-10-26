from queue import LifoQueue as Pila    
from queue import Queue as Cola
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


pila_resultado = generar_nros_al_azar(10, 5, 20)
print("10 numeros entre 5 y 20 ->", pila_resultado) # print no muestra el contenido, muestra objeto Pila

# Para verificar el contenido, desapilo:
print("Contenido de la pila (desapilando):")
while not pila_resultado.empty():
    print(pila_resultado.get())

print(pila_resultado.empty())




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


print("--------------------")

mi_pila = Pila()
mi_pila.put(1)
mi_pila.put(2)
mi_pila.put(3)
resultado = cantidad_elementos(mi_pila)
print(resultado)


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

mi_pila = Pila()
mi_pila.put(10)
mi_pila.put(5)
mi_pila.put(99)
mi_pila.put(420)
mi_pila.put(1)

print("--------------------")

max_obtenido = buscar_el_maximo(mi_pila)
print("max encontrado en mi_pila=[10,5,99,420,1]:", max_obtenido)


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


print("--------------------")

pila_alumnos: Pila[tuple[str, int]] = Pila()

pila_alumnos.put(("Juan", 4))   
pila_alumnos.put(("Pedro", 7))
pila_alumnos.put(("Ana", 10))
pila_alumnos.put(("Mica", 9))

tupla_ganadora = buscar_nota_max(pila_alumnos)
print(f"La tupla con la nota máxima es: {tupla_ganadora}")



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


print("--------------------")

print("1 + (2 x 3 = (20 / 5)) ->", esta_bien_balanceada("1 + (2 x 3 = (20 / 5))"))
print("1 + ) 2 x 3 ( () ->", esta_bien_balanceada("1 + ) 2 x 3 ( ()"))

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

print("--------------------")

expresion = "3 4 + 5 * 2 -"
print(f"Resultado de '{expresion}': {evaluar_expresion(expresion)}")

expresion_2 = "10 2 / 3 +"
print(f"Resultado de '{expresion_2}': {evaluar_expresion(expresion_2)}")


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


print("--------------------")
print("--------------------")

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


print("--------------------")

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


print("--------------------")

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

print("--------------------")

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

print("--------------------")

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