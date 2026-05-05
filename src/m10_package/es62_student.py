import math


def crea_punto(x: float, y: float) -> dict:
    return {"x": x, "y": y}


def distanza_tra_punti(p1: dict, p2: dict) -> float:
    x1 = p1["x"]
    y1 = p1["y"]

    x2 = p2["x"]
    y2 = p2["y"]

    distanza = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distanza


def info_punto(punto: dict) -> str:
    return f"({punto['x']}, {punto['y']})"
from . import distanza_tra_punti, crea_punto, info_punto


def crea_linea(p1: dict, p2: dict) -> dict:
    return {"p1": p1, "p2": p2}


def lunghezza_linea(linea: dict) -> float:
    return distanza_tra_punti(linea["p1"], linea["p2"])


def punto_medio(linea: dict) -> dict:
    x1 = linea["p1"]["x"]
    y1 = linea["p1"]["y"]

    x2 = linea["p2"]["x"]
    y2 = linea["p2"]["y"]

    xm = (x1 + x2) / 2
    ym = (y1 + y2) / 2

    return crea_punto(xm, ym)


def info_linea(linea: dict) -> str:
    p1 = info_punto(linea["p1"])
    p2 = info_punto(linea["p2"])

    return f"Linea da {p1} a {p2}"
from coordinate import punti, linee


print("=== Coordinate e Linee ===\n")

# Creazione punti
pA = punti.crea_punto(0.0, 0.0)
pB = punti.crea_punto(3.0, 4.0)
pC = punti.crea_punto(6.0, 0.0)

print("Punti:")
print(f"- Punto A: {punti.info_punto(pA)}")
print(f"- Punto B: {punti.info_punto(pB)}")
print(f"- Punto C: {punti.info_punto(pC)}")

# Creazione linee
l1 = linee.crea_linea(pA, pB)
l2 = linee.crea_linea(pB, pC)

print("\nLinee:")

for linea in [l1, l2]:
    lunghezza = round(linee.lunghezza_linea(linea), 2)
    medio = linee.punto_medio(linea)

    print(
        f"- {linee.info_linea(linea)} | "
        f"Lunghezza: {lunghezza:.2f} | "
        f"Punto medio: {punti.info_punto(medio)}"
    )