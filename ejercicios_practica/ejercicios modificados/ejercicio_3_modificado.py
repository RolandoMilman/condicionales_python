# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese primero su nombre y luego su apellido
# Capture ambos datos e imprima su nombre completo
print('Ingrese por consola su nombre/s:')
nombre = str(input())

print('Ingrese por consola su apellido/s:')
apellido = str(input())

# Imprima su nombre completo (Nombre y Apellido)
print('Nombre y apellido', nombre.capitalize(), apellido.capitalize())
# Imprima su nombre completo (Apellido y Nombre)
print('Apellido y nombre', apellido.capitalize(), nombre.capitalize())
# Almacenar su nombre completo en una variable
# nombre_completo = .....
nombre_completo_1 = nombre.capitalize() + ' ' + apellido.capitalize()

nombre_completo_2= apellido.capitalize() + ' ' + nombre.capitalize()

# Imprima su nombre completo (Nombre y Apellido)
print('Nombre y apellido', nombre_completo_1)
# Imprima su nombre completo (Apellido y Nombre)
print('Apellido y nombre', nombre_completo_2)


# Imprimir la cantidad de letras que posee su nombre completo
# cantidad_letras = len(....)
print('Cantidad de caracteres del NOmbre y Apellido', len(nombre_completo_1))
print('Cantidad de caracteres del Apellido y nombre', len(nombre_completo_2))