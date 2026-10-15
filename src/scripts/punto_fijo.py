import sympy as sp
funcion = lambda x: sp.ln(x) + x - 4

x, y = sp.symbols('x y')

expresion = str(funcion(x))
caracteres = list(expresion)

posibles_despejes = []
despejes =[]
for i in range(0, len(caracteres)):
    if caracteres[i] == 'x':
        caracteres[i] = 'y'
        posibles_despejes.append(''.join(caracteres))
        caracteres[i] = 'x'
posibles_despejes.append(expresion + " + y = x")

for i, despeje in enumerate(posibles_despejes):
    if i == len(posibles_despejes) - 1:
        partes = despeje.split('=')
        ecuacion = sp.Eq(sp.sympify(partes[0]), sp.sympify(partes[1]))
    else:
        ecuacion = sp.sympify(despeje)
    resultado = sp.solve(ecuacion, y)
    despejes.append(resultado)

despejes_validos = []

for lista in despejes:
    for g in lista:
        if g.has(x):
            derivada = sp.diff(g, x)
            valor = abs(derivada.subs(x, 1.5))

            if valor < 1:
                despejes_validos.append(g)

print("Despejes válidos:", despejes_validos)




