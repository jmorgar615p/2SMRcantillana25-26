
# Es el bucle principal. Se repite hasta que el usuario elige una opción. 

while True:
    print("1. Mostrar datos de la mascota")
    print("2. Entrenar mascota")
    print("3. Salir")

# Ahora hago que pida una de las 3 opciones. 

    opcion=input("Selecciona una opción: ")

#  Aquí le decímos que salga este mensaje de error, debe introducir un número, en caso de que introduzca la palabra. Y también que salga si elige salir. 

    try:
        opcion=int(opcion)
    except ValueError:
        print("¡Debes introducir un número. Inténtalo de nuevo!")
        continue

# Y por último, definimos qué tiene que aparecer en pantalla según que opción elija el usuario.

    if opcion == 1:
        print("Mostrando datos de la mascota...")

    elif opcion== 2:
        print("Entrenando a la mascota...")

    elif opcion == 3:
        print("Saliendo del juego...")
        break

    else:
        print("Opción inválida. Por favor elige entre: 1, 2 o 3.")