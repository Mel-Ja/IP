from math import sqrt, factorial, pi, ceil

# ej 1 Definir funciones y procedimientos
"""
(1) 
problema imprimir_hola_mundo () {
    requiere: { True }
    asegura: { imprime "Hola mundo!" por consola }
}
""" 
def imprimir_hola_mundo() -> None:
    print("¡Hola mundo!")

imprimir_hola_mundo()

"""
(2) imprimir_un_verso(): que imprima un versp de una canción que vos elijas, respetando los salgos de línea demiante el caracter \n
"""

def imprimir_un_verso():
    print("Cambia el clima con los años\nCambia el pastor su rebaño\nY así como todo cambia\nQue yo cambie no es extraño")

imprimir_un_verso()

"""
(3) raizde2(): que devuelva la raíz cuadrada de 2 con 4 decimales. ver función round

+ round(argument, ndigits) -> python en numeros finalizados en .5 los redondea al número par más cercano
"""
def raizde2() -> int:
    raiz_de_2: int = sqrt(2)
    rounded_raiz_2 = round(raiz_de_2, 2)
    return rounded_raiz_2

print(raizde2())

"""
(4) factorial_de_dos()
problema factorial_2() : Z {
    requiere: { True }
    asegura: { res = 2! }
}
"""
def factorial_de_dos() -> int:
    factorial_dos = factorial(2) 
    return factorial_dos

print(factorial_de_dos())

"""
(5) perimetro: que devuelva el perímetro de la circunferencia de radio 1. Utilizar la biblioteca math mediante el comando `import math` y la constante `math.pi`

problema perimetro () : R {
    requiere: { True }
    asegura: { res=2*pi }
}
"""
def perimetro() -> int:
    return 2*pi
print(perimetro())



# ej 2 Definir funciones y procedimientos con parámetros
"""
(1)

problema imprimir_saludo(in nombre: String) {
    requiere: { True }
    asegura: { imprime "Hola <nombre>" por pantalla }
}

"""
def imprimir_saludo(nombre: str) -> None:
    mensaje= f"Hola {nombre}"
    return print(mensaje)

imprimir_saludo("Mel")


"""
(2) raiz_cuadrada_de(numero): que devuelva la raíz cuadrada del número
"""
def raiz_cuadrada_de(numero: int) -> int:
    return int(sqrt(numero))

print("Raíz cuadrada de 25: ", raiz_cuadrada_de(25))

"""
(3) fahrenheit_a_celsius(temp_far): que convierta una temperatura en grados Fahrenheit a grados Celcius

problema fahrenheit_a_celsius(in t: R) : R {
    requiere: { True }
    asegura: { res= ( (t-32) * 5 )/9 }
}
"""
def fahrenheit_a_celsius (f: float) -> float:
    celsius: float = (f - 32) * 5/9
    return celsius

print("Fahrenheit a Celsius:", fahrenheit_a_celsius(50.0), "°C")


"""
(4) imprimmir_dos_veces(estribillo): que imprima dos veces el estribillo de una canción. Nota: Analizar el comportamiento del operador (*) con string
"""

def imprimir_dos_veces(estribillo: str) -> str:
    duplicar: str = estribillo*2
    print(duplicar)

imprimir_dos_veces("I love rock&roll <3 ")

"""
(5)
problema es_multiplo_de(in n: Z, in m: Z) : Bool {
    requiere: { m != 0 }
    asegura: { (res=true) <-> (existe un k∈Z tal que n=m*k) }
}
"""
def es_multiplo_de(n: int, m:int) -> bool:
    return n % m == 0

print("Es 20 múltiplo de 2?", es_multiplo_de(20,2))
print("Es 50 múltiplo de 3?", es_multiplo_de(50,3))

"""
(6) es_par(numero): que indique si numero es par (usar función es_multiplo_de())
"""
def es_par(numero: int) -> bool:
    return es_multiplo_de(numero, 2)

print("Es 40 par?", es_par(40))
print("Es 69 par?", es_par(69))

"""
(7) cantidad_de_pizzas(comensales, min_cant_de_porciones) que devuelva la cantidad de pizzas que necesitamos para que cada comensar coma como mínimo min_cant_de_porciones porciones ed pizza. COnsidere que cada pizza tiene 8 porciones y que se prefiere que sobren porciones

si tengo 5 comensales con 4 porciones mínimas por persona. Sé que cada pizza tiene 8 porciones y se prefiere que sobren porciones

5*4 = 20 -> porciones totales
20 / 8 -> cantidad de pizzas necesarias

"""

def cantidad_de_pizzas(comensales: int, min_cant_de_porciones: int) -> int:
    porciones_totales: int = comensales * min_cant_de_porciones 
    porciones_por_cada_pizza: int = 8
    pizzas_necesarias: int = ceil(porciones_totales / porciones_por_cada_pizza)
    return pizzas_necesarias

print("Somos 10 con 6 porciones mínimas por persona. Necesito ",cantidad_de_pizzas(10,6),"pizza(s)")
print("Somos 50 con 5 porciones mínimas por persona. Necesito ",cantidad_de_pizzas(50,5),"pizza(s)")
print("Somos 3 con 4 porciones mínimas por persona. Necesito ",cantidad_de_pizzas(3,4),"pizza(s)")

# ej 3 Resuelva los siguientes ejercicios utilizando los operados lógicos and, or, not. Resolverlos sin utilizar alternativa condicional (if)

"""
(1) alguno_es_0(numero1, numero2): dados dos números racionales, decide si alguno de los dos es igual a 0
"""
def alguno_es_0(num1: float, num2: float) -> bool:
    return num1 == 0 or num2 == 0

print("¿Alguno es cero?", alguno_es_0(20,0))
print("¿Alguno es cero?", alguno_es_0(20,30))

"""
(2) ambos_son_0(numero1, numero2): dados dos números racionales, decide si ambos son iguales a 0
"""
def ambos_son_0(num1: int, num2: int) -> bool:
    return num1 == 0 and num2 == 0

print("¿Ambos son cero?", ambos_son_0(20,0))
print("¿Ambos son cero?", ambos_son_0(0,0))

"""
(3) 
problema es_nombre_largo(in nombre: String) : Bool {
    requiere: { True }
    asegura: { (res=true) <-> ( 3 <= |nombre| <= 8 ) }
}
"""
def es_nombre_largo(nombre: str) -> bool:
    cant_caract_nombre: int = len(nombre)
    return  cant_caract_nombre >= 3 and cant_caract_nombre <= 8

print("¿Es el nombre 'Mel' largo?", es_nombre_largo("Mel"))
print("¿Es el nombre 'Fu' largo?", es_nombre_largo("Fu"))
print("¿Es el nombre 'Marcos' largo?", es_nombre_largo("Marcos"))

"""
(4) es_bisiesto(año): que indica si un año tiene 366 días. Recordar que un año es bisiesto si es múltiplo de 400, es múltiplo de 4 pero no de 100
"""

def es_bisiesto(año: int) -> bool:
    return (año % 4 == 0 and año % 100 != 0) or año % 400 == 0

print("¿es 2024 año bisiesto?", es_bisiesto(2024))
print("¿es 2008 año bisiesto?", es_bisiesto(2008))
print("¿es 1900 año bisiesto?", es_bisiesto(1900))



#ej 4
"""
Programar en Python usando composición de funciones (como en funcional). Resolver este ejercicio usando las funciones de python min y max:

    En una plantación de pinos, de cada árbol se conoce la altura expresada en metros. El peso de un pino se puede estimar a partir de la altura de la siguiente manera:
        - 3kg por cada centímetro hasta 3 metros
        - 2 kg por cada centrimetro arriba de los 3 metros
    
    Los pinos se usan para llevarlos a una fábrica de muebles, a la que le sirven árboles de entre 400 y 1000 kg, un pino fuera de ese rango no le sirve a la fábrica.
    Definir las siguientes funciones, deducir qué parámetros tendrán a partir del enunciado. Se pueden usar funciones auxiliares si fuese necesario para aumentar la legibilidad.

    (1) Definir la función peso_pino
    (2) Definir la función es_peso_util, recibe un peso en kg y responde si un pino de ese peso le sirve a la fábrica.
    (3) Definir la función sirve_pino, recibe la altura de un pino y responde si un pino de ese peso le sirve a la fábrica
    (4) Definir sirve_pino usando composición de funciones

    si la altura del pino es <= 300cm entonces lo multiplico por 3kg
    si la altura es mayor entonces ya se que por lo menos tiene 300cm siento 300*3 + (altura-300)*2

    sirve_pino(altura_pino) devuelve un bool, sirve_pino invoca es_peso_util(altura_pino) pasandole altura de un pino, es_peso_util
    sirve_pino(altura) -> peso_pino(altura) -> es_peso_util(peso_pino(altura))


"""

def calcular_peso_pino(altura_pino: int) -> int:
    altura_pino_cm: int = altura_pino * 100
    if altura_pino_cm <= 300:
        peso_pino = altura_pino_cm*3
        return peso_pino
    else:
        peso_pino = 300*3 + (altura_pino_cm-300) * 2
        return peso_pino

def peso_pino_condicionales(altura_pino_metro: int) -> int:
    peso_pino_kg = calcular_peso_pino(altura_pino_metro)
    return peso_pino_kg

def peso_pino(altura_pino_metro: int) -> int:
    altura_cm: int = altura_pino_metro*100
    return min(altura_cm, 300)*3 + max(0, altura_cm-300)*2

def es_peso_util(peso_kg: int) -> bool:
    return peso_kg > 400 and peso_kg < 1000

def sirve_pino(altura_pino: int) -> bool:
    peso = peso_pino(altura_pino)
    return es_peso_util(peso)

print("Sirve mi pino de 2mt?", sirve_pino(2))
print("Sirve mi pino de 5mt?", sirve_pino(5))


# ej 5 Implementar los siguientes problemas de alternativa condicional (if/else). Los enunciados pueden no ser del todo claros, especificar los problemas en nuestro lenguaje de especificación y programar en base a tu propuesta de especificación.

"""
(1) devolver_el_doble_si_es_par(numero); que devuelve el doble del número en caso de ser par y el mismo número en caso contrario

problema devolver_el_doble_si_es_par(in n: Z ) : Z {
    requiere: { True }
    asegura: { si n%2== 0 entonces res = n^2, si no res=n }
}
"""
def devolver_el_doble_si_es_par(numero: int) -> int:
    if numero % 2 == 0:
        return numero ** 2
    else:
        return numero

print("4 ->", devolver_el_doble_si_es_par(4))
print("11 ->", devolver_el_doble_si_es_par(11))
print("92 ->", devolver_el_doble_si_es_par(92))

"""
(2) devolver_valor_si_es_par_sino_el_que_sigue(numero); que devuelve el mismo número si es par y sino el siguiente, analizar distintas formas de implementación (usando un if-then-else, y 2 if, ¿todas funcionan?)

problema devolver_valor_si_es_par_sino_el_que_sigue(in n: Z) : Z {
    requiere: { True }
    asegura: { si n%2== 0 entonces res=n, si no res=n+1}
}


"""

def devolver_valor_si_es_par_sino_el_que_sigue(numero: int) -> int:
    if numero%2 == 0:
        return numero
    else:
        return numero+1

def devolver_valor_si_es_par_sino_el_que_sigue_2if(numero: int) -> int:
    if numero%2 == 0:
        return numero
    if numero%2 != 0:
        return numero+1
    
"""
(3) devolver_el_doble_si_es_multiplo3_el_triple_si_es_multiple9(numero). En otro caso devolver el número original. Analizar distintas formas de implementación (usando un if-then-else, y dos if, usando alguna opción de operación lógica) ¿todas funcionan? ¿cúal es el resultado si la entrada es 18?

problema devolver_el_doble_si_esmultipl3_el_triple_si_es_multiplo9(in n: Z) : Z {
    requiere: { True }
    asegura: { si n % 3 == 0 entonces res=n*2 }
    asegura: { o si n % 9 == 0 entonces res=n*3 }
    asegura: { si no entonces res=n}
}

"""
def devolver_doble_si_es_multiplo3_el_triple_si_es_multiplo9(numero: int) -> int:
    if numero % 9 == 0:
        return numero * 3
    elif numero % 3 == 0:
        return numero * 2
    else:
        return numero


def devolver_doble_si_es_multiplo3_el_triple_si_es_multiplo9_2if(numero: int) -> int:
    if numero % 9 == 0:
        return numero * 3
    if numero % 3 == 0:
        return numero * 2
    else:
         return numero

def devolver_doble_si_es_multiplo3_el_triple_si_es_multiplo9_logico(numero: int) -> int:
    return ( numero*3 if numero % 9 == 0 else numero*2 if numero %  3 == 0 else numero )


print("-"*20)

print("20 ->)", devolver_doble_si_es_multiplo3_el_triple_si_es_multiplo9(20))
print("30 ->)", devolver_doble_si_es_multiplo3_el_triple_si_es_multiplo9(30))
print("90 ->)", devolver_doble_si_es_multiplo3_el_triple_si_es_multiplo9(90))

print("-"*20)

print("20 ->)", devolver_doble_si_es_multiplo3_el_triple_si_es_multiplo9_2if(20))
print("30 ->)", devolver_doble_si_es_multiplo3_el_triple_si_es_multiplo9_2if(30))
print("90 ->)", devolver_doble_si_es_multiplo3_el_triple_si_es_multiplo9_2if(90))

print("-"*20)

print("20 ->)", devolver_doble_si_es_multiplo3_el_triple_si_es_multiplo9_logico(20))
print("30 ->)", devolver_doble_si_es_multiplo3_el_triple_si_es_multiplo9_logico(30))
print("90 ->)", devolver_doble_si_es_multiplo3_el_triple_si_es_multiplo9_logico(90))

print("-"*20)

"""
(4) lindo_nombre(nombre), que dado un nombre, si la longitud es igual o mayor a 5 devolver una frase que diga "Tu nombre tiene muchas letras!" y sino, "Tu nombre tiene menos de 5 caracteres"

problema lindo_nombre(in nombre : String) : String {
    requiere: {True}
    asegura: {si longitud de nombre > 5 entonces devolver "Tu nombre tiene muchas letras!"}
    asegura: {si no entonces devolver "Tu nombre tiene menos de 5 caracteres}
}

"""

def lindo_nombre(nombre: str) -> str:
    longitud_nombre: int = len(nombre)
    if longitud_nombre > 5:
        return "¡Tu nombre tiene muchas letras!"
    else:
        return "Tu nombre tiene menos de 5 caracteres "

print("Me llamo Fernando\n", lindo_nombre("Fernando"))
print("Me llamo Javier\n", lindo_nombre("Javier"))
print("Me llamo Cristiana\n", lindo_nombre("Cristiana"))
print("Me llamo Ian\n", lindo_nombre("Ian"))


"""
(5) elRango(numero), que imprime por pantalla "Menor a 5" si el número es menor a 5. "Entre 10 y 20" si el número está en ese rango y "Mayor a 20" si el número el mayor a 20

problema elRango(in numero: Z) : String {
    requiere: {True}
    asegura: {si n < 5 -> res = "Menor a 5"}
    asegura: {si 10 <= n <= 20 -> res = "Entre 10 y 20"}
    asegura: {si n > 20 -> res = "Mayor a 20"}
}
"""

def elRango(numero: int) -> str:
    if numero < 5:
        return "Menor a 5"
    elif 10 <= numero <= 20:
        return "Entre 10 y 20"
    elif numero > 20:
        return "Mayor a 20"

print("2 ->", elRango(2))
print("14 ->", elRango(14))
print("42 ->", elRango(42))


"""
(6) En Argentina una persona del sexo femenino se jubila a los 60 años, mientras que aquellas del sexo masculino se jubilan a los 65 años. Quienes son menores de 18 años deben ir de vacaciones junto al grupo que se jubila. Al resto de las personas se les ordena ir a trabajar. Implemente una funcion que, dados los parámentros de sexo (Fo M) y edad, imprima la grase que se corresponda según el caso: "Andá de vacaciones" o "Te toca trabajar"


problema es_jubilado_femenino(in edad: int) : Bool {
    requiere: { True }
    asegura: { si edad > 60 entonces res = true }
}

problema es_jubilado_masculino (in edad: int) : Bool {
    requiere: { True }
    asegura: { si edad > 65 entonces res = true}
}

problema es_jubilado(in sexo: String, in edad: int) : Bool {
    requiere: { True }
    asegura: { Si es_jubilado_femenino entonces res = true }
    asegura: { Si es_jubilado_masculino entonces res = true }
    asegura: { Si no res=false}
}

problema es_menor_18(in edad: Z) : Bool {
    requiere: { True }
    asegura: { si edad < 18 devuelve true, si no devuelve false }
}

problema accion_a_tomar(in sexo: String, in edad: Z) : String {
    requiere: { edad >= 0 }
    asegura: { Si edad < 18 -> res = "Andá de vacaciones" }
    asegura: { Si edad >= 60 y es sexo femenino -> res= "Andá de vacaciones" }
    asegura: { Si edad >= 65 y es sexo masculino -> res= "Andá de vacaciones" }
    asegura: { Si no res = "Te toca trabajar"}
}


"""
def es_jubilado_femenino(edad : int) -> bool:
    return edad > 60

def es_jubilado_masculino(edad : int) -> bool:
    return edad > 65

def es_jubilado(sexo: str, edad: int) -> bool:
    if sexo.lower() == "f":
        return es_jubilado_femenino(edad)
    elif sexo.lower() == "m":
        return es_jubilado_masculino(edad)

def es_menor_18(edad: int) -> bool:
    return edad < 18

def accion_a_tomar(sexo: str, edad: int) -> str:
    if es_menor_18(edad) or es_jubilado(sexo, edad):
        return "Andá de vacaciones"  
    else:
        return "Te toca trabajar"

print("-"*20)
print("Tengo 20 años->", accion_a_tomar("f", 20))
print("Tengo 70 años, mujer ->", accion_a_tomar("f", 70))
print("Tengo 30 años, hombre ->", accion_a_tomar("m", 30))
print("Tengo 83 años, hombre ->", accion_a_tomar("M", 83))
print("Tengo 10 años->", accion_a_tomar("F", 10))

print("-"*20)


# ej 6 Implementar las siguientes funciones usando repetición condicional while:
"""
(1) Escribir una función que imprima los números de 1 al 10
"""

def imprime_primeros_10_num():
    control: int = 1
    while control <= 10:
        print(control)
        control += 1

imprime_primeros_10_num()

print("-"*20)

"""
(2) Escribir una función que imprima los números pares entre el 10 y el 40
"""
def imprime_pares_entre_10_40():
    control: int = 10
    while control <= 40:
        if control % 2 == 0:
            print(control)
            control +=1
        else:
            control +=1

imprime_pares_entre_10_40()

print("-"*20)

"""
(3) Escribir una función que imprima la palabra "eco" 10 veces
"""
def eco_repetido():
    control: int = 0
    while control < 10:
        print("Eco")
        control += 1

eco_repetido()

print("-"*20)

"""
(4) Escribir una función de cuenta regresiva para lanzar un cohete. Dicha función irá imprimiendo desde el número que me pasan por parámetro (que será positivo) hasta el 1, y por último "Despegue"
"""

def cuenta_regresiva_cohete(num: int) -> str:
    while num >= 1:
        print(num)
        num -= 1

    print("¡Despegue!")

cuenta_regresiva_cohete(20)
cuenta_regresiva_cohete(10)

print("-"*20)


"""
(5) Hacer una función que monitoree un viaje en el tiempo. Diche función recibe dos parámetros, "el año de partida" y "algún año de llegada", siendo este último parámetro siempre más chico que el primero. EL viaje se realizará de a saltos de un año y la función debe mostrar el texto: "Viajó un año al pasado, estamos en el año: <año>" cada vez que se realice un salto de un año

si salgo en el 2025 y quiero llegar al 2020 e imprimo por pantalla cada vez que pasa un año desde 2025 hasta 2020

"""

def monitorear_viaje_en_el_tiempo(partida: int, llegada: int) -> None:
    print(f"Estamos en el año {partida} y vamos a ir viajar al {llegada}")
    while llegada < partida:
        partida -= 1
        print(f"Viajo un año al pasado, estamos en el año {partida}")

monitorear_viaje_en_el_tiempo(2025, 2020)

print("-"*20)


"""
(6) Implementar de nuevo la función de monitoreo de viaje en el tiempo, pero desde el año de partida hasta lo más cercano al 384 a.C, donde conoceremos a Aristóteles. Y para que sea más rápido el viaje, ¡vamos a viajar de a 20 años en cada salto!
"""

def viaje_tiempo_aristoteles(partida: int) -> None:
    while partida > -384:
        print(f"Estamos en el año {partida}")
        partida -= 20

    print("Llegamos al 384 a.C, ¡Allá voy Aristóteles!")

viaje_tiempo_aristoteles(1900)

print("-"*20)


# ej 7 Implementar las funciones del ejercicio 6 usando for num in range (i,f,p). Recordar que la función range para generar una secuencia de números en un rango dado, con el valor iniciar i, un valor final f y un paso p

# (1)
def imprimir_primeros_10_num_for():
    for numero in range(0, 10, 1):
        print(numero+1)
    
imprimir_primeros_10_num_for()

print("-"*20)

# (2)
def imprimir_pares_entre_10_40_for():
    for numero in range(10, 41, 2):
        if numero % 2 == 0:
            print(numero)

imprimir_pares_entre_10_40_for()

print("-"*20)

# (3)
def eco_repetido_for():
    for n in range (0, 10, 1):
        print("Eco...")

eco_repetido_for()

print("-"*20)

# (4)
def cuenta_regresiva_cohete_for(techo: int):
    for n in range(techo, 0, -1):
        print(n)
    print("¡Despegue!")


cuenta_regresiva_cohete_for(15)
cuenta_regresiva_cohete_for(5)

print("-"*20)

# (5)
def monitorear_viaje_tiempo_for(partida: int, llegada: int):
    print(f"Estamos en el {partida} y vamos a {llegada}")
    for año_partida in range(partida, llegada, -1):
        año_partida -=1
        print(f"Viajo un año al pasado, estamos en el año: {año_partida}")

monitorear_viaje_tiempo_for(2025, 2019)

print("-"*20)

# (6)
def viaje_tiempo_aristoteles(partida: int):
    for año in range(partida, -384, -20):
        print(f"Estamos en el año {año}, viajamos en el tiempo...")
    print("¡Llegamos!")

viaje_tiempo_aristoteles(900)

print("-"*20)

# ej 8 Realizar la ejecución simbólica de los siguientes códigos:
"""
(1) x=5 ; y=7 ; x = x + y

    *representación formal de la ejecución simbólica*
    x@a : indefinido
    x@b = 5
    x@c = x@b = 5
    y@c = 7
    x@d = x@c + y@c = 5+7 = 12
    y@d = y@c = 7


"""
    #Estado a: 
    #(no hay variables definidas todavía)
    
x=5
    #Estado b:
    #x@b = 5
    

y=7
    #Estado c:
    #y@c=7
    #x@c = x@b = 5

x = x + y
    #Estado d:
    #x@d = x@c + y@c = 5 + 7 = 12
    #y@d = y@c = 7


"""
(2) x=5 ; y=7 ; z=x-y ; y = z * 2

    *representación formal de la ejecución simbólica*
    x@a: indefinido
    x@b = 5
    x@c = x@b = 5
    y@c = 7
    z@d = x@c - y@c = 5 - 7 = -2
    x@d = 5
    y@d = 7
    y@e = z@d * 2 = (-2) * 2 = -4
    x@e = 5
    z@e = z@d = -2
"""
    #Estado a:
    # Sin variables definidas
x = 5
    #Estado b:
    #x@b = 5

y= 7
    #Estado c:
    #y@c = 7
    #x@c = x@b = 5

z = x-y
    #Estado d:
    #z@d = x@c - y@c = 5-7 = -2
    #x@d = x@c = 5
    #y@d = y@c = 7 

y = z*2
    #Estado e:
    #y@d = z@d * 2 = (-2)*2 = -4
    #x@e = x@d = 5
    #z@e = z@d = -2


"""
(3) x=5 ; y=7 ; x="hora" ; y = x*2

    *representación formal de la ejecución simbólica*
    x@a : indefinido
    x@b = 5
    x@c = x@b = 5
    y@c = 7
    x@d = "hora"
    y@d = y@c = 7
    y@e = x@d * 2 = "hora" * 2 = "horahora"
    x@e = x@d = "hora"

"""
    #Estado a:
    # Sin variables definidas
x = 5
    #Estado b:
    # x@b = 5

y = 7
    #Estado c:
    #y@c = 7
    #x@c = x@b = 5

x = "hora"
    #Estado d:
    #x@d = "hora"
    #y@d = y@c = 7

y = x*2
    #Estado e:
    #y@e = x@d * 2 = "hora" * 2 = "horahora"
    #x@e = x@d = "hora"

"""
(4) x=False ; res=not(x)

    *representación formal de la ejecución simbólica*
    x@a : indefinido
    x@b = False
    x@c = x@b = False
    res@c = not(x@b) = not(False) = True
"""
    #Estado a:
    # Sin variables definidas
x = False
    #Estado b:
    # x@b = False

res = not(x)
    #Estado c:
    #res@c = not(x@b) = not(False) = True
    #x@c = x@b = False

"""
(5) x=False ; x=not(x)

    *representación formal de la ejecución simbólica*
    x@a : indefinido
    x@b = False
    x@c = not(x@b) = not(False) = True
"""
    #Estado a:
    # Sin variables definidas
x = False
    #Estado b:
    #x@b = False

x = not(x)
    #Estado c:
    #x@c = not(x@b) = not(False) = True

"""
(6) x=True ; y=False ; res= x and y; x = res and x

    *representación formal de la ejecución simbólica*
    x@a : indeterminado
    x@b = True
    x@c = x@b = True
    y@c = False
    x@d = x@c = True
    y@d = y@c = False
    res@d = x@c and y@c = True and False = False
    x@e = res@d and x@d = False and True = False
    y@e = y@d = False
"""

    #Estado a:
    # Sin variables declaradas
x = True
    #Estado b:
    #x@b = True

y = False
    #Estado c:
    #y@c = False
    #x@c = x@b = True

res = x and y
    #Estado d:
    #res@d = x@c and y@c = True and False = False
    #x@d = x@c = True
    #y@d = y@c = False

x = res and x
    #Estado e:
    #x@e = res and x@d = False and True = False
    #res@e = res@d = False
    #y@e = y@d = False




# ej 9
"""
Sea el siguiente código:

def rt(x: int, g:int) -> int:
    g = g+1
    return x + g

g: int = 0
def ro(x: int) -> int:
    global g
    g = g+1
    return x + g

(1) ¿Cuál es el resultado de evaluar tres veces seguidas ro(1)?
(2) ¿Cuál es el resultado de evaluar tres veces seguidas rt(1,0)?
(3) En cada función, realizar la ejecución simbólica.
(4) Dar la especificación para cada función, rt y ro


"""

def rt(x: int, g: int) -> int:
    g = g + 1
    return x + g

g: int = 0

def ro(x: int) -> int:
    global g
    g = g+1
    return x+g

print("-"*20)
print("ro(1)", ro(1))
print("ro(1)", ro(1))
print("ro(1)", ro(1))
print("-"*20)
print("rt(1)", rt(1,0))
print("rt(1)", rt(1,0))
print("rt(1)", rt(1,0))
print("-"*20)