import random

# Constants
MIN = 1
MAX1 = 100
MAX2 = 1000
MAX3 = 1000000
MAX4 = 1000000000000

# This function asks user the level/difficulty
def pedir_nivel():
    while True:
        nivel = input("¿Quieres jugar en nivel fácil (1), medio (2), difícil (3), o extremo (4)?: ")
        try:
            nivel = int(nivel)
            if 1 <= nivel <= 4:
                break
            else:
                print("Ese número no es válido")
        except ValueError:
            print("No has introducido un valor válido, te vuelvo a preguntar.")
    return nivel
"""
Variables LOCALES:
    nivel

return:
    El valor de nivel {1, 2, 3, 4}
"""


# This function asks user the number of tries 
def num_intentos():
    while True:
        intentos = input("¿Cuántos intentos quieres tener?: ")
        try:
            intentos = int(intentos)
            if intentos > 0:
                break
            else:
                print("Ese número no es válido")
        except ValueError:
            print("No has introducido un valor válido, te vuelvo a preguntar.")
    return intentos

"""
Variables LOCALES:
    intentos

return:
    El número de intentos máximo que tiene el usuario para adivinar el número {1, 2, 3, ...}
"""

# This function asks user whether he wants help or not
def pedir_ayuda():
    while True:
        ayuda = input("¿Quieres tener una ayuda opcional que te reduzca los rangos a la hora de acertar el número? Sí (s) / No (n): ")
        ayuda = ayuda.lower()
        try:
            ayuda = str(ayuda)
            if ayuda == "s" or ayuda == "n":
                break
            else:
                print("Debes responder con (s) si quieres ayuda o con (n) si no la quieres.")
        except ValueError:
            print("No has introducido texto")
    return ayuda

"""
Variables LOCALES:
    ayuda

return:
    Devuelve el valor de ayuda {s, n}. "s" significará que sí querrá la ayuda y "n" que no.
"""

# This function sets the upper bound of the ragne using the value of the level asked before
def definir_rango(nivel):
    if nivel == 1:
        return MAX1
    elif nivel == 2:
        return MAX2
    elif nivel == 3:
        return MAX3
    elif nivel == 4:
        return MAX4
    
"""
Parámetro:
    nivel

Variables globales:
    MAX1 = 100; MAX2 = 1000; MAX3 = 1000000; MAX4 = 1000000000000

return:
    En función del nivel que hayas señalado, la función devolverá una variable global distinta {MAX1, MAX2, MAX3, MAX4}, 
    cada una de estas variables asociada al límite superior del rango en función del nivel de dificiultad.
"""

# This function is used if you said you wanted to be helped and it gives you help by telling you if the number you have to guess is in the first half of the range or in the second
def actualizar_rango(al, i, ayuda, MIN, MAX):
    if ayuda == "s":
        if al <= (MAX//2):
            if i == 1:
                print("A partir de ahora ten en cuenta que el rango está entre {} y {}".format(MIN, MAX//2))
            if i > 1:
                print("Te recuerdo que tu rango estaba entre {} y {}".format(MIN, MAX//2))
        elif al > (MAX//2):
            if i == 1:
                print("A partir de ahora ten en cuenta que el rango está entre {} y {}".format(MAX//2, MAX))
            if i > 1:
                print("Te recuerdo que tu rango estaba entre {} y {}".format(MAX//2, MAX))
                
"""
Parámetros:
    al = número aleatorio que genera el juego que tienes que tratar de adivinar
    i = variable que nos sirve para saber si es el primer intento o no y dar un mensaje distinto en función de ello
    ayuda = nos dice si se ha solicitado la ayuda o no
    MIN, MAX = sirven para dar el valor del nuevo rango
    
Esta función se implementa en la función de empezar juego que es en la que se empieza el juego
"""

# With this function we define and start the game
def empezar_juego(MIN, MAX, al, intentos, ayuda):
    print("De acuerdo, vamos a comenzar el juego !!")
    print()
    i = 1
    while i <= intentos:
        try:
            num = int(input("Dime un número del {} al {}: ".format(MIN, MAX)))
            if MIN <= num <= MAX:
                if num == al:
                    print("Enhorabuena, has acertado el numero en {} intentos. Te quedaban {} intentos".format(i, intentos - i))
                    break
                else:
                    if ayuda == "s":
                        if num < al:
                            print("Te has quedado por debajo. Te quedan: {} intentos.".format(intentos - i))
                        elif num > al:
                            print("Te has pasado. Te quedan: {} intentos".format(intentos - i))
                        actualizar_rango(al, i, ayuda, MIN, MAX)
                        print()
                        i = i + 1
                        
                    elif ayuda == "n":
                        if num < al:
                            print("Te has quedado por debajo. Te quedan: {} intentos".format(intentos - i))
                        elif num > al:
                            print("Te has pasado. Te quedan: {} intentos".format(intentos - i))
                        print()
                        i += 1
            else:
                print("Ese número no es válido")
        except ValueError:
            print("Introduce un número entre el {} y el {}: ".format(MIN, MAX))
    return i
            
"""
Parámetros:
    MIN, MAX = Son los parámetros que nos definen el rango que tenemos para adivinar
    al = es el número aleatorio que tiene que adivinar el usuario
    intentos = es el número de intentos que el usuario ha dicho que quiere tener como máximo
    ayuda = en función de si el usuario ha solicitado la ayuda o no se dará un rango menor o no
    
En la función al principio te pide que ingreses un número, mientras el número sea válido, comprobará si está por encima, por debajo
o si es igual al número que había que adivinar. Además, en caso de que no aciertes, y hayas solicitado la ayuda, 
el rango se te reducirá.
"""

# Main part of the program
def empezar():
    nivel = pedir_nivel()
    intentos = num_intentos()
    ayuda = pedir_ayuda()
    MAX = definir_rango(nivel)
    al = random.randint(MIN, MAX)
    intentos_utilizados = empezar_juego(MIN, MAX, al, intentos, ayuda)
    return intentos_utilizados

"""
Esta función agrupa todas las funciones anteriores para llamarlas a la vez y que no se pueda olvidar llamar a alguna    
"""

if __name__ == "__main__":
    empezar()
    
"""
Con esto hacemos que al importar este archivo al otro no se ejecute directamente la función "empezar()", sino que habrá que llamarla
"""