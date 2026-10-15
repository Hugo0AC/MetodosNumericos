#Codigo utiliza funciones lambda como parametro
def nuevo_punto(funcion, x_actual, x_anterior):
    numerador = funcion(x_actual) * (x_actual - x_anterior)
    denominador = funcion(x_actual) - funcion(x_anterior)
    x_nueva = x_actual - (numerador / denominador)
    return x_nueva

def secante(funcion, x_actual, x_anterior, tolerancia, max_iteraciones):
    iteracion = 0
    while iteracion < max_iteraciones:
        x_nueva = nuevo_punto(funcion, x_actual, x_anterior)
        error = abs((x_nueva - x_actual) / x_nueva) * 100 if x_nueva != 0 else abs(x_nueva - x_actual) * 100
        x_anterior = x_actual
        x_actual = x_nueva

        if abs(funcion(x_nueva)) < tolerancia:
            return x_nueva, error, iteracion
        
        iteracion += 1

    return None, "No se llego a una solucion dentro del numero maximo de itraciones"
    
if __name__ == "__main__":
    funcion = lambda x: x**3 - x - 2
    a = 1
    b = 2
    tolerancia = 1e-6   
    max_iteraciones = 100
    resultado = secante(funcion, a, b, tolerancia, max_iteraciones)
    print(f"Resultado: {resultado}")