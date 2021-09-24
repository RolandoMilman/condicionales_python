# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite ingresar tres valores de temperatura
De las temperaturas ingresadas por consola determinar:
1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
3 - ¿Cuál es el promedio de las temperaturas ingresadas?

En cada caso imprimir en pantalla el resultado

IMPORTANTE: Para ordenar las temperatuas debe utilizar condicionales compuestos o anidados,
no se busca utilizar bucles o algoritmos de ordenamiento ya que aún no hemos llegado a ese
contenido. Recomendamos pensar bien este problema de lógica con un lápiz y papel.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio

numero_1 = float(input('Ingrese el primer valor de temperatura:'))
numero_2 = float(input('Ingrese el segundo valor de temperatura:'))
numero_3 = float(input('Ingrese el tercer valor de temperatura:'))

if numero_1 > numero_2:
    if numero_1 > numero_3:
        print('El valor mayor de temperatura {} corresponde al número {}'.format(numero_1, '1'))
        if numero_2 > numero_3:
            print('El 2do valor de temperatura {} corresponde al número {}'.format(numero_2, '2'))
            print('El 3er valor de temperatura {} corresponde al número {}'.format(numero_3, '3'))
        else:
            print('El 2do valor de temperatura {} corresponde al número {}'.format(numero_3, '3'))
            print('El 3er valor de temperatura {} corresponde al número {}'.format(numero_2, '2'))
    else:
        print('El valor mayor de temperatura {} corresponde al número {}'.format(numero_3, '3'))    
        if numero_2 > numero_1:
            print('El 2do valor de temperatura {} corresponde al número {}'.format(numero_2, '2'))
            print('El 3er valor de temperatura {} corresponde al número {}'.format(numero_1, '1'))
        else:
            print('El 2do valor de temperatura {} corresponde al número {}'.format(numero_1, '1'))
            print('El 3er valor de temperatura {} corresponde al número {}'.format(numero_2, '2'))
else:
    if numero_2 > numero_3:
        print('El valor mayor de temperatura {} corresponde al número {}'.format(numero_2, '2'))
        if numero_1 > numero_3:
            print('El 2do valor de temperatura {} corresponde al número {}'.format(numero_1, '1'))
            print('El 3er valor de temperatura {} corresponde al número {}'.format(numero_3, '3'))
        else:
            print('El 2do valor de temperatura {} corresponde al número {}'.format(numero_3, '3'))
            print('El 3er valor de temperatura {} corresponde al número {}'.format(numero_1, '1'))
    else:
        print('El valor mayor de temperatura {} corresponde al número {}'.format(numero_3, '3'))    
        if numero_2 > numero_1:
            print('El 2do valor de temperatura {} corresponde al número {}'.format(numero_2, '2'))
            print('El 3er valor de temperatura {} corresponde al número {}'.format(numero_1, '1'))
        else:
            print('El 2do valor de temperatura {} corresponde al número {}'.format(numero_1, '1'))
            print('El 3er valor de temperatura {} corresponde al número {}'.format(numero_2, '2'))