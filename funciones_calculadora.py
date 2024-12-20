def sumar_n_numeros():
    numeros_a_sumar = int(input('¿Cuántos números quieres sumar? '))
    lista_numeros = []

    for numero in range(0, numeros_a_sumar):
        numero_a_sumar = float(input(f'Ingresa el número {numero + 1} a sumar: '))
        lista_numeros.append(numero_a_sumar)

    return sum(lista_numeros)

def multiplicacion_n_numeros():
    resultado = 1
    numeros_a_multiplicar = int(input('¿Cuántos números quieres multiplicar? '))
    
    for numero in range(0, numeros_a_multiplicar):
        numero_a_multiplicar = float(input(f'Ingresa el número {numero + 1} a multiplicar: '))
        resultado *= numero_a_multiplicar
        
    return resultado

def division_2_numeros():
    numerador = float(input('Ingresa el numerador: '))
    denominador = float(input('Ingresa el denominador: '))
    
    if denominador == 0:
        print('No puedes dividir entre 0')
        return None
    
    return numerador / denominador

def resolver_para_y():
    pendiente = float(input('Por favor, ingresa la pendiente: '))
    ordenada_origen = float(input('Por favor, ingresa la irdenada al origen: '))
    punto_x = int(input('Por favor, ingresa el punto en x: '))

    resultado = (pendiente * punto_x) + ordenada_origen

    return {'resultado': resultado, 'pendiente': pendiente, 'ordenada_origen': ordenada_origen, 'punto_x': punto_x}