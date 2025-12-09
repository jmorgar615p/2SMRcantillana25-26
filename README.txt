Aquí se explicará paso por paso el Hito 3 del Equipo 3
-------------------------------------------------------------------------------------------------------------------
import json
Importa el módulo estándar json, que proporciona funciones para convertir listas, dicts, etc en texto JSON.
-------------------------------------------------------------------------------------------------------------------
import os
Importa el módulo estándar os, Comprobar si existe un archivo, rutas, variables de entorno, etc.
-------------------------------------------------------------------------------------------------------------------
eventos = []
Crea una lista vacía llamada eventos. Se usa para almacenar mensajes de registro (logs).
-------------------------------------------------------------------------------------------------------------------
def log_evento(mensaje):
Define una función llamada log_evento que recibe un parámetro mensaje. Su uso es para registrar eventos.
-------------------------------------------------------------------------------------------------------------------
print(mensaje)
Dentro de log_evento: imprime el mensaje en la salida estándar
-------------------------------------------------------------------------------------------------------------------
eventos.append(mensaje)
Añade el mensaje a la lista eventos.
-------------------------------------------------------------------------------------------------------------------
def registrar_resultado_entrenamiento(trainer, mascota, resultado):
Define otra función llamada registrar_resultado_entrenamiento que recibe tres parámetros: trainer, mascota y resultado.
Su tarea es guardar esos datos en un archivo JSON.
-------------------------------------------------------------------------------------------------------------------
datos = {

Comienza la creación de un diccionario datos que agrupa la información que se va a guardar.
"trainer": trainer,
Añade al diccionario la clave "trainer" cuyo valor será el contenido del parámetro trainer

"mascota": mascota,
Añade la clave "mascota" con el valor del parámetro mascota

"resultado": resultado
Añade la clave "resultado" con el valor del parámetro resultado (por ejemplo, "aprobado", puntuación, etc.).

}
Cierra la definición del diccionario datos
-------------------------------------------------------------------------------------------------------------------
archivo = "resultados_entrenamientos.json"
Asigna a la variable local archivo el nombre del archivo donde se guardarán los datos
-------------------------------------------------------------------------------------------------------------------
try:
Inicia un bloque try/except para capturar cualquier excepción que ocurra durante la lectura/escritura del archivo.
-------------------------------------------------------------------------------------------------------------------
if os.path.exists(archivo):
Comprueba si el archivo indicado por archivo ya existe en el sistema de archivos.

with open(archivo, "r", encoding="utf-8") as f:
Si el archivo existe, lo abre en modo lectura ("r") usando un gestor de contexto with — esto asegura que el archivo se cierre automáticamente al salir del bloque. Se especifica encoding="utf-8" para manejar correctamente caracteres acentuados/Unicode.

registros = json.load(f)
Lee el contenido JSON del archivo y lo convierte en una lista de diccionarios. 
El resultado se asigna a la variable registros.
-------------------------------------------------------------------------------------------------------------------
except Exception as error:
Si ocurre cualquier excepción dentro del bloque try, se captura aquí como error.
-------------------------------------------------------------------------------------------------------------------
log_evento("Error al guardar el resultado:")
Registra un mensaje general indicando que hubo un error al guardar.
-------------------------------------------------------------------------------------------------------------------
log_evento(str(error))
Convierte la excepción error a cadena con str(error) y la registra (imprime y guarda) para que puedas ver el mensaje concreto del error



________________________________________________________________________________________________________________________________________________




main.py

from registro_entrenamientos import 
Importa desde el archivo llamado registro_entrenamientos.py (debe existir en la misma carpeta o ser accesible por Python):
-------------------------------------------------------------------------------------------------------------------
trainer = input("Elige tu entrenador:")
Muestra el mensaje "Elige tu entrenador:" y espera que el usuario escriba algo.
-------------------------------------------------------------------------------------------------------------------
mascota = input("Elige tu mascota:")
Muestra el mensaje "Elige tu mascota:" y espera que el usuario escriba algo.
-------------------------------------------------------------------------------------------------------------------
resultado = "Victoria en 3 rondas"
Guarda en la variable resultado el texto "Victoria en 3 rondas".

log_evento("Inicio del entrenamiento")
Llama a la función log_evento con el mensaje "Inicio del entrenamiento".
Esto hace dos cosas:
	Lo imprime en pantalla.

	Lo guarda en la lista eventos.
-------------------------------------------------------------------------------------------------------------------
log_evento("Ronda 1 completada")
Registra e imprime el mensaje de que la ronda 1 terminó.
-------------------------------------------------------------------------------------------------------------------
log_evento("Ronda 2 completada")
Registra e imprime el mensaje de que la ronda 2 terminó.
-------------------------------------------------------------------------------------------------------------------
log_evento("Ronda 3 completada")
Registra e imprime el mensaje de que la ronda 3 terminó.
-------------------------------------------------------------------------------------------------------------------
registrar_resultado_entrenamiento(trainer, mascota, resultado)
Guarda la información en el archivo JSON.
-------------------------------------------------------------------------------------------------------------------
log_evento("Entrenamiento finalizado")
Registra e imprime un último mensaje indicando que todo el proceso terminó.
