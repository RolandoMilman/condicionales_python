# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Comparadores
# Ingrese dos palabras cualesquiera y realice las sigueintes
# comparaciones entre ellas
import unidecode
texto_1 = str(input('Ingrese la primera palabra:\n').lower())

texto_2 = str(input('Ingrese la segunda palabra:\n').lower())

# Compare cual de las dos palabras es mayor (alfabéticamente)
# Imprima en pantalla según corresponda

# Compare cual de las dos palabras tiene mayor
# cantidad de letras
# Imprima en pantalla según corresponda

# Verifique si la primera letra de la primera palabra
# es mayor a la primera letra de la segunda palabra
# Imprima en pantalla según corresponda

# copia_texto_1 = texto_1  # Copia de la variable texto_1

# Verifique que copia_texto_1 es igual a texto_1
# Imprima en pantalla según corresponda

# Verifique que copia_texto_1 es distinta a texto_2
# Imprima en pantalla según corresponda

# Verificar que texto es mayor alfabéticamente

if unidecode.unidecode(texto_1) > unidecode.unidecode(texto_2):
    print('{} es mayor que {}'.format(texto_1, texto_2))
else:
    print('{} es mayor que {}'.format(texto_2, texto_1))


# Verificar que cadena de texto es más larga en caracteres (longitud)
if len(texto_1) > len(texto_2):
    print('{} es más larga que {}'.format(texto_1, texto_2))
else:
    print('{} es más larga que {}'.format(texto_2, texto_1))

# Verificar que la primera letra de la primera palabra es mayor a la primera letra de la segunda palabra
if texto_1[0:1] > texto_2[0:1]:
    
    print('La primera letra de la palabra {} es mayor que de la palabra {}'.format(texto_1, texto_1[0:1], texto_2, texto_2[0:1]))

elif texto_2[0:1] > texto_1[0:1]:
    print('La primera letra de la palabra {} {} es mayor que de la palabra {} {}'.format(texto_2, texto_2[0:1], texto_1, texto_1[0:1]))

elif texto_2[0:1] == texto_1[0:1]:
    print('La primera letra de la palabra {} {} es igual que de la palabra {} {}'.format(texto_2, texto_2[0:1], texto_1, texto_1[0:1]))

