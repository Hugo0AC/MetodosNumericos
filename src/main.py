import sympy as sp
import matplotlib.pyplot as plt
import csv
from scripts.biseccion import biseccion #funcion,a,b,tolerancia,max_iteraciones
from scripts.falsa_posicion import falsa_posicion #funcion,a,b,tolerancia,max_iteraciones
from scripts.punto_fijo import punto_fijo #funcion,x0,tolerancia.max_iteraciones
from scripts.secante import secante #funcion,x1,x0,tolerancia,max_iteraciones
from scripts.newton_raphson import newton_raphson #funcion,x0,tolerancia,max_iteraciones
from scripts.nr_modificado import newton_raphson_modificado #funcion,x0,tolerancia,max_iteraciones
from data.casos_estudio import CE


t = CE["Tolerancia"]
it = CE["Iteraciones"]
ps = CE["PolinomioSimple"]
pd = CE["PolinomioDoble"]
lo = CE["Logaritmo"]
ex = CE["Exponencial"]
tri = CE["Trigonometrica"]
mi = CE["Mixta"]


def obtener_resultados():
    func_ps = [] #Funcion Polinomica Simple
    func_ps.append(biseccion(ps["f(x)"], ps["a"], ps["b"], t, it))
    func_ps.append(falsa_posicion(ps["f(x)"], ps["a"], ps["b"], t, it))
    func_ps.append(punto_fijo(ps["f(x)"], ps["x0"], t, it))
    func_ps.append(secante(ps["f(x)"], ps["x1"], ps["x0"], t, it))
    func_ps.append(newton_raphson(ps["f(x)"], ps["x0"], t, it))
    func_ps.append(newton_raphson_modificado(ps["f(x)"], ps["x0"], t, it))

    func_pd = [] #Funcion Polinomica Doble
    func_pd.append(biseccion(pd["f(x)"], pd["a"], pd["b"], t, it))
    func_pd.append(falsa_posicion(pd["f(x)"], pd["a"], pd["b"], t, it))
    func_pd.append(punto_fijo(pd["f(x)"], pd["x0"], t, it))
    func_pd.append(secante(pd["f(x)"], pd["x1"], pd["x0"], t, it))
    func_pd.append(newton_raphson(pd["f(x)"], pd["x0"], t, it))
    func_pd.append(newton_raphson_modificado(pd["f(x)"], pd["x0"], t, it))

    func_log = [] #Funcion Logaritmica
    func_log.append(biseccion(lo["f(x)"], lo["a"], lo["b"], t, it))
    func_log.append(falsa_posicion(lo["f(x)"], lo["a"], lo["b"], t, it))
    func_log.append(punto_fijo(lo["f(x)"], lo["x0"], t, it))
    func_log.append(secante(lo["f(x)"], lo["x1"], lo["x0"], t, it))
    func_log.append(newton_raphson(lo["f(x)"], lo["x0"], t, it))
    func_log.append(newton_raphson_modificado(lo["f(x)"], lo["x0"], t, it))

    func_exp = [] #Funcion Exponencial
    func_exp.append(biseccion(ex["f(x)"], ex["a"], ex["b"], t, it))
    func_exp.append(falsa_posicion(ex["f(x)"], ex["a"], ex["b"], t, it))
    func_exp.append(punto_fijo(ex["f(x)"], ex["x0"], t, it))
    func_exp.append(secante(ex["f(x)"], ex["x1"], ex["x0"], t, it))
    func_exp.append(newton_raphson(ex["f(x)"], ex["x0"], t, it))
    func_exp.append(newton_raphson_modificado(ex["f(x)"], ex["x0"], t, it))

    func_tri = [] #Funcion Trigonometrica
    func_tri.append(biseccion(tri["f(x)"], tri["a"], tri["b"], t, it))
    func_tri.append(falsa_posicion(tri["f(x)"], tri["a"], tri["b"], t, it))
    func_tri.append(punto_fijo(tri["f(x)"], tri["x0"], t, it))
    func_tri.append(secante(tri["f(x)"], tri["x1"], tri["x0"], t, it))
    func_tri.append(newton_raphson(tri["f(x)"], tri["x0"], t, it))
    func_tri.append(newton_raphson_modificado(tri["f(x)"], tri["x0"], t, it))

    func_mix = [] #Funcion Mixta
    func_mix.append(biseccion(mi["f(x)"], mi["a"], mi["b"], t, it))
    func_mix.append(falsa_posicion(mi["f(x)"], mi["a"], mi["b"], t, it))
    func_mix.append(punto_fijo(mi["f(x)"], mi["x0"], t, it))
    func_mix.append(secante(mi["f(x)"], mi["x1"], mi["x0"], t, it))
    func_mix.append(newton_raphson(mi["f(x)"], mi["x0"], t, it))
    func_mix.append(newton_raphson_modificado(mi["f(x)"], mi["x0"], t, it))

    return func_ps, func_pd, func_log, func_exp, func_tri, func_mix


def crear_csv(func_ps, func_pd, func_log, func_exp, func_tri, func_mix):
    funciones = ["PolinomicaSimple", "PolinomicaDoble", "Logaritmica", "Exponencial", "Trigonometrica", "Mixta"]
    metodos = ["Biseccion", "FalsaPosicion", "PuntoFijo", "Secante", "NewtonRaphson", "NewtonRaphsonMOD"]
    resultados = [func_ps, func_pd, func_log, func_exp, func_tri, func_mix]

    with open("src\\data\\resultados.csv", "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["Metodo"] + funciones)
        for i, metodo in enumerate(metodos):
            fila = [metodo]
            for resultado_funcion in resultados:
                resultado = resultado_funcion[i]
                if resultado[0] is None:
                    datos = "Raiz: N.A.N. | Error: N.A.N. | Iteraciones: N.A.N."
                else:
                    valor, historial_errores, iteraciones = resultado
                    datos = (f"Raiz: {valor} | Error: {historial_errores[-1]} | Iteraciones: {iteraciones}")

                fila.append(datos)
            escritor.writerow(fila)

def grafico_FuncionRaiz():
    _, ax = plt.subplots(2, 3)

    fps = ps["f(x)"]
    fpd = pd["f(x)"]
    flo = lo["f(x)"]
    fex = ex["f(x)"]
    ftri = tri["f(x)"]
    fmi = mi["f(x)"]

    valores_x = [i / 100 for i in range(-400, 401)]

    ax[0, 0].plot(valores_x, [fps(x) for x in valores_x])
    ax[0, 0].set_xlim(-4, 4)
    ax[0, 0].set_ylim(-4, 4)
    ax[0, 0].set_title("Polinomio Simple")


    ax[0, 1].plot(valores_x, [fpd(x) for x in valores_x])
    ax[0, 1].set_xlim(-4, 4)
    ax[0, 1].set_ylim(-4, 4)
    ax[0, 1].set_title("Polinomio Doble")


    x_log = [x for x in valores_x if x > 0]
    ax[0, 2].plot(x_log, [flo(x) for x in x_log])
    ax[0, 2].set_xlim(0, 4)
    ax[0, 2].set_ylim(0, 4)
    ax[0, 2].set_title("Logaritmo")

    
    ax[1, 0].plot(valores_x, [fex(x) for x in valores_x])
    ax[1, 0].set_xlim(-4, 4)
    ax[1, 0].set_ylim(-4, 4)
    ax[1, 0].set_title("Exponencial")

    
    ax[1, 1].plot(valores_x, [ftri(x) for x in valores_x])
    ax[1, 1].set_xlim(-4, 4)
    ax[1, 1].set_ylim(-4, 4)
    ax[1, 1].set_title("Trigonometica")

    x_mix = [x for x in valores_x if x >= 0]
    ax[1, 2].plot(x_mix, [fmi(x) for x in x_mix])
    ax[1, 2].set_xlim(0, 4)
    ax[1, 2].set_ylim(0, 4)
    ax[1, 2].set_title("Mixta")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    grafico_FuncionRaiz()
