# Documentacion

## Instalacion Repositorio

completar al final...

## Bibliotecas

- **sympy:** Utilizado para calculos matematicos. Se elige por sombre *numpy*, pues *sympy* permite un calculo mas sencillo de las derivadas para poder aplicarlas en los metodos numericos requeridos.
  
```python
import sympy as sp 
```

- **csv:** Utilizado para crear documentos .csv requeridos en la pauta

```python
import csv
```

- **matplotlib:** Utilizado para crear los graficos de los analisis numericos requeridos en la pauta.
  
```python
import matplotlib.pyplot as plt 
```

## Codigos de Pyhton

- **\src\data\casos_estudios.py:** Codigo de Python que contiene un diccionario con todas las funciones a estudiar, mas algunos elementos claves (Tolerancia, Iteraciones maximas permitidas). Las funciones del diccionario presentan datos claves para su estudio, como; puntos iniciales *x0*, *x1* y rangos *[a, b]*. Las funciones *f(x)* estan implementadas como funciones **lambda** para poder facilitar los calculos.
- **\src\scripts\biseccion.py:** Implementacion del metodo de Biseccion. El codigo cuenta con 3 funciones: *bolzano()* -> Retorna un valor booleano si hay cambio de signo. *valor_medio()* -> Calculo punto C. *biseccion()* -> Proceso iterativo del metodo.
- **\src\scripts\falsa_posicion.py:** Implementacion del metodo de Falsa Posicion. El codigo cuenta con 3 fucniones: *bolzano()* -> Retorna un valor booleano si hay cambio de signo. *punto_corte()* -> Calculo del punto C a partir de rectas. *falsa_posicion()* -> Proceso iterativo del metodo.
- **\src\scripts\newton_raphson.py:** Implementacion del metodo de Newton-Raphson. El codigo cuenta con 3 funciones: *derivar()* -> Calcula la derivada de la funcion con **sympy**. *siguiente_punto()* -> Calculo del siguiente punto utilizando la recta tangente a la funcion. *newton_raphson()* -> Proceso iterativo del metodo.
- **\src\scripts\nr_modificado.py:** Implementacion del metodo de Newton-Raphson Modificado. El codgo cuenta con 3 funciones: *derivar()* -> Deriva la funcion con **sympy**. *siguiente_punto()* -> Busca una posible raiz de forma similar al metodo anterior, pero modificando la formula para mejorar convergencia. *nweton_raphson_modificado()* -> Proceso iterativo del metodo.
- **\src\scripts\punto_fijo.py:** Implementa el metodo de Punto Fijo. El codigfo cuenta con 2 funciones: *g_x()* -> Obtiene g(x) a partir de f(x). En el primer **for** la funcion encuentra todas las formas posibles de despejar la funcion, en el segundo **for** se utiliza **sympy** para despejar cada uno de las posibles formas de despejar la funcion, dejando todo de la forma x = g(x), en el ultimo **for** se verifica si el punto y la funcion elegida cumplen con que al derivada de |g(x)| sea menor a 0. *punto_fijo()* -> Proceso iterativo del metodo.
- **\src\scripts\secante.py:** Implementa el metodo de la Secante. El codigo cuenta con 2 funciones: *nuevo_punto()* -> Busca el neuvo punto a aprtir de una recta secante que pasa por dos puntos de la funcion. *secante()* -> Proceso iterativo del metodo.

## main.py

Script principal del programa, se encuentra en la ruta **\src\main.py**, este codigo a diferencia de los otros se encuentra en la raiz de la carpeta **\src**, para que no se mezcle con los demas codigos que se utilizan como modulos dentro de la misma.

El codigo dentro del programa se encuentra divido en 4 secciones principales:

- **Librerias:** Se utiliza *csv* y *matplotlib*, mas los modulos propios *\src\data\casos_estudio.py* y los codigos .py de la carpeta *\src\scripts*.
- **Primera parte:** Se definen variables globales a partir del diccionario de *casos_estudio.py*. En la funcion *obtener_resultados()* se utilizan las variables globales para acceder a todas las funciones y los datos asociados a ella, ademas de utilizar todos los scripts de la carpeta *\src\scripts* para el calculo de todos los metodos numericos en todas las funciones estudiadas. Esta parte cuenta con 2 funciones mas que son de ayuda para obtener datos para posteriormente analizar y generar graficos y archivos.
- **Segunda parte:** Creacion de archivos .csv, alojados en la ruta *\src\data*. El primer archivo.csv creado corresponde a los datos referidos a la raiz, error (ultimo error del historial de errores) y la cantidad de iteraciones. El segundo archivo.csv corresponde al solicitado en el cual se encuantra las funciones y metodos correspondientes, junto con sus raices *x* y las funciones evaluadas en las raices *f(x)*.
- **Tercera parte:** Creacion de graficos. Primera funcion *grafico_FuncionRaiz()* -> Se muestran las funciones graficadas, con un punto senialado (raiz), el punto elegido fue seleccionado de entre el resultado de todos los metodos, escogiendo asi la raiz mas cercana al 0 evaluada en la funcion. Segunda funcion *grafico_ErrorIteracion()* -> 6 graficos que representan como el error se hace cada vez mas pequenio por cada iteracion que hace el metodo. Tercer grafico *grafico_CantidadIteraciones()* -> Corresponde a la representacion de cuantas iteraciones necesito cada metodo hasta llegar al criterio de parada, en cada una de las funciones.

### Observaciones

- No se utiliza la libreria numpy, pues es su lugar se utiliza sympy. La eleccion anterior tiene realcion con que sympy trae funciones propias para obtener la derivada de una funcion sin necesidad de hacerlo a mano. Tambien para evitar errores matematicos se siguio utilizando sympy para cualquier funcion matemarica asociada, como cos(), sqrt(), ln(), etc.
- En los documentos, si el metodo no llega a una raiz se pone el argumento *NAN* indicando que el resultado no es un numero (no converge con las condiciones dadas). En los documentos como tal no es posible identificar porque falla, sin embargo a traves de consola utilizando *prints* en el programa si es posible hacerlo. En cuanto a los graficos, si el valor a graficar es *None* simplemnte no se grafica.
- Se declara uso de IA para ayuda en sintaxis en las librerias utilizadas (sympy, matplotlib, csv).
- Proyecto realizado por: Hugo Albornoz Contreras - COMPUTACIÓN NUMÉRICA-S2 [INF321]|secc:S2
