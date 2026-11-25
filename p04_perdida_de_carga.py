"""Problema 4. Perdida de carga en una tuberia de acero.

Por una tuberia de acero comercial de 150 m de largo y 100 mm de diametro
interno circulan 15 L/s de agua a 20 C. La rugosidad del acero comercial se
toma como 0.045 mm. Cuanto se pierde por friccion?

Planteo
    Con el caudal y el diametro se saca la velocidad y el numero de Reynolds.
    Con Reynolds y la rugosidad relativa sale el factor de friccion de
    Colebrook, que no tiene formula cerrada y se resuelve iterando. Despues se
    aplica Darcy Weisbach.

        hf = f (L / D) V^2 / (2 g)

    Tambien se muestra el f de Swamee y Jain para ver cuanto difiere.
"""
from comun import G, area_circulo, colebrook, reynolds, swamee_jain


def perdida_friccion(Q, L, D, rug, g=G):
    V = Q / area_circulo(D)
    re = reynolds(V, D)
    f = colebrook(re, rug / D)
    hf = f * (L / D) * V ** 2 / (2 * g)
    return V, re, f, hf


if __name__ == "__main__":
    Q, L, D, rug = 0.015, 150.0, 0.10, 0.045e-3
    V, re, f, hf = perdida_friccion(Q, L, D, rug)
    fsj = swamee_jain(re, rug / D)
    print(f"V  = {V:.2f} m/s")
    print(f"Re = {re:,.0f}")
    print(f"f  = {f:.5f} (Colebrook)   {fsj:.5f} (Swamee Jain, {100 * (fsj - f) / f:+.2f} %)")
    print(f"hf = {hf:.2f} m")
