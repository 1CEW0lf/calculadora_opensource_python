from funciones_calculadora import sumar_n_numeros
from funciones_calculadora import multiplicacion_n_numeros
from funciones_calculadora import division_2_numeros
from funciones_calculadora import resolver_para_y

#Se importaron librerias
import numpy as np
import matplotlib.pyplot as plt

while True:
    print('''
Bienvenido a mi calculadora, por favor ingresa la opción que desees.
--------------------------------------------------------------------
          
1) Hacer una suma de N números
2) Hacer una multiplicación de N números
3) Hacer una división de 2 números
4) Resolver la operación en Y (para la ecuación y = mx + b)

0) Salir del programa
''')
    
    opcion = int(input('> '))
    
    if opcion == 0:
        break

    elif opcion == 1:
        resultado = sumar_n_numeros()  # Llamar a la función
        print(f'El resultado de tu suma es {resultado}')

    elif opcion == 2:
        resultado = multiplicacion_n_numeros()  # Llamar a la función
        print(f'El resultado de tu multiplicación es {resultado}')

    elif opcion == 3:
        resultado = division_2_numeros()  # Llamar a la función
        if resultado is not None:  # Comprobar si la división fue válida
            print(f'El resultado de tu división es {resultado}')
        else:
            print("No se puede realizar la división.")

    elif opcion == 4:
        resultado = resolver_para_y()
        print(f'El resultado es: {resultado}')

        x = np.linspace(-10,10)
        y = (resultado['pendiente'] * x) + resultado['ordenada_origen']

        fig, ax = plt.subplots()

        ax.plot(x, y, linewidth = 2.0)
        ax.plot(resultado['punto_x'], resultado['resultado'], 'yo')

        ax.grid(True, linestyle = '-')

        #ax.set(xlim=(0, 8), xticks=np.arange(1, 8), ylim=(0, 8), yticks=np.arange(1, 8))

        plt.show()

    else:
        print('Ejecuta una opción válida')

print('---------------------------------------')
print('Bye, Gracias por usar mi calculadora')