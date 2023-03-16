#!/usr/bin/env python

from random import randint
import matplotlib as mpl
import matplotlib.pyplot as plt


def lanzar_dado():
    return randint(1, 6)


def noop(mensaje):
    return


def pregunta(r):
    while True:
        respuesta = input(f"En la ronda {r}, ¿deseas continuar? [Y/n]: ").strip()
        if respuesta in ["Y", "y", ""]:
            return "continuar"
        if respuesta in ["N", "n"]:
            return "salir"
        print("Respuesta no es válida, responde Y (para Yes) o n (para No)")


def estrategia1(r):
    return "continuar"


def estrategia2(r):
    return "salir"


def juega(estrategia, log):
    utilidad = 0
    r = 1
    while True:
        accion = estrategia(r)
        if accion == "salir":
            utilidad += 10
            log("¡Ganaste $10!")
            break
        elif accion == "continuar":
            utilidad += 4
            log("¡Ganaste $4!")
            dado = lanzar_dado()
            if dado in (1, 2):
                break
        else:
            raise ValueError(f"La acción `{accion}` no es válida")
    return utilidad


def experimento(estrategia, n=int(10**6)):
    resultados = []
    promedio = 0
    for _ in range(n):
        utilidad = juega(estrategia, noop)
        promedio += utilidad
        resultados.append(utilidad)
    promedio = promedio / n
    fig = plt.figure()
    ax = plt.axes()
    ax.hist(resultados, bins=100, density=True)
    ax.set_title(f"Utilidad promedio {promedio}")
    ax.set_xlabel("Utilidad")
    ax.set_ylabel("Probabilidad")
    fig.savefig("resultado.png")


if __name__ == "__main__":
    # print("Utilidad =", juega(pregunta, print))
    experimento(estrategia1)
