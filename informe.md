# Informe

Hugo Albornoz Contreras

## Introduccion

En el presente documento se implementan 6 de los metodos numericos vistos en clases, cada uno se aplica en distintas funciones de estudio bajo un ambiente controlado. Esto tiene la finalidad de comprender con mayor profundidad como se comportan dichos metodos en distintas situaciones.

## Desarrollo Preguntas (Punto 6)

### Que metodo converge en menos iteraciones por funcion, porque?

- **Polinomio Simple:** Tanto Newton-Raphson como Newton-Raphson Modificado tuvieron 4 iteraciones, sin embargo el segundo nos da un valor mas cercano a 0. Esto sucede porque ambos metodos al utilizan derivadas para ajustar la direccion mas exacta a la raiz.
- **Polinomio Doble:** Newton-Raphson Modificado logra encontrar la raiz en solo una iteracion, esto sucede porque al utilizar doble derivada, el metodo transofrma el calculo a uno mas sencillo y directo.
- **Logaritmica:** Tanto Newton-Raphson como Newton-Raphson Modificado tuvieron 3 iteraciones, sin embargo el primer nos da un valor mas cercano a 0. Como se menciono antes por derivadas convergen mas rapido.
- **Exponencial:** Tanto Newton-Raphson como Newton-Raphson Modificado tuvieron 4 iteraciones, sin embargo el segundo nos da un valor mas cercano a 0. Esto sucede porque ambos metodos al utilizan derivadas para ajustar la direccion mas exacta a la raiz.
- **Trigonometrica:** Tanto Newton-Raphson como Newton-Raphson Modificado tuvieron 4 iteraciones, sin embargo el segundo nos da un valor mas cercano a 0. Esto sucede porque ambos metodos al utilizan derivadas para ajustar la direccion mas exacta a la raiz.
- **Mixta:** Con 3 iteraciones converge mas rapido Newton normal, sin embargo con una iteracion mas tanto secante y newtonMOD convergen a un valor mas cercano a 0.
- En resumen los metodos newton y newton modificado, generalmente convergen mas rapido, debido a que utilizan las derivadas y su comportamiento es cuadratico, haciendo que los errores graficquen una curva hacia abajo.
  
### Que orden de convergencia tiene cada metodo, como se refleja en el grafico?

Biseccion, Falsa posicion, Punto fijo tienen convergencia lineal (r = 1). Secante tiene convergencia superlineal (r = 1.618). Newton normal y modificado tienen convergencia cuadratica (r = 2). Esto se refleja de forma muy visual en los graficos, haciendo que los 2 ultimos metodos formen una curva hacia abajo, el de la secante un a recta (al principio un poco curva) muy pronunciada. El resto se ven como pendientes que caen.

### En la funcion doble, que metodos fallan, cuales aplican y cuales se comportan mejor, porque?

Los metodos que dependen del cambio de signo fallan, como biseccion o falsa posicion. El metodo de punto fijo no fue capaz de encontrar una funcion de la forma x = g(x) que cumpliera |g'(x)| < 0. Los que si aplican fueron secante, newton normal y modificado, eso ocurre pues no dependen del cambio de signo sino de estimaciones iniciales. El metodo de newton raphson modificado fue el mejor pues como su derivada es tangente al eje x entonces esto hace que las derivadas puedan ayudar a que el metodo encuentre la raiz de forma muy rapida, en este caso de forma inmediata.

### Influencia del itervalo inicial o estimacion en la convergencia del metodo

En biseccion y falsa posicion el intervalo inicial es determinante, pues de no cumplir el teorema de bolzano, no se puede asegurar que exista una raiz en el intervalo. Los demas metodos abietos, que dependen de una estimacion inicial se comportan de distintan forma segun esta, si esta cerca de 0 convergen mas rapido, si estan lejos, se demoran mas, pero los metodos abiertos no garantizan convergencia, por lo tanto en determinados casos estas estimaciones pueden fallar, por ejemplo en puntos donde una derivada se haga 0, o si la condicion de punto fijo no se cumple con la estimacion inicial.

### Metodo recomendado para cada funcion

Para funciones cuyas derivadas sean complejas se pueden utilizar metodos como secante, falsa posicion o biseccion que no dependen de evaluar derivadas. Para funciones con polinomios, exponenciales, logaritmos y trignomoetricas (siempre que tengan raices simples y sean continuas), utilizaria Newton-Raphson normal o modificado. Por ultimo para funciones con comportamientos raros o desconocidos implementaria algun metodo cerrado, pues estos son los unicos que aseguran convergencia si existe cambio de signo.

## Conclusiones

Al estudiar los distintos metodos y sus comportamientos en las funciones evaluadas se puede concluir que el seleccionar un metodo adecuado a la funcion es de vital importancia, pues dependiendo del comportamiento de esta hay metodos que se benefician u otros que se ven perjudicados. Si hablamos de velocidad pura tanto el metodo de Newton-Raphson como el metodo de Newton-Raphson modificado se destacan, le sigue por detras casi siempre el metodo de la secante, pero dado que los metodos mencionados son metodos abiertos, estos no aseguran convergencia, por lo tanto hay que elegir bien el metodo, no necesariamente por rapidez. El metodo de biseccion (a pesar de ser lento), segura convergencia si hay cambio de signo, por lo tanto lo utilizaria en funciones con comportamientos desconocidos, el metodo de Newton Raphson o el de la secante, se podrian utilizar con funciones cuyas derivadas sean sencillas, el metodo de Newton Raphson Modificado, tambien aplica para lo anterior, pero tambien sirve en funciones cuadraticas.

En cuanto a funciones cuadraticas, al analizar el polinomio con raiz doble, se puede concluir que los metodos cerrados, no sirven pues en el ejemplo no habia cambio de signo. Los metodos abiertos estandar funcionan, pero la derivada se anula en el punto por lo tanto la convergencia de estos metodos, de ser cuadraticos o superlineals, pasan a ser lineales. Por ultimo el metood de Newton Raphson Modificado, al incorporar la segunda derivada, evita lo anterior, permitiendo incluso una convergencia mas rapida.

Como se observo antes en el desarrollo de las respuestas, se puede afirmar que el punto o intervalo inicial es igual de importante o incluso mas que elegir un buen metodo para la funcion, pues el moverlo puede interferir en las iteraciones necesarias para que el metodo pueda converger, necesitando mas o menos iteraciones segun el caso, ademas en ciertos metodos el intervalo como el punto inicial pueden hacer directamente que no exista convergencia (biseccion, si no hay cambio de signo o en punto fijo si la derivda evuluada en el punto no es menor a 0).
