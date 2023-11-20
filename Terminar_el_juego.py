import menu

# This function gives us the initial message
def mensaje_inicio():
    print()
    print("Vamos a comenzar a jugar a un juego en el que tendrás que adivinar el número en el que estoy pensando") 
    print()

# This function asks the user his/her name
def pedir_nombre():
    while True:
        nom = input("Lo primero de todo necesito que me digas tu nombre: ")
        try:
            nom = str(nom)
            break
        except:
            print("Dime tu nombre de verdad")
    return nom
        
# This function prints the list of scores 
def imprimir_puntuaciones(puntuaciones):
    print()
    print("La lista de ganadores es:")
    for i in puntuaciones:
        print("1º.  {} ---> {} ".format(i, puntuaciones[i]))
        
# This function represents the whole game.
def jugar():
    mensaje_inicio()
    nom = pedir_nombre()
    intentos_usados = menu.empezar()
    puntuaciones = {nom: intentos_usados}
    imprimir_puntuaciones(puntuaciones)
    
jugar()



    

    
    
    
