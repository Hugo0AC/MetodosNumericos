import sympy as sp
import matplotlib.pyplot as plt
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


if __name__ == "__main__":
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

    print(func_ps)
    print(func_pd)
    print(func_log)
    print(func_exp)
    print(func_tri)
    print(func_mix)