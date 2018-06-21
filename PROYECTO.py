import time

def menu_principal():
    print("\n"*20)
    print(f"--- Bienvenido al menu {usuarioactual} ---" )
    print()
    print("1. Acerca de...")
    print("2. Mantenimiento de Usuarios...")
    print("3. Rankings")
    print("4. Empezar el cuso de Python")
    print("5. Ayuda")
    print()
    return int(input("Elija una opción (1-5): "))

def menu_usuarios():
    print("1. Agregar un usuario")
    print("2. Reporte de usuarios")
    print("3. Cambiar de usuario")
    print("4. Eliminar un usuario")
    print("0. Atras")
    print()
    return int(input("Elija una opción (0-4): "))

def reporte_usuarios():
    bold = "\033[1m"
    reset = "\033[0;0m"

    print ("|       " + bold + "Nombre" + reset + "        |       " + bold + "Nivel" + reset + "       |     " + bold + "Puntaje" + reset + "     |")

    cont1=0
    for valor in usuario.items():
        for valor2 in valor[1]:
            nivel = valor2
            if cont1==1:
                puntaje = valor2
            cont1=cont1+1

        print("|",valor[0]," "*(18-len(valor[0])),"|",nivel," "*(16-len(str(nivel))),"|",puntaje," "*(14-len(str(puntaje))),"|",)
    return

def cursogen_python():
    print("1. Introducción y Variables")
    print("2. Estructuras de Control")
    print("3. Listas")
    print("4. Funciones")
    print("0. Atras")
    print()
    return int(input("Elija una opción (0-4): "))

def cintro_python():
    print("1. Introducción")
    print("2. Variables")
    print("3. Ejercicios")
    print("4. Información Adicional")
    print("0. Atras")
    print()
    return int(input("Elija una opción (0-4): "))

def cintro_ejer():
    print("1. Ejercicio 1")
    print("2. Ejercicio 2")
    print("3. Ejercicio 3")
    print("0. Atras")
    print()
    return int(input("Elija una opción (0-3): "))

def cestruc_python():
    print("1. Estructuras de Control Selectivas")
    print("2. Estructuras de Control Repetitivas")
    print("0. Atras")
    print()
    return int(input("Elija una opción (0-3): "))

def cestrucselec_python():
    print("1. Introducción")
    print("2. if, elif y else")
    print("3. Ejercicios")
    print("4. Información Adicional")
    print("0. Atras")
    print()
    return int(input("Elija una opción (0-4): "))

def cestrucselec_ejer():
    print("1. Ejercicio 1")
    print("2. Ejercicio 2")
    print("3. Ejercicio 3")
    print("0. Atras")
    print()
    return int(input("Elija una opción (0-3): "))

def cestrucrepet_python():
    print("1. Introducción")
    print("2. for y while")
    print("3. Ejercicios")
    print("4. Información Adicional")
    print("0. Atras")
    print()
    return int(input("Elija una opción (0-4): "))

def cestrucrepet_ejer():
    print("1. Ejercicio 1")
    print("2. Ejercicio 2")
    print("3. Ejercicio 3")
    print("0. Atras")
    print()
    return int(input("Elija una opción (0-3): "))

def clist_python():
    print("1. Introducción")
    print("2. Listas")
    print("3. Ejercicios")
    print("4. Información Adicional")
    print("0. Atras")
    print()
    return int(input("Elija una opción (0-4): "))

def clist_ejer():
    print("1. Ejercicio 1")
    print("2. Ejercicio 2")
    print("3. Ejercicio 3")
    print("0. Atras")
    print()
    return int(input("Elija una opción (0-3): "))

def cfunc_python():
    print("1. Introducción")
    print("2. funciones")
    print("3. Ejercicios")
    print("4. Información Adicional")
    print("0. Atras")
    print()
    return int(input("Elija una opción (0-4): "))

def cfunc_ejer():
    print("1. Ejercicio 1")
    print("2. Ejercicio 2")
    print("3. Ejercicio 3")
    print("0. Atras")
    print()
    return int(input("Elija una opción (0-3): "))

def P1cintro():
    while True:
        print('Si ves:')
        print('X=0')
        print('print(X*1)')
        print('¿Qué mostrará el programa?')
        print('')
        print("1. 0")
        print("2. 1")
        print("3. Habrá un error en el programa")
        Resp=int(input())
        if Resp == 1:
            print('')
            print('Respuesta correcta!')
            return
        elif Resp == 2 or Resp == 3:
            print('')
            print('Respuesta incorrecta')
            P1cintro()
        else:
            print('')
            print('Escriba una opción válida.')
            P1cintro()

def P2cintro():
    while True:
        print('Si ves:')
        print('X=25')
        print('print(x*2)')
        print('¿Qué mostrará el programa?')
        print('')
        print("1. 50")
        print("2. 27")
        print("3. Habrá un error en el programa")
        Resp=int(input())
        if Resp == 3:
            print('')
            print('Respuesta correcta!')
            return
        elif Resp == 2 or Resp == 1:
            print('')
            print('Respuesta incorrecta')
            P2cintro()
        else:
            print('')
            print('Escriba una opción válida.')
            P2cintro()

def P3cintro():
    while True:
        print('Si ves:')
        print('X=25')
        print('Y=2')
        print('X=Y')
        print('print(X)')
        print('¿Qué mostrará el programa?')
        print('')
        print("1. 25")
        print("2. 2")
        print("3. Habrá un error en el programa")
        Resp=int(input())
        if Resp == 2:
            print('')
            print('Respuesta correcta!')
            return
        elif Resp == 3 or Resp == 1:
            print('')
            print('Respuesta incorrecta')
            P3cintro()
        else:
            print('')
            print('Escriba una opción válida.')
            P3cintro()


#PROGRAMA

print()
print("Bienvenidos al programa: Aprendiendo en Python")
print()
print("- - - - - - - - - - - - - - - - - - - - - - -")
print()
print("Escribe tu nombre a continuación para ingresar al programa:")
print()
usuarioactual = input("Nombre: ")

usuario = {}
usuario.update({usuarioactual:[0,0]}) #El primer cero es donde se quedo y el tercero el PUNTAJE



#Ingresa al Menu Principal del Programa


print("\n"*20)


while True:

    #Menu Principal - ACERCA DE...

    while True:
        while True:
            sel = menu_principal()
            if sel in range(1,6):
                break
            print("El numero ingresado no es correcto.")

        if sel == 1:
            while True:
                print("\n"*20)
                print("Este trabajo está diseñado por alumnos de la UTEC cursando")
                print("el curso de Introducción a las Ciencias de la Computación")
                print("")
                print("El objetivo de este programa es enseñarles a las personas a")
                print("programar desde un nivel cero.")
                print("")
                time.sleep(2)
                print("Creado por:")
                print(" - Christian Ledgard")
                print(" - Lorena Gallo")
                print(" - Luis Alberto Garcia")
                print("\n")
                sel = input("Presione enter para regresar")
                break




        #Menu Principal - MANTENIMIENTO DE USUARIOS

        elif sel == 2:

            while True:

                print("\n")
                print("- - - - - - - - - - - - - - - - - - - - - - -")
                print("Mantenimiento de Usuarios")
                print("- - - - - - - - - - - - - - - - - - - - - - -")

                while True:
                    sel = menu_usuarios()
                    if sel in range(0,5):
                        break
                    print("El numero ingresado no es correcto.")

                if sel == 0:
                    break

                if sel == 1: #Agregar un usuario
                    print("\n")

                    usuarioactual = input("Ingrese el nombre del nuevo usuario: ")
                    usuario.update({usuarioactual:[0,0]})
                    print("\n")
                    print("--- El usuario se agrego correctamente ---")
                    time.sleep(1.5)
                    print()

                elif sel == 2: #Reporte de usuarios
                    print("\n")
                    print("Reporte de usuarios:")
                    print()
                    reporte_usuarios()
                    print()
                    sel = input("Presione enter para regresar")




                elif sel == 3: #Cambiar de usuario
                    print("\n")
                    print("Selecciona el usuario a cambiar")
                    cont2=0
                    cont3=1
                    for i in usuario.items():
                        print(f"{cont3}. {i[0]}")
                        cont2+=1
                        cont3+=1
                    sel = int(input(f"Elija una opción (1-{cont2}):"))

                    nuevalista = []
                    for i in usuario.keys():
                        nuevalista.append(i)

                    usuarioactual = nuevalista[sel-1]

                    print("\n")
                    print("--- El usuario se cambio correctamente ---")
                    time.sleep(1.5)
                    print()




                elif sel == 4: #Eliminar un usuario
                    print("\n")
                    print("Selecciona el usuario a ELIMINAR:")
                    print()
                    cont2=0
                    cont3=1
                    for i in usuario.items():
                        print(f"{cont3}. {i[0]}")
                        cont2+=1
                        cont3+=1
                    print()
                    sel = int(input(f"Elija una opción (1-{cont2}):"))

                    nuevalista2 = []
                    for i in usuario.keys():
                        nuevalista2.append(i)

                    delete=nuevalista2[sel-1]
                    del usuario[delete]

                    print("\n")
                    print("--- El usuario se elimino correctamente ---")
                    time.sleep(1.5)
                    print()



        #Menu Principal - RANKINGS

        elif sel == 3:

            while True:

                print("\n")
                print("- - - - - - - - - - - - - - - - - - - - - - -")
                print("               R A N K I N G ")
                print("- - - - - - - - - - - - - - - - - - - - - - -")
                print("\n")
                bold = "\033[1m"
                reset = "\033[0;0m"

                print ("           " + bold + "Nombre" + reset + "              " + bold + "Puntaje" + reset)

                cont1=0
                numeracion=0

                usuarioordenado = usuario

                for valor in usuario.items():
                    for valor2 in valor[1]:
                        nivel = valor2
                        if cont1==1:
                            puntaje = valor2
                        cont1+=1
                    numeracion+=1
                    print(numeracion,". |",valor[0]," "*(18-len(valor[0])),"|",puntaje," "*(14-len(str(puntaje))),"|",)
                print("\n")
                sel = input("Presione enter para regresar")
                break


        #Menu Principal - EMPEZAR EL CURZO DE PYTHON

        elif sel == 4:

            while True:

                print("\n")
                print("- - - - - - - - - - - - - - - - - - - - - - -")
                print("            C u r s o  P Y T H O N")
                print("- - - - - - - - - - - - - - - - - - - - - - -")
                print("\n")
                bold = "\033[1m"
                reset = "\033[0;0m"
                cursogen_python()
                print("\n")
                sel = input("Presione enter para regresar")

                while True:
                    sel = cursogen_python()
                    if sel in range(0,5):
                        break
                    print("El numero ingresado no es correcto.")

                if sel == 0:
                    break

                if sel == 1: #Introducción y Variables
                    print("\n")
                    print("- - - - - - - - - - - - - - - - - - - - - - -")
                    print("         I n t r o d u c c i ó n  y")
                    print("              V a r i a b l e s")
                    print("- - - - - - - - - - - - - - - - - - - - - - -")
                    print("\n")
                    bold = "\033[1m"
                    reset = "\033[0;0m"
                    cintro_python()
                    print("\n")
                    sel = input("Presione enter para regresar")

                    while True:
                        sel = cintro_python()
                        if sel in range(0,5):
                            break
                        print("El numero ingresado no es correcto.")
                        
                    if sel == 0:
                        break

                    elif sel == 1: #Introducción
                        print("\n")
                        print('La base de la computación son los algoritmos. Un algoritmo es un conjunto ordenado de operaciones sistemáticas.')
                        print('Puesto de manera más simple, un algoritmo es una serie de instrucciones sencillas que se llevan a cabo para solventar')
                        print('un problema.')
                        print('Características: Finito, definido y preciso.')
                        print('')
                        print('Python es un lenguaje utilizado para escribir algoritmos. Un lenguaje de programación.')
                        print('Algunas instrucciones comunmente usadas son las siguientes:')
                        print('print(): Imprime lo que esté dentro del parentesis. Si quieres escribir debe ir entre "".')
                        print('input(): Permite ingresar datos al usuario.')
                        print('También, los objetos tienen tipos. Un número entero es un int() y un número decimal, un float().')
                        print('Los textos son str().')
                        print('Suma: + | Resta: - | Multiplicación: * | División: /')
                        print("\n")

                    elif sel == 2: #Variables
                        print("\n")
                        print('Una variable está formada por un espacio en el sistema de almacenaje (memoria principal de un ordenador)')
                        print('y un nombre simbólico (un identificador) que está asociado a dicho espacio')
                        print('Las variables sirven para almacenar valores.')
                        print('En Python, una variable se define de la siguiente manera:')
                        print('X = "HOLA"')
                        print('Donde "X" es la variable y "HOLA" el valor que esta toma.')
                        print("\n")

                    elif sel == 3: #Ejercicios
                        print("\n")
                        print("- - - - - - - - - - - - - - - - - - - - - - -")
                        print("            E j e r c i c i o s")
                        print("- - - - - - - - - - - - - - - - - - - - - - -")
                        print("\n")
                        bold = "\033[1m"
                        reset = "\033[0;0m"
                        cintro_ejer()
                        print("\n")
                        sel = input("Presione enter para regresar")

                        while True:
                            sel = cintro_ejer()
                            if sel in range(0,4):
                                break
                            print("El numero ingresado no es correcto.")

                        if sel == 0:
                            break

                        elif sel == 1: #Ejercicio1
                            print("\n")
                            P1cintro()
                            print("\n")
                            break

                        elif sel == 2: #Ejercicio2
                            print("\n")
                            P2cintro()
                            print("\n")
                            break

                        elif sel == 3: #Ejercicio3
                            print("\n")
                            P3cintro()
                            print("\n")
                            break

                    elif sel == 4: #Información Adicional
                        print("\n")
                        
                elif sel == 2: #Estructuras de Control
                    print("\n")
                    print("- - - - - - - - - - - - - - - - - - - - - - -")
                    print("         E s t r u c t u r a s   d e")
                    print("                C o n t r o l")
                    print("- - - - - - - - - - - - - - - - - - - - - - -")
                    print("\n")
                    bold = "\033[1m"
                    reset = "\033[0;0m"
                    cintro_python()
                    print("\n")
                    sel = input("Presione enter para regresar")
                    
                    while True:
                        sel = cestruc_python()
                        if sel in range(0,3):
                            break
                        print("El numero ingresado no es correcto.")

                    if sel == 0:
                        break

                    elif sel == 1: #Estructuras de Control Selectivas
                        print("\n")
                        print("- - - - - - - - - - - - - - - - - - - - - - -")
                        print("         E s t r u c t u r a s   d e")
                        print("     C o n t r o l  S e l e c t i v a s")
                        print("- - - - - - - - - - - - - - - - - - - - - - -")
                        print("\n")
                        
                        while True:
                            sel = cestrucselec_python()
                            if sel in range(0,5):
                                break
                            print("El numero ingresado no es correcto.")

                        if sel == 0:
                            break

                        elif sel == 1: #Introducción
                            print("\n")
                        
                        elif sel == 2: #if, elif y else
                            print("\n")
                        
                        elif sel == 3: #Ejercicios
                            print("\n")
                            print("- - - - - - - - - - - - - - - - - - - - - - -")
                            print("            E j e r c i c i o s")
                            print("- - - - - - - - - - - - - - - - - - - - - - -")
                            print("\n")
                            bold = "\033[1m"
                            reset = "\033[0;0m"
                            cestrucselec_ejer()
                            print("\n")
                            sel = input("Presione enter para regresar")
    
                            while True:
                                sel = cestrucselec_ejer()
                                if sel in range(0,4):
                                    break
                                print("El numero ingresado no es correcto.")
    
                            if sel == 0:
                                break
    
                            elif sel == 1: #Ejercicio1
                                print("\n")
    
                            elif sel == 2: #Ejercicio2
                                print("\n")
    
                            elif sel == 3: #Ejercicio3
                                print("\n")
                            
                        elif sel == 4: #Información Adicional
                            print("\n")

                    elif sel == 2: #Estructuras de Control Repetitivas
                        print("\n")
                        print("\n")
                        print("- - - - - - - - - - - - - - - - - - - - - - -")
                        print("         E s t r u c t u r a s   d e")
                        print("     C o n t r o l  R e p e t i t i v a s")
                        print("- - - - - - - - - - - - - - - - - - - - - - -")
                        print("\n")

                        while True:
                            sel = cestrucrepet_python()
                            if sel in range(0,5):
                                break
                            print("El numero ingresado no es correcto.")

                        if sel == 0:
                            break

                        elif sel == 1: #Introducción
                            print("\n")
                        
                        elif sel == 2: #for y while
                            print("\n")
                        
                        elif sel == 3: #Ejercicios
                            print("\n")
                            print("- - - - - - - - - - - - - - - - - - - - - - -")
                            print("            E j e r c i c i o s")
                            print("- - - - - - - - - - - - - - - - - - - - - - -")
                            print("\n")
                            bold = "\033[1m"
                            reset = "\033[0;0m"
                            cestrucrepet_ejer()
                            print("\n")
                            sel = input("Presione enter para regresar")

                            while True:
                                sel = cestrucrepet_ejer()
                                if sel in range(0,4):
                                    break
                                print("El numero ingresado no es correcto.")

                            if sel == 0:
                                break

                            elif sel == 1: #Ejercicio1
                                print("\n")

                            elif sel == 2: #Ejercicio2
                                print("\n")

                            elif sel == 3: #Ejercicio3
                                print("\n")
                            
                        elif sel == 4: #Información Adicional
                            print("\n")

                elif sel == 3: #Listas
                    print("\n")
                    print("- - - - - - - - - - - - - - - - - - - - - - -")
                    print("                L i s t a s")
                    print("- - - - - - - - - - - - - - - - - - - - - - -")
                    print("\n")
                    bold = "\033[1m"
                    reset = "\033[0;0m"
                    clist_python()
                    print("\n")
                    sel = input("Presione enter para regresar")

                    while True:
                        sel = clist_python()
                        if sel in range(0,5):
                            break
                        print("El numero ingresado no es correcto.")

                    if sel == 0:
                        break

                    elif sel == 1: #Introducción
                        print("\n")

                    elif sel == 2: #Listas
                        print("\n")

                    elif sel == 3: #Ejercicios
                        print("\n")
                        print("- - - - - - - - - - - - - - - - - - - - - - -")
                        print("            E j e r c i c i o s")
                        print("- - - - - - - - - - - - - - - - - - - - - - -")
                        print("\n")
                        bold = "\033[1m"
                        reset = "\033[0;0m"
                        clist_ejer()
                        print("\n")
                        sel = input("Presione enter para regresar")

                        while True:
                            sel = clist_ejer()
                            if sel in range(0,4):
                                break
                            print("El numero ingresado no es correcto.")

                        if sel == 0:
                            break

                        elif sel == 1: #Ejercicio1
                            break

                        elif sel == 2: #Ejercicio2
                            break

                        elif sel == 3: #Ejercicio3
                            break

                    elif sel == 4: #Información Adicional
                        print("\n")

                elif sel == 4: #Funciones
                    print("\n")
                    print("- - - - - - - - - - - - - - - - - - - - - - -")
                    print("             F u n c i o n e s")
                    print("- - - - - - - - - - - - - - - - - - - - - - -")
                    print("\n")
                    bold = "\033[1m"
                    reset = "\033[0;0m"
                    cfunc_python()
                    print("\n")
                    sel = input("Presione enter para regresar")

                    while True:
                        sel = cfunc_python()
                        if sel in range(0,5):
                            break
                        print("El numero ingresado no es correcto.")

                    if sel == 0:
                        break

                    elif sel == 1: #Introducción
                        print("\n")

                    elif sel == 2: #Funciones
                        print("\n")

                    elif sel == 3: #Ejercicios
                        print("\n")
                        print("- - - - - - - - - - - - - - - - - - - - - - -")
                        print("            E j e r c i c i o s")
                        print("- - - - - - - - - - - - - - - - - - - - - - -")
                        print("\n")
                        bold = "\033[1m"
                        reset = "\033[0;0m"
                        cfunc_ejer()
                        print("\n")
                        sel = input("Presione enter para regresar")

                        while True:
                            sel = cintro_ejer()
                            if sel in range(0,4):
                                break
                            print("El numero ingresado no es correcto.")

                        if sel == 0:
                            break

                        elif sel == 1: #Ejercicio1
                            print("\n")

                        elif sel == 2: #Ejercicio2
                            print("\n")

                        elif sel == 3: #Ejercicio3
                            print("\n")

                    elif sel == 4: #Información Adicional
                        print("\n")
                        
            break


        #Menu Principal - AYUDA

        elif sel == 5:
            while True:
                print("\n"*20)
                print("Este es un programa super sencillo.")
                print("Usted no va a necesitar usar su mouse,")
                print("solo las teclas de su computador.")
                print("\n")
                sel = input("Presione enter para regresar")
                break

