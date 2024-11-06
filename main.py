while True:
    print('''
Bienvenido a mi calculadora, por favor ingresa la opción que desees.
--------------------------------------------------------------------
          
1) Hacer una suma de N números
2) Hacer una multiplicación de N números
3) Hacer una división de 2 números

0) Salir del programa
''')
    
    opcion = int(input('> '))
    if opcion == 0:
        break