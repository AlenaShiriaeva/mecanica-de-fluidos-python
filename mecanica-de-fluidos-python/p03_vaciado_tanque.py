"""Problema 3. Vaciado de un tanque por un orificio en el fondo.

Un tanque cilindrico de 1.2 m de diametro tiene agua hasta 2 m. En el fondo hay
un orificio de 3 cm de diametro con coeficiente de descarga 0.62. Cuanto tarda
en bajar a 0.5 m? Y en vaciarse del todo?

Planteo
    El caudal que sale por el orificio sale de Torricelli corregido con Cd.

        Q = Cd a sqrt(2 g h)

    Lo que sale es lo que baja el nivel en el tanque.

        At dh/dt = -Cd a sqrt(2 g h)

    Separando variables e integrando entre h0 y h queda una formula cerrada.

        t = At / (Cd a) * 2 (sqrt(h0) - sqrt(h)) / sqrt(2 g)

    Para comparar, la misma ecuacion se integra tambien con Runge Kutta de
    orden 4. Hasta 0.5 m las dos dan lo mismo. Para el vaciado completo RK4
    se separa alrededor de un segundo, porque sqrt(h) no es suave cerca de h = 0.
"""
import math

from comun import G, area_circulo


def tiempo_analitico(At, a, cd, h0, h, g=G):
    return At / (cd * a) * 2 * (math.sqrt(h0) - math.sqrt(h)) / math.sqrt(2 * g)


def tiempo_rk4(At, a, cd, h0, h_fin, dt=0.5, g=G):
    def dhdt(h):
        return -cd * a * math.sqrt(2 * g * max(h, 0.0)) / At

    t, h = 0.0, h0
    while h > h_fin:
        k1 = dhdt(h)
        k2 = dhdt(h + dt / 2 * k1)
        k3 = dhdt(h + dt / 2 * k2)
        k4 = dhdt(h + dt * k3)
        nuevo = h + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        if nuevo <= h_fin:
            # interpolo el ultimo paso para no pasarme del nivel final
            return t + dt * (h - h_fin) / (h - nuevo)
        t, h = t + dt, nuevo
    return t


if __name__ == "__main__":
    At = area_circulo(1.2)
    a = area_circulo(0.03)
    cd = 0.62
    for h_fin in (0.5, 0.0):
        ta = tiempo_analitico(At, a, cd, 2.0, h_fin)
        tn = tiempo_rk4(At, a, cd, 2.0, max(h_fin, 1e-6))
        print(f"hasta {h_fin:.1f} m   analitico {ta / 60:6.1f} min   RK4 {tn / 60:6.1f} min")
