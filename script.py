import json
from usuario import Usuario

# lista para almacenar las instancias de Usuario
usuarios = []

# archivo para registrar las excepciones
error_log = open("error.log", "a")

# abrir el archivo usuarios.txt
with open('usuarios.txt', 'r') as archivo:
    # leer cada línea del archivo
    linea = archivo.readline()
    while linea:
        try:
            # convertir la línea en un diccionario
            usuario_dict = json.loads(linea)
            # crear una instancia de Usuario y añadirla a la lista de usuarios
            usuario = Usuario(usuario_dict['nombre'], usuario_dict['apellido'], usuario_dict['email'], usuario_dict['genero'])
            usuarios.append(usuario)
        except json.JSONDecodeError as e:
            # escribir la excepción en el archivo error.log
            error_log.write(f"Error de decodificación JSON en la línea: {linea}\n")
            error_log.write(f"Mensaje de error: {str(e)}\n\n")
        except KeyError as e:
            # escribir la excepción en el archivo error.log
            error_log.write(f"Error de clave faltante en la línea: {linea}\n")
            error_log.write(f"Mensaje de error: {str(e)}\n\n")
        except Exception as e:
            # manejar otras excepciones genéricas y escribirlas en el archivo error.log
            error_log.write(f"Error inesperado en la línea: {linea}\n")
            error_log.write(f"Mensaje de error: {str(e)}\n\n")
        finally:
            # leer la siguiente línea
            linea = archivo.readline()

# cerrar el archivo de registro de errores
error_log.close()

#verificar los usuarios creados
for usuario in usuarios:
    print(f"Nombre: {usuario.nombre}, Apellido: {usuario.apellidos}, Email: {usuario.email}, Género: {usuario.genero}")