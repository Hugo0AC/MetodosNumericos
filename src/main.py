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

#n = 0 -> Raiz  ;  n = 1 -> Historial errores  ;  n = -1 -> Iteraciones 
def obtener_datos_resultado(resultados, n):
    datos = []
    for j in range(0, len(resultados)):
        val_metodos = []
        for i in range(0, len(resultados[j])):
            val_dato = resultados[j][i][n]
            if val_dato is None or isinstance(val_dato, str):
                val_metodos.append(None)
            else:
                val_metodos.append(val_dato)
        datos.append(val_metodos)
    return datos

def mejor_raiz(resultados, funciones):
    raices = obtener_datos_resultado(resultados, 0)

    mejores_indices = []
    for i in range(0, len(funciones)):
        residuos_metodos = []
        for j in range(len(raices[i])):
            if raices[i][j] != None:
                residuos_metodos.append(abs(funciones[i](raices[i][j])))
            else: 
                residuos_metodos.append(9999)

        min_residuo = min(residuos_metodos)
        mejor_indice = residuos_metodos.index(min_residuo)
        mejores_indices.append(mejor_indice)

    mejores_puntos = []
    for i in range(0, 6):
        mejores_puntos.append(raices[i][mejores_indices[i]])

    return mejores_puntos



def crear_csv(resultados, funciones, metodos):
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

def csv_funciones(resultados, nombres_funciones, nombres_metodos, fx):  
    #NombreFuncion, Funcion, Metodo, x, f(x)
    raices_totales = obtener_datos_resultado(resultados, 0)
    funciones = ["x**3 - x - 2", "(x - 2)**2", "ln(x) + x - 4", "exp(-x) - x", "cos(x) - x", "sqrt(x) - cos(x)"]

    with open("src\\data\\xfx_evalauda.csv", mode = "w", newline = "", encoding = "utf-8") as file:
        escribir = csv.writer(file)
        escribir.writerow(["NombreFuncion", "Funcion", "Metodo", "x", "f(x)"])
        for raices_funciones, nombre, fun, fx_evaluada in zip(raices_totales, nombres_funciones, funciones, fx):
            for raiz, metodo in zip(raices_funciones, nombres_metodos):
                if raiz == None:
                    escribir.writerow([nombre, fun, metodo, "NAN", "NAN"])
                else:
                    escribir.writerow([nombre, fun, metodo, raiz, fx_evaluada(raiz)])



def grafico_FuncionRaiz(mejores_puntos):
    _, ax = plt.subplots(2, 3)

    fps = ps["f(x)"]
    fpd = pd["f(x)"]
    flo = lo["f(x)"]
    fex = ex["f(x)"]
    ftri = tri["f(x)"]
    fmi = mi["f(x)"]

    # Valor de la raiz
    raiz_ps = mejores_puntos[0]
    raiz_pd = mejores_puntos[1]
    raiz_lo = mejores_puntos[2]
    raiz_ex = mejores_puntos[3]
    raiz_tri = mejores_puntos[4]
    raiz_mi = mejores_puntos[5]

    valores_x = [i / 100 for i in range(-400, 401)]

    ax[0, 0].plot(valores_x, [fps(x) for x in valores_x])
    ax[0, 0].scatter(raiz_ps, fps(raiz_ps), color="red", zorder=5)
    ax[0, 0].set_xlim(-4, 4)
    ax[0, 0].set_ylim(-4, 4)
    ax[0, 0].set_title("PolonomioSimple")
    ax[0, 0].grid(True)

    ax[0, 1].plot(valores_x, [fpd(x) for x in valores_x])
    ax[0, 1].scatter(raiz_pd, fpd(raiz_pd), color="red", zorder=5)
    ax[0, 1].axhline(y=0, color="black", linewidth=1)
    ax[0, 1].plot([raiz_pd - 0.5, raiz_pd + 0.5], [0, 0], color="red", linewidth=2 )
    ax[0, 1].set_xlim(-4, 4)
    ax[0, 1].set_ylim(-4, 4)
    ax[0, 1].set_title("PolinomioDoble")
    ax[0, 1].grid(True)

    x_log = [x for x in valores_x if x > 0]
    ax[0, 2].plot(x_log, [flo(x) for x in x_log])
    ax[0, 2].scatter(raiz_lo, flo(raiz_lo), color="red", zorder=5)
    ax[0, 2].set_xlim(0, 4)
    ax[0, 2].set_ylim(0, 4)
    ax[0, 2].set_title("Logaritmica")
    ax[0, 2].grid(True)

    ax[1, 0].plot(valores_x, [fex(x) for x in valores_x])
    ax[1, 0].scatter(raiz_ex, fex(raiz_ex), color="red", zorder=5)
    ax[1, 0].set_xlim(-4, 4)
    ax[1, 0].set_ylim(-4, 4)
    ax[1, 0].set_title("Exponencial")
    ax[1, 0].grid(True)

    ax[1, 1].plot(valores_x, [ftri(x) for x in valores_x])
    ax[1, 1].scatter(raiz_tri, ftri(raiz_tri), color="red", zorder=5)
    ax[1, 1].set_xlim(-4, 4)
    ax[1, 1].set_ylim(-4, 4)
    ax[1, 1].set_title("Trigonometrica")
    ax[1, 1].grid(True)

    # Mixta
    x_mix = [x for x in valores_x if x >= 0]
    ax[1, 2].plot(x_mix, [fmi(x) for x in x_mix])
    ax[1, 2].scatter(raiz_mi, fmi(raiz_mi), color="red", zorder=5)
    ax[1, 2].set_xlim(0, 4)
    ax[1, 2].set_ylim(0, 4)
    ax[1, 2].set_title("Mixta")
    ax[1, 2].grid(True)

    plt.tight_layout()
    plt.savefig("src\\assets\\Funcion y raiz.png")

#Los metodos siempre iran en el orden:
#Biseccion -> FalsaPosicion -> PuntoFijo -> Secante -> NewtonRaphson ->NewtonRaphsonModificado
#Funciones: PoliniomioSimple[0], PolinomioDoble[1], Logaritmica[2], Exponencial[3], Trignonometrica[4], Mixta[5]
#Errores: Resultados[0][metodo][1] 
def grafico_ErrorIteracion(resultados, nombres_funciones, nombres_medotos):
    historial_errores = obtener_datos_resultado(resultados, 1)
    for i in range(len(historial_errores)):
        nombre_func = nombres_funciones[i]
        plt.figure(figsize = (9, 6))
        for j in range(len(historial_errores[i])):
            historial = historial_errores[i][j]
            if historial is not None and isinstance(historial, list) and len(historial) > 0:
                iteraciones = range(len(historial))
                nombre_metodo = nombres_medotos[j]
                plt.plot(iteraciones, historial, marker='o', markersize=3, label=nombre_metodo, linewidth=1.5)

        plt.yscale('log')
        plt.xlabel('Iteraciones', fontsize=11)
        plt.ylabel('Error relativo porcentual en cada iteracion, por funciones', fontsize=11)
        plt.title(f'Convergencia de metodos - {nombre_func}', fontsize=13, fontweight='bold')
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.grid(True, which="both", linestyle="--", alpha=0.5)
        plt.tight_layout()
        
        plt.savefig(f"src\\assets\\{nombre_func}.png") 
        plt.close()           

def grafico_CantidadIteraciones(resultados, nombres_funciones, nombres_metodos):
    iteraciones = obtener_datos_resultado(resultados, -1)
    num_funciones = len(nombres_funciones)
    num_metodos = len(nombres_metodos)
    
    x = list(range(num_funciones))
    ancho = 0.12  
    plt.figure(figsize=(11, 6))

    for i in range(num_metodos):
        x_barras = []
        y_barras = []
        for j in range(num_funciones):
            val = iteraciones[j][i]
            if val is not None:
                pos_x = x[j] + (i - 2.5) * ancho
                x_barras.append(pos_x)
                y_barras.append(val)
        if x_barras:
            plt.bar(x_barras, y_barras, width=ancho, label=nombres_metodos[i])

    plt.xticks(x, nombres_funciones, rotation=15, ha='right')
    plt.xlabel('Funciones de estudio', fontsize=11, fontweight='bold')
    plt.ylabel('Iteraciones', fontsize=11, fontweight='bold')
    plt.title('Iteraciones por for funcion, segun metodo', fontsize=13, fontweight='bold')
    plt.legend(title='Metodos', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig(f"src\\assets\\Iteraciones por funcion.png")



if __name__ == "__main__":
    func_ps, func_pd, func_log, func_exp, func_tri, func_mix = obtener_resultados()
    resultados = [func_ps, func_pd, func_log, func_exp, func_tri, func_mix]
    funciones = [ps["f(x)"], pd["f(x)"], lo["f(x)"], ex["f(x)"], tri["f(x)"], mi["f(x)"]]
    nombres_funciones = list(CE.keys())[0:-2]
    nombres_medotos = ["Biseccion", "FalsaPosicion", "PuntoFijo", "Secante", "Newton", "NewtonMOD"]
    mejores_puntos = mejor_raiz(resultados, funciones)

    crear_csv(resultados, nombres_funciones, nombres_medotos)
    csv_funciones(resultados, nombres_funciones, nombres_medotos, funciones)

    grafico_FuncionRaiz(mejores_puntos)
    grafico_ErrorIteracion(resultados, nombres_funciones, nombres_medotos)
    grafico_CantidadIteraciones(resultados, nombres_funciones, nombres_medotos)
