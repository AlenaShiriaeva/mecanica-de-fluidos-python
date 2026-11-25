"""Problema 2. Compuerta rectangular vertical.

Una compuerta vertical de 2 m de ancho y 3 m de alto cierra un tanque de agua.
El borde de arriba de la compuerta esta 1.5 m por debajo de la superficie libre
y ahi tiene la bisagra. Abajo apoya contra un tope.

    a) Fuerza total del agua sobre la compuerta.
    b) Profundidad del centro de presiones.
    c) Fuerza que tiene que hacer el tope de abajo para que no se abra.

Planteo
    La fuerza es la presion en el centroide por el area.

        F = rho g hc A

    El centro de presiones queda mas abajo que el centroide.

        ycp = hc + Ic / (hc A)        con Ic = b H^3 / 12

    Para el tope se toman momentos respecto de la bisagra.

        F (ycp - d) = R H
"""
from comun import G, RHO_AGUA


def compuerta(b, alto, d, rho=RHO_AGUA, g=G):
    area = b * alto
    hc = d + alto / 2
    fuerza = rho * g * hc * area
    ic = b * alto ** 3 / 12
    ycp = hc + ic / (hc * area)
    reaccion_tope = fuerza * (ycp - d) / alto
    return fuerza, hc, ycp, reaccion_tope


if __name__ == "__main__":
    F, hc, ycp, R = compuerta(b=2.0, alto=3.0, d=1.5)
    print(f"a) F   = {F / 1000:.1f} kN  (centroide a {hc:.2f} m)")
    print(f"b) ycp = {ycp:.3f} m de profundidad")
    print(f"c) R   = {R / 1000:.1f} kN en el tope")
