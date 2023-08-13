import random

print(" ")
print("BIENVENIDO AL JUEGO DE PIEDRA PAPEL O TIJERAS")
print(" ")

def elegir_opcion():
    opciones = ('piedra', 'papel', 'tijeras')
    opcion_usu = input("¿Piedra, Papel o Tijeras?-> ")
    opcion_usu = opcion_usu.lower()

    if opcion_usu == 'tijera':
        opcion_usu = 'tijeras'
    
    if opcion_usu not in opciones:
        print('     ')
        print("Esa opción no es válida")
        print("Por favor intenta de nuevo.")
        print('     ')
        print('     ')
        return None,None

    opcion_pc = random.choice(opciones)
    
    print('     ')
    print("Opción del Usuario-> ", opcion_usu)
    print("Opción del Computador-> ", opcion_pc)
    return opcion_usu, opcion_pc

def reglas(opcion_usu, opcion_pc, victoria_usu, victoria_pc):
    if opcion_usu is None:
        return victoria_usu, victoria_pc

    if opcion_usu == opcion_pc:
        print("Empate!!")
        
    elif opcion_usu == "piedra" :
        if opcion_pc == 'tijeras' :
            print("Piedra gana a Tijeras")
            print("¡Ganaste! :D")
            victoria_usu += 1
        else:
            print("Papel gana a Piedra")
            print("¡Perdiste! D:")
            victoria_pc += 1
            
    elif opcion_usu == "papel" :
        if opcion_pc == 'piedra' :
            print("Papel gana a Piedra")
            print("¡Ganaste! :D")
            victoria_usu += 1
        else:
            print("Tijeras gana a Papel")
            print("¡Perdiste! D:")
            victoria_pc += 1
            
    elif opcion_usu == "tijeras" :  
        if opcion_pc == 'papel' :
            print("Tijeras gana a Papel")
            print("¡Ganaste! :D")
            victoria_usu += 1
        else:
            print("Piedra gana a Tijeras")
            print("¡Perdiste! D:")
            victoria_pc += 1

    print('     ')
    print('     ')
    return victoria_usu, victoria_pc
        

def cheq_ganador(victoria_usu, victoria_pc):

        if victoria_pc == 2:
            print("*" * 47)
            print("Victorias del Computador-> ",victoria_pc)
            print("¡El ganador de todo el juego es la Computadora!")
            print("*" * 47)
            exit()
            
        if victoria_usu == 2:
            print("*" * 43)
            print("Victorias del Usuario-> ",victoria_usu)
            print("¡El ganador de todo el juego es el Usuario!")
            print("*" * 43)
            exit()


def run_game():
    victoria_usu = 0
    victoria_pc = 0
    
    rondas = 1

    while True:
        print('*' * 10)
        print(' RONDA', rondas)
        print('*' * 10)
        print('     ')
        print("Victorias del Usuario-> ",victoria_usu)
        print("Victorias del Computador-> ",victoria_pc)
        print(" ")

        rondas += 1

        opcion_usu, opcion_pc = elegir_opcion()
        victoria_usu, victoria_pc = reglas(opcion_usu, opcion_pc, victoria_usu, victoria_pc)
        cheq_ganador(victoria_usu, victoria_pc)

run_game() 