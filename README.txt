EXPLICACIÓN DE HITO 2
Aquí explicaremos para que sirve cada línea
-----------------------------------------------------------------
while True:
Crea un bucle. Este se detendrá al poner break.
-----------------------------------------------------------------
print("1. Mostrar datos de la mascota")
print("2. Entrenar mascota")
print("3. Salir")

Son las diferentes opciones que tiene el usuario. 
-----------------------------------------------------------------
try:
    opcion = int(opcion)
except ValueError:
    print("¡Debes introducir un número. Inténtalo de nuevo!")
    continue

Comprueba la opción que ha elegido el usuario si es valida o no.
-----------------------------------------------------------------
if opcion == 1:
    print("Mostrando datos de la mascota...")
elif opcion == 2:
    print("Entrenando a la mascota...")
elif opcion == 3:
    print("Saliendo del juego...")
    break

Verifica la opción que ha elegido el usuario. Las dos primera muestra un mensaje cada uno y la tercera usa break para acabar el bucle.
-------------------------------------------------------------------------------------------------------------------------------------------
else:
    print("Opción inválida. Por favor elige entre: 1, 2 o 3.")

Si el usuario elige una opción distinta que no sea ninguna mostrada (1, 2 o 3) muestra que la opción no es valida que elijas una de esas opciones
-------------------------------------------------------------------------------------------------------------------------------------------
