"""Problema 1. Manometro diferencial de mercurio.

Dos tubos horizontales con agua, A y B, estan a la misma altura y se conectan
con un tubo en U que tiene mercurio abajo. El mercurio del lado de B queda
h = 25 cm mas arriba que el del lado de A. Cuanto vale pA - pB?

Datos
    densidad del agua      1000 kg/m3
    densidad del mercurio  13600 kg/m3
    h                      0.25 m

Planteo
    Se baja desde A por el agua hasta la superficie del mercurio del lado de A
    y se sube por el otro lado hasta B. La columna de agua que queda arriba del
    mercurio en cada rama se cancela porque los dos tubos estan a la misma
    altura, salvo el tramo h, que de un lado es agua y del otro mercurio.

        pA + rho_a g (y + h) - rho_m g h - rho_a g y = pB
        pA - pB = (rho_m - rho_a) g h

    y es la altura de agua sobre el mercurio en la rama de B. No hace falta
    conocerla porque se cancela.
"""
from comun import G, RHO_AGUA

RHO_HG = 13600.0


def diferencia_presion(h, rho_m=RHO_HG, rho_a=RHO_AGUA, g=G):
    return (rho_m - rho_a) * g * h


if __name__ == "__main__":
    h = 0.25
    dp = diferencia_presion(h)
    print(f"pA - pB = {dp:.0f} Pa = {dp / 1000:.2f} kPa")
    # Lo mismo expresado en metros de columna de agua
    print(f"equivale a {dp / (RHO_AGUA * G):.2f} m de columna de agua")
