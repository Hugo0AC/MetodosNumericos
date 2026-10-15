import sympy as sp

def derivar(funcion):
    x = sp.symbols('x')
    derivada = sp.diff(funcion(x), x)
    return derivada

def siguiente_punto(funcion, derivada, x_actual):
    x_nueva = x_actual - (funcion(x_actual) / derivada.subs(sp.symbols('x'), x_actual))
    return x_nueva

def newton_raphson(funcion, x_actual, tolerancia, max_iteraciones):
    iteracion = 0
    derivada = derivar(funcion)

    while iteracion < max_iteraciones:
        x_nueva = float(siguiente_punto(funcion, derivada, x_actual))
        error = abs((x_nueva - x_actual) / x_nueva) * 100 if x_nueva != 0 else abs(x_nueva - x_actual) * 100

        if abs(funcion(x_actual)) < tolerancia:
            return x_actual, error, iteracion

        x_actual = x_nueva
        iteracion += 1
    return None, "No se llego a una solucion dentro del numero maximo de itraciones"

if __name__ == "__main__":

    funcion = lambda x: x**3 - x - 2

    a = 1

    b = 2

    tolerancia = 1e-6  

    max_iteraciones = 100

    resultado = newton_raphson(funcion, a, tolerancia, max_iteraciones)

    print(f"Resultado: {resultado}, error: {resultado[1]}%, iteraciones: {resultado[2]}")