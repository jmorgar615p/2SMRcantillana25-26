# main.py
# Pruebas del Backend — Hito 2

from data_model import registrar_mascota, listar_mascotas

def main():
    print("=== PRUEBAS BACKEND EQUIPO 4 — HITO 2 ===")

    while True:
        print("\nMenú de pruebas:")
        print("1. Registrar mascota")
        print("2. Listar mascotas")
        print("3. Salir")

        opcion = input("Elige una opción: ")

        try:
            if opcion == "1":
                registrar_mascota()
            elif opcion == "2":
                listar_mascotas()
            elif opcion == "3":
                print(" Saliendo del programa...")
                break  # Sentencia de salto RA2.ce3
            else:
                print(" Opción inválida. Intenta de nuevo.")
        except Exception as e:
            print(" Error inesperado en el menú:", str(e))

if __name__ == "__main__":
    main()