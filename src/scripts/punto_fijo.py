import sympy as sp

def g_x(funcion, punto): #Obtener posible g(x) a partir de f(x)
    x, y = sp.symbols('x y')
    str_funcion = str(funcion(x))
    expresion = list(str_funcion)

    a_despejar = []
    despejes =[]
    depejes_validos = []

    for i in range(0, len(expresion)):
        if expresion[i] == 'x':
            expresion[i] = 'y'
            a_despejar.append(''.join(expresion))
            expresion[i] = 'x'
    a_despejar.append(''.join(expresion) + " + y = x")

    for despeje in a_despejar:
        if despeje == a_despejar[-1]:
            partes = despeje.split('=')
            ecuacion = sp.Eq(sp.sympify(partes[0]), sp.sympify(partes[1]))
        else:
            ecuacion = sp.sympify(despeje)
        resultado = sp.solve(ecuacion, y)
        despejes.append(resultado)

    for lista in despejes:
        for g in lista:
            if g.has(x):
                derivada = sp.diff(g, x)
                valor = abs(derivada.subs(x, punto))

                if valor < 1:
                    depejes_validos.append(g)

    return depejes_validos[0] if depejes_validos else "Sin despeje valido"

def punto_fijo(funcion, x0, tolerancia, max_iteraciones): #Metodo iterativo
    gx = g_x(funcion, x0)
    if gx == "Sin despeje valido":
        return gx
    iteraciones = 0
    errores = []

    while iteraciones < max_iteraciones:
        x1 = float(gx.subs('x', x0))

        error = abs((x1 - x0) / x1) * 100 if x1 != 0 else abs(x1 - x0) * 100
        errores.append(error)
        if abs(x1 - x0) < tolerancia:
            return x1, errores, iteraciones
        x0 = x1
        iteraciones += 1

    return None, "No converge"