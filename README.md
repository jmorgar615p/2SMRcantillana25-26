# Hito 2 — Backend / API
**Equipo 4**

Este proyecto es la parte de Backend del Hito 2, donde se gestiona la lógica de mascotas del juego. Permite registrar y listar mascotas, usando condicionales, bucles y manejo básico de errores.

## **Archivos**

- `data_model.py` → Contiene las funciones principales:
  - `registrar_mascota()`: Permite añadir una nueva mascota al sistema.  
    - Verifica que el nombre no esté vacío.  
    - Evita duplicados (si ya existe una mascota con ese nombre, no se registra).  
    - Maneja errores inesperados con `try/except`.
  - `listar_mascotas()`: Muestra todas las mascotas registradas.  
    - Usa un bucle `for` para recorrer el diccionario de mascotas.  
    - Maneja errores si se intenta acceder a claves inexistentes o si ocurre algún fallo inesperado.

- `main.py` → Archivo de pruebas.  
  - Muestra un menú interactivo para:
    1. Registrar mascota  
    2. Listar mascotas  
    3. Salir  
  - Incluye validación de opciones incorrectas y manejo de errores generales.  
  - Usa `break` para salir del bucle del menú.

## **Manejo de errores**

- **Nombres vacíos o duplicados** → mensaje de advertencia, no se registra la mascota.  
- **Errores inesperados** → se captura cualquier excepción con `try/except` y se muestra un mensaje amigable.  
- **Opciones inválidas en el menú** → el programa pide al usuario que intente de nuevo sin bloquearse.

## **Cómo ejecutar**

1. Abrir la terminal en la carpeta del proyecto (`Hito2_Equipo4`).  
2. Ejecutar:

```bash
python main.py
