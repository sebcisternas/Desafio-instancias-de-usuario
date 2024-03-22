# Desafío - Instancias de usuario

#### Python 3.8

## Descripción

En este desafío, se solicita crear un script en Python que permita crear instancias de usuario a partir de los datos entregados en un archivo de texto llamado usuarios.txt, y almacenar cada instancia creada en una lista.

Cada línea del archivo usuarios.txt contiene un texto en estructura JSON, donde cada clave corresponde al nombre de un atributo de Usuario y su valor asociado corresponde al valor que debe tener en dicho atributo cada instancia de usuario creada.

El script también debe manejar las posibles excepciones al leer cada línea y/o generar cada instancia, y agregar la excepción en un archivo error.log. Se proporciona la definición de la clase Usuario en el archivo usuario.py, así como el archivo usuarios.txt que contiene los datos de los usuarios.

## Archivos Incluidos

- `script.py`: El script principal que lee el archivo `usuarios.txt`, crea instancias de Usuario y maneja excepciones.
- `usuario.py`: El archivo que contiene la definición de la clase Usuario.
- `usuarios.txt`: El archivo de texto que contiene los datos de los usuarios en formato JSON.
- `error.log`: El archivo de registro donde se registran las excepciones.

## Formato de los Datos

El archivo `usuarios.txt` proporciona los datos de los usuarios en el siguiente formato JSON:

```json
{"nombre": "Ejemplo", "apellido": "ApellidoEjemplo", "email": "ejemplo@dominio.com", "genero": "Masculino"}