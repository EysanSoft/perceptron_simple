import numpy as np
import random
from matplotlib import pyplot as plt
import pandas as pd


def definirDatos(w0, umbral):
    eta = format(random.random(), '.4f')
    X = [
        [1, 0, 0],
        [1, 0, 1],
        [1, 1, 0],
        [1, 1, 1]
    ]

    Y = [
        [0],
        [0],
        [0],
        [1]
    ]
    resultados = bucleEntrenamiento(w0, eta, X, Y, umbral)
    WF = resultados.pop()
    WF = WF['wK']
    salida = [eta, WF, resultados]
    graficar(resultados)
    return salida


def asignarDatos(w0, eta, umbral, bias, x1, x2, y):
    X = [
        [int(bias[0]), int(x1[0]), int(x2[0])],
        [int(bias[1]), int(x1[1]), int(x2[1])],
        [int(bias[2]), int(x1[2]), int(x2[2])],
        [int(bias[3]), int(x1[3]), int(x2[3])]
    ]

    Y = [
        [int(y[0])],
        [int(y[1])],
        [int(y[2])],
        [int(y[3])]
    ]
    resultados = bucleEntrenamiento(w0, eta, X, Y, umbral)
    WF = resultados.pop()
    WF = WF['wK']
    salida = [eta, WF, resultados]
    graficar(resultados)
    return salida


def bucleEntrenamiento(w0, eta, X, Y, umbral):
    listaResultados = []
    iteracion = 0
    while True:
        print(iteracion)
        if iteracion == 0:
            wK = w0
        else:
            wK = wk.copy()

        u1 = (float(wK[0]) * X[0][0]) + (float(wK[1]) * X[0][1]) + (float(wK[2]) * X[0][2])
        u2 = (float(wK[0]) * X[1][0]) + (float(wK[1]) * X[1][1]) + (float(wK[2]) * X[1][2])
        u3 = (float(wK[0]) * X[2][0]) + (float(wK[1]) * X[2][1]) + (float(wK[2]) * X[2][2])
        u4 = (float(wK[0]) * X[3][0]) + (float(wK[1]) * X[3][1]) + (float(wK[2]) * X[3][2])
        u = [format(u1, '.4f'), format(u2, '.4f'), format(u3, '.4f'), format(u4, '.4f')]
        print("U")
        print(u)

        Ycalculada = [0, 0, 0, 0]
        iteracionYC = 0
        for i in u:
            if float(i) < 0:
                Ycalculada[iteracionYC] = 0
            if float(i) >= 0:
                Ycalculada[iteracionYC] = 1
            iteracionYC = iteracionYC + 1
        print("Y Calculada")
        print(Ycalculada)

        e1 = Y[0][0] - Ycalculada[0]
        e2 = Y[1][0] - Ycalculada[1]
        e3 = Y[2][0] - Ycalculada[2]
        e4 = Y[3][0] - Ycalculada[3]
        e = [e1, e2, e3, e4]
        print("Error")
        print(e)

        magnitudError = np.linalg.norm(e)
        print("Magnitud del Error")
        print(magnitudError)

        traspuestaX01 = e[0] * X[0][0]
        traspuestaX02 = e[1] * X[1][0]
        traspuestaX03 = e[2] * X[2][0]
        traspuestaX04 = e[3] * X[3][0]
        traspuestaX0 = traspuestaX01 + traspuestaX02 + traspuestaX03 + traspuestaX04

        traspuestaX11 = e[0] * X[0][1]
        traspuestaX12 = e[1] * X[1][1]
        traspuestaX13 = e[2] * X[2][1]
        traspuestaX14 = e[3] * X[3][1]
        traspuestaX1 = traspuestaX11 + traspuestaX12 + traspuestaX13 + traspuestaX14

        traspuestaX21 = e[0] * X[0][2]
        traspuestaX22 = e[1] * X[1][2]
        traspuestaX23 = e[2] * X[2][2]
        traspuestaX24 = e[3] * X[3][2]
        traspuestaX2 = traspuestaX21 + traspuestaX22 + traspuestaX23 + traspuestaX24

        traspuestaX = [traspuestaX0, traspuestaX1, traspuestaX2]
        traspuestaETA1 = traspuestaX[0] * float(eta)
        traspuestaETA2 = traspuestaX[1] * float(eta)
        traspuestaETA3 = traspuestaX[2] * float(eta)

        saneo = [traspuestaETA1, traspuestaETA2, traspuestaETA3]
        w01 = float(wK[0]) + saneo[0]
        w02 = float(wK[1]) + saneo[1]
        w03 = float(wK[2]) + saneo[2]
        wk = [format(w01, '.4f'), format(w02, '.4f'), format(w03, '.4f')]
        print("Nuevo wk")
        print(wk)
        iteracion = iteracion + 1
        dicRes = {
            'iter': iteracion,
            'magErr': magnitudError,
            'wK': wk,
            'eta': eta
        }
        listaResultados.append(dicRes)
        try:
            if magnitudError < float(umbral):
                dicRes = {
                    'iter': iteracion,
                    'magErr': magnitudError,
                    'wK': wk,
                    'eta': eta
                }
                listaResultados.append(dicRes)
                print("Esta es la magnitud que rompio el bucle.")
                print(magnitudError)
                break
            else:
                print("El ciclo continua.")
        except:
            print("El ciclo nunca termino.")
    return listaResultados


def graficar(lista):
    df = pd.DataFrame(lista)
    print(df)
    fig, ax = plt.subplots()
    ax.plot(df.index.values, df["magErr"])
    plt.xlabel('Iteraciones')
    plt.ylabel('Magnitud del Error')
    plt.title('Curva de Error con ETA: ' + str(df["eta"][0]))
    plt.show()
