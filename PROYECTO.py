print("Bienvenidos al programa: Aprendiendo en Python")
print()
print("- - - - - - - - - - - - - - - - - - - - - - -")
print()
print("Escribe tu nombre a continuación para ingresar al programa:")

usuarioactual = input("Nombre: ")

usuario = {}
usuario.update({usuarioactual:0})

#Ingresa al Menu del Programa
print("\n"*20)
print(f"--- Bienvenido al menu {usuarioactual} ---" )
print("\n")
print("1. Acerca de...")
print("2. Mantenimiento de Usuarios...")
print("3. Rankings")
print("4. Empezar el cuso de Python")
print("5. Ayuda")
print()
sel = input("Elija una opción (1-5): ")
