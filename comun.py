"""Constantes y funciones que usan varios problemas."""
import math

G = 9.81            # m/s2
RHO_AGUA = 1000.0   # kg/m3
NU_AGUA_20C = 1.004e-6  # m2/s, viscosidad cinematica del agua a 20 C


def area_circulo(d):
    return math.pi * d ** 2 / 4


def reynolds(v, d, nu=NU_AGUA_20C):
    return v * d / nu


def colebrook(re, rug_rel, tol=1e-10, max_iter=100):
    """Factor de friccion de Darcy por Colebrook, iterando sobre 1/sqrt(f).

    Arranca desde Swamee y Jain, que ya queda muy cerca. En flujo laminar
    devuelve 64/Re directamente.
    """
    if re < 2300:
        return 64 / re
    x = 1 / math.sqrt(swamee_jain(re, rug_rel))
    for _ in range(max_iter):
        nuevo = -2 * math.log10(rug_rel / 3.7 + 2.51 * x / re)
        if abs(nuevo - x) < tol:
            return 1 / nuevo ** 2
        x = nuevo
    raise RuntimeError("Colebrook no convergio")


def swamee_jain(re, rug_rel):
    """Aproximacion explicita de Colebrook. Vale para 5e3 < Re < 1e8."""
    return 0.25 / math.log10(rug_rel / 3.7 + 5.74 / re ** 0.9) ** 2


def biseccion(fn, a, b, tol=1e-9, max_iter=200):
    fa = fn(a)
    if fa * fn(b) > 0:
        raise ValueError("la funcion no cambia de signo en el intervalo")
    for _ in range(max_iter):
        m = (a + b) / 2
        fm = fn(m)
        if abs(fm) < tol or (b - a) / 2 < tol:
            return m
        if fa * fm < 0:
            b = m
        else:
            a, fa = m, fm
    return (a + b) / 2
