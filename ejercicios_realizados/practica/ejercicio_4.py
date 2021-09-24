# Condicionales [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# texto_1 = '5'
# texto_2 = '7'
texto_1 = str(input('Ingrese el valor de texto_1:'))
print('Tipo de variable de texto_1, de valor {}, es {}' .format(texto_1, type(texto_1)))
texto_2 = str(input('Ingrese el valor de texto_2:'))
print('Tipo de variable de texto_2, de valor {} es {}' .format(texto_2,  type(texto_2)))
print('')
# 1-Verifique cual de los dos textos es mayor alfabéticamente
# La comparación alfabética es aquella que se logra cuando
# se utiliza el operador mayor o menor con Strings (textos)
# Imprima en pantalla según corresponda
print('Comparación de números como texto')
if texto_1 > texto_2:
    mayor = texto_1

    print('El valor más grande entre {} y {} es {}'.format(texto_1, texto_2, mayor))

elif texto_2 > texto_1:
    mayor = texto_2

    print('El valor más grande entre {} y {} es {}'.format(texto_1, texto_2, mayor))

elif texto_2 == texto_1:
    
    print('Los valores ingresados son iguales')    

# 2-Transforma esas variables tipo texto en variables numéricas con (int)
# y almacénalas en nuevas variables.
# Compare las nuevas variables para ver cual es mayor o menor
# utilizando los operadores correspondientes
# ¿Cuál de las nuevas variables es mayor?
# Imprima en pantalla según corresponda
print('')
print('Conversión a números enteros')
print('')
numero_1= int(texto_1)
print('Tipo de variable de numero_1, de valor {} es {}' .format(numero_1, type(numero_1)))
numero_2 = int(texto_2)
print('Tipo de variable de numero_2, de valor {} es {}' .format(numero_2, type(numero_2)))
print('')
print('Comparación de números como números')
print('')
if numero_1 > numero_2:
    mayor = numero_1

    print('El número más grande entre {} y {} es {}'.format(numero_1, numero_2, mayor))

elif numero_2 > numero_1:
    mayor = numero_2

    print('El número más grande entre {} y {} es {}'.format(numero_1, numero_2, mayor))

elif numero_2 == numero_1:
    
    print('Los números ingresados son iguales')    



# Para pensar!
# ¿Por qué cree que texto_2 es mayor a texto_1?
# Siendo números tiene sentido, pero son caracteres, texto,
# aún así el operador arroja el mismo resultado que con las
# variables numéricas, cierto? ¿Por qué creen que es así?
# Esta pregunta estará repetida en el Campus para que puedan
# responder.
# NOTA: La respuesta no se encuentra en el apunte, sino en Google ;)
