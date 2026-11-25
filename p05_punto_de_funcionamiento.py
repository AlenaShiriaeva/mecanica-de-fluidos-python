"""Problema 5. Punto de funcionamiento de una bomba.

Una bomba sube agua de un tanque a otro que esta 12 m mas arriba. La tuberia
es de acero comercial, 200 m de largo y 150 mm de diametro, con codos y
valvulas que suman K = 5 en perdidas localizadas. La curva de la bomba que da
el fabricante se aproxima con una parabola.

    Hb(Q) = 30 - 4000 Q^2        (Hb en m, Q en m3/s)

Que caudal entrega la bomba en esta instalacion y con que altura?

Planteo
    La curva del sistema es el desnivel mas las perdidas por friccion y las
    localizadas. El factor de friccion depende del caudal, asi que se recalcula
    con Colebrook para cada Q.

        Hs(Q) = dz + (f L / D + K) V^2 / (2 g)

    El punto de funcionamiento es donde Hb(Q) = Hs(Q). Se busca con biseccion
    entre Q = 0 y el caudal donde la bomba ya no da altura.
"""
import math

from comun import G, area_circulo, biseccion, colebrook, reynolds

DZ, L, D, RUG, K = 12.0, 200.0, 0.15, 0.045e-3, 5.0
H0, KB = 30.0, 4000.0


def altura_bomba(Q):
    return H0 - KB * Q ** 2


def altura_sistema(Q):
    if Q <= 0:
        return DZ
    V = Q / area_circulo(D)
    f = colebrook(reynolds(V, D), RUG / D)
    return DZ + (f * L / D + K) * V ** 2 / (2 * G)


if __name__ == "__main__":
    q_max = math.sqrt(H0 / KB)
    Q = biseccion(lambda q: altura_bomba(q) - altura_sistema(q), 1e-6, q_max)
    print(f"Q = {Q * 1000:.1f} L/s")
    print(f"H = {altura_bomba(Q):.2f} m")
    print()
    print("  Q [L/s]   bomba [m]   sistema [m]")
    for i in range(0, 9):
        q = i * 0.01
        print(f"  {q * 1000:7.0f}   {altura_bomba(q):9.2f}   {altura_sistema(q):11.2f}")
