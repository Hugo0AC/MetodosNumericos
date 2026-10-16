import sympy as sp

CASOS = {
    "PolinomioSimple": {
        "f(x)": lambda x: x**3 - x - 2,
        "a": 1,
        "b": 2,
        "x0": 1.2,
        "x1": 2.1,
    },
    "PolinomioDoble": {
        "f(x)": lambda x: (x - 2)**2, #Sin cambio de signo
        "a": 1,
        "b": 2,
        "x0": 1.2,
        "x1": 2.1,
    },
    "Logaritmo": {
        "f(x)": lambda x: sp.ln(x) + x - 4,
        "a": 2,
        "b": 3,
        "x0": 2.2,
        "x1": 3.34,
    },
    "Exponencial": {
        "f(x)": lambda x: sp.exp(-x) - x,
        "a": 0,
        "b": 1,
        "x0": 0.01,
        "x1": 1.02,
    },
    "Trigonometrica": {
        "f(x)": lambda x: sp.cos(x) - x,
        "a": 0,
        "b": 1,
        "x0": 0.1,
        "x1": 1.3,
    },
    "Mixta": {
        "f(x)": lambda x: sp.sqrt(x) - sp.cos(x),
        "a": 0.5,
        "b": 1.1,
        "x0": 0.023,
        "x1": 0.93,
    },
    "Tolerancia": 1e-6,
    "Iteraciones": 100
}