# mecanica-de-fluidos-python

Problemas clasicos de mecanica de fluidos resueltos con Python. Cada archivo tiene el enunciado y el planteo arriba, y abajo el codigo que lo resuelve. Los enunciados los arme yo con datos inventados.

Solo usa la libreria estandar de Python, no hace falta instalar nada.

## Como se corre

```
python3 p04_perdida_de_carga.py
```

Cada archivo se corre solo. Las constantes y las funciones que se repiten estan en `comun.py`.

## Problemas

| Archivo | Tema | Resultado |
|---|---|---|
| `p01_manometro_diferencial.py` | Manometro de mercurio entre dos tubos | pA menos pB da 30.9 kPa |
| `p02_compuerta_vertical.py` | Fuerza y centro de presiones en una compuerta | 176.6 kN a 3.25 m de profundidad |
| `p03_vaciado_tanque.py` | Vaciado de un tanque por un orificio, formula cerrada y RK4 | 27.5 min para vaciarse |
| `p04_perdida_de_carga.py` | Darcy Weisbach con Colebrook y Swamee Jain | 5.20 m de perdida |
| `p05_punto_de_funcionamiento.py` | Curva de bomba contra curva del sistema | 46.2 L/s con 21.45 m |

## Que tiene comun.py

* `colebrook` resuelve el factor de friccion iterando. Arranca desde Swamee y Jain y converge en pocas vueltas.
* `swamee_jain` es la aproximacion explicita.
* `biseccion` busca raices. La uso para el punto de funcionamiento de la bomba.

## Ideas para seguir

* Tuberias en paralelo y redes con Hardy Cross.
* Golpe de ariete con la formula de Joukowsky.
* Vertederos y canales abiertos con Manning.
