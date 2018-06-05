

def menu_principal():
    print("\n")
    print("1. Acerca de...")
    print("2. Mantenimiento de Usuaraios...")
    print("3. Rankings")
    print("4. Empezar el cuso de Python")
    print("5. Ayuda")
    print()
    return int(input("Elija una opción (1-5): "))

def menu_usuarios():
    print("\n")
    print("1. Agregar un usuario")
    print("2. Reporte de usuarios")
    print("3. Cambiar de usuario")
    print("4. Eliminar un usuario")
    print()
    return int(input("Elija una opción (1-4): "))


#PROGRAMA


print("Bienvenidos al programa: Aprendiendo en Python")
print()
print("- - - - - - - - - - - - - - - - - - - - - - -")
print()
print("Escribe tu nombre a continuación para ingresar al programa:")

usuarioactual = input("Nombre: ")

usuario = {}
usuario.update({usuarioactual:[0,0]}) #El primer cero es donde se quedo y el tercero el PUNTAJE



#Ingresa al Menu Principal del Programa


print("\n"*20)
print(f"--- Bienvenido al menu {usuarioactual} ---" )


while True:
    sel = menu_principal()
    if sel in range(1,5):
        break
    print("El numero ingresado no es correcto.")




#Menu Principal - ACERCA DE...

if sel == 1:
    print("\n")
    print("Este trabajo....")




#Menu Principal - MANTENIMIENTO DE USUARIOS

elif sel == 2:
    print("\n")
    print("- - - - - - - - - - - - - - - - - - - - - - -")
    print("Mantenimiento de Usuarios")
    print("- - - - - - - - - - - - - - - - - - - - - - -")


    while True:
        sel = menu_usuarios()
        if sel in range(1,4):
            break
        print("El numero ingresado no es correcto.")





    if sel == 1: #Agregar un usuario
        print("\n")

        usuarioactual = input("Ingrese el nombre del nuevo usuario: ")
        usuario.update({usuarioactual:[0,0]})
        print("\n")




    elif sel == 2: #Reporte de usuarios
        print("\n")
        print("Reporte de usuarios:")
        print()
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




    elif sel == 3: #Cambiar de usuario
        print("\n")
        print("Selecciona el usuario a cambiar")
        cont2=0
        for i in usuario.items():
            print(f"1. {i[0]}")
            cont2=cont2+1
        sel = int(input(f"Elija una opción (1-{cont2}):"))

        nuevalista = []
        for i in usuario.keys():
            nuevalista.append(i)

        usuarioactual = nuevalista[sel-1]




    elif sel == 4: #Eliminar un usuario
        print("\n")



#Menu Principal - RANKINGS

elif sel == 3:
    print("\n")
    print("Rankings")


#Menu Principal - EMPEZAR EL CURZO DE PYTHON

elif sel == 4:
    print("\n")
    print("Curso PYTHON")

#Menu Principal - AYUDA

elif sel == 5:
    print("\n")
    print("Ayuda")
