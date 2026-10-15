import sympy as sp

def derivar(funcion):
    x = sp.symbols('x')
    derivada = sp.diff(funcion(x), x)
    return derivada

def siguiente_punto(funcion, denominador, x_actual):
    numerador = funcion(x_actual)
    x_nueva = x_actual - (numerador / denominador)
    return x_nueva

def newton_raphson(funcion, x_actual, tolerancia, max_iteraciones):
    iteracion = 0
    derivada = derivar(funcion)
    denominador = float(derivada.subs(sp.symbols('x'), x_actual))

    while iteracion < max_iteraciones:
        x_nueva = siguiente_punto(funcion, denominador, x_actual)
        x_actual = x_nueva

        if abs(funcion(x_actual)) < tolerancia:
            return x_actual
        
        iteracion += 1

    raise Exception("No se llego a una solucion dentro del numero maximo de itraciones")

if __name__ == "__main__":
    funcion = lambda x: x**3 - x - 2
    a = 1
    b = 2
    tolerancia = 1e-6   
    max_iteraciones = 100
    resultado = newton_raphson(funcion, b, tolerancia, max_iteraciones)
    print(f"Resultado: {resultado}")
