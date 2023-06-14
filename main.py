import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
import random
from matplotlib import pyplot as plt
import pandas as pd
import entrenamiento


class index(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("vistaPerceptron.ui", self)
        self.tablaResultados.setHidden(True)
        self.tablaSecreta.setHidden(True)
        self.botonOtraVez.setHidden(True)
        self.textoETA.setHidden(True)
        self.entradaETA.setHidden(True)
        self.textoUmbral.setHidden(True)
        self.entradaUmbral.setHidden(True)
        self.textoW0.setHidden(True)
        self.entradaW0.setHidden(True)
        self.botonEjecutar.setHidden(True)
        self.textoBias.setHidden(True)
        self.entradaBias.setHidden(True)
        self.textoX1.setHidden(True)
        self.entradaX1.setHidden(True)
        self.textoX2.setHidden(True)
        self.entradaX2.setHidden(True)
        self.textoY.setHidden(True)
        self.entradaY.setHidden(True)
        self.botonDef.clicked.connect(self.OpsDef)
        self.botonMod.clicked.connect(self.OpsMod)
        self.botonOtraVez.clicked.connect(self.OtraVez)

    def OpsDef(self):
        self.botonDef.setHidden(True)
        self.textoDef.setHidden(True)
        self.botonMod.setHidden(True)
        self.textoMod.setHidden(True)
        self.tablaResultados.setHidden(False)
        self.textoW0.setHidden(False)
        self.entradaW0.setHidden(False)
        self.textoUmbral.setHidden(False)
        self.entradaUmbral.setHidden(False)
        self.botonEjecutar.setHidden(False)
        self.botonEjecutar.clicked.connect(self.metodoDef)

    def metodoDef(self):
        iter1 = self.tablaResultados.item(1, 0)
        iter1_text = iter1.text()
        iter2 = self.tablaResultados.item(1, 1)
        iter2_text = iter2.text()
        iter3 = self.tablaResultados.item(1, 2)
        iter3_text = iter3.text()
        iter4 = self.tablaResultados.item(1, 3)
        iter4_text = iter4.text()
        iter5 = self.tablaResultados.item(1, 4)
        iter5_text = iter5.text()
        if iter1_text == "_":
            print("Iteracion 1")
            w0 = self.entradaW0.text()
            umbral = self.entradaUmbral.text()
            print(w0)
            print(umbral)
            if w0 == "RANDOM":
                valorR1 = format(random.random(), '.4f')
                valorR2 = format(random.random(), '.4f')
                valorR3 = format(random.random(), '.4f')
                w0 = [valorR1, valorR2, valorR3]
                print(w0)
            else:
                w0 = w0.replace(' ', '')
                w0 = w0.split(",")
                print(w0)
            if umbral == "RANDOM":
                umbral = format(random.random(), '.4f')
            self.tablaResultados.setItem(1, 0, QTableWidgetItem(str(w0)))
            resultados = entrenamiento.definirDatos(w0, umbral)
            self.tablaResultados.setItem(0, 0, QTableWidgetItem(str(resultados[0])))
            self.tablaResultados.setItem(2, 0, QTableWidgetItem(str(resultados[1])))
            self.entradaUmbral.setText(str(umbral))
            self.tablaSecreta.setItem(0, 0, QTableWidgetItem(str(resultados[2])))

        elif iter2_text == "_":
            print("Iteracion 2")
            w0 = self.entradaW0.text()
            umbral = self.entradaUmbral.text()
            print(w0)
            if w0 == "RANDOM":
                valorR1 = format(random.random(), '.4f')
                valorR2 = format(random.random(), '.4f')
                valorR3 = format(random.random(), '.4f')
                w0 = [valorR1, valorR2, valorR3]
                print(w0)
            else:
                w0 = w0.replace(' ', '')
                w0 = w0.split(",")
                print(w0)
            if umbral == "RANDOM":
                umbral = format(random.random(), '.4f')
            self.tablaResultados.setItem(1, 1, QTableWidgetItem(str(w0)))
            resultados = entrenamiento.definirDatos(w0, umbral)
            self.tablaResultados.setItem(0, 1, QTableWidgetItem(str(resultados[0])))
            self.tablaResultados.setItem(2, 1, QTableWidgetItem(str(resultados[1])))
            self.tablaSecreta.setItem(0, 1, QTableWidgetItem(str(resultados[2])))

        elif iter3_text == "_":
            print("Iteracion 3")
            w0 = self.entradaW0.text()
            umbral = self.entradaUmbral.text()
            print(w0)
            if w0 == "RANDOM":
                valorR1 = format(random.random(), '.4f')
                valorR2 = format(random.random(), '.4f')
                valorR3 = format(random.random(), '.4f')
                w0 = [valorR1, valorR2, valorR3]
                print(w0)
            else:
                w0 = w0.replace(' ', '')
                w0 = w0.split(",")
                print(w0)
            if umbral == "RANDOM":
                umbral = format(random.random(), '.4f')
            self.tablaResultados.setItem(1, 2, QTableWidgetItem(str(w0)))
            resultados = entrenamiento.definirDatos(w0, umbral)
            self.tablaResultados.setItem(0, 2, QTableWidgetItem(str(resultados[0])))
            self.tablaResultados.setItem(2, 2, QTableWidgetItem(str(resultados[1])))
            self.tablaSecreta.setItem(0, 2, QTableWidgetItem(str(resultados[2])))

        elif iter4_text == "_":
            print("Iteracion 4")
            w0 = self.entradaW0.text()
            umbral = self.entradaUmbral.text()
            print(w0)
            if w0 == "RANDOM":
                valorR1 = format(random.random(), '.4f')
                valorR2 = format(random.random(), '.4f')
                valorR3 = format(random.random(), '.4f')
                w0 = [valorR1, valorR2, valorR3]
                print(w0)
            else:
                w0 = w0.replace(' ', '')
                w0 = w0.split(",")
                print(w0)
            if umbral == "RANDOM":
                umbral = format(random.random(), '.4f')
            self.tablaResultados.setItem(1, 3, QTableWidgetItem(str(w0)))
            resultados = entrenamiento.definirDatos(w0, umbral)
            self.tablaResultados.setItem(0, 3, QTableWidgetItem(str(resultados[0])))
            self.tablaResultados.setItem(2, 3, QTableWidgetItem(str(resultados[1])))
            self.tablaSecreta.setItem(0, 3, QTableWidgetItem(str(resultados[2])))

        elif iter5_text == "_":
            print("Iteracion 5")
            w0 = self.entradaW0.text()
            umbral = self.entradaUmbral.text()
            print(w0)
            if w0 == "RANDOM":
                valorR1 = format(random.random(), '.4f')
                valorR2 = format(random.random(), '.4f')
                valorR3 = format(random.random(), '.4f')
                w0 = [valorR1, valorR2, valorR3]
                print(w0)
            else:
                w0 = w0.replace(' ', '')
                w0 = w0.split(",")
                print(w0)
            if umbral == "RANDOM":
                umbral = format(random.random(), '.4f')
            self.tablaResultados.setItem(1, 4, QTableWidgetItem(str(w0)))
            resultados = entrenamiento.definirDatos(w0, umbral)
            self.tablaResultados.setItem(0, 4, QTableWidgetItem(str(resultados[0])))
            self.tablaResultados.setItem(2, 4, QTableWidgetItem(str(resultados[1])))
            self.tablaSecreta.setItem(0, 4, QTableWidgetItem(str(resultados[2])))
            self.botonEjecutar.setText("Finalizar")

        else:
            print("Se acabo")
            self.textoW0.setHidden(True)
            self.entradaW0.setHidden(True)
            self.textoUmbral.setHidden(True)
            self.entradaUmbral.setHidden(True)
            self.botonEjecutar.setHidden(True)
            self.botonOtraVez.setHidden(False)
            curva1 = self.tablaSecreta.item(0, 0)
            curva1_text = curva1.text()
            curva2 = self.tablaSecreta.item(0, 1)
            curva2_text = curva2.text()
            curva3 = self.tablaSecreta.item(0, 2)
            curva3_text = curva3.text()
            curva4 = self.tablaSecreta.item(0, 3)
            curva4_text = curva4.text()
            curva5 = self.tablaSecreta.item(0, 4)
            curva5_text = curva5.text()
            listaCurvas = [curva1_text, curva2_text, curva3_text, curva4_text, curva5_text]
            graficarCincoCurvas(listaCurvas)

    def OpsMod(self):
        self.botonDef.setHidden(True)
        self.textoDef.setHidden(True)
        self.botonMod.setHidden(True)
        self.textoMod.setHidden(True)
        self.tablaResultados.setHidden(False)
        self.textoBias.setHidden(False)
        self.entradaBias.setHidden(False)
        self.textoX1.setHidden(False)
        self.entradaX1.setHidden(False)
        self.textoX2.setHidden(False)
        self.entradaX2.setHidden(False)
        self.textoY.setHidden(False)
        self.entradaY.setHidden(False)
        self.textoW0.setHidden(False)
        self.entradaW0.setHidden(False)
        self.textoETA.setHidden(False)
        self.entradaETA.setHidden(False)
        self.textoUmbral.setHidden(False)
        self.entradaUmbral.setHidden(False)
        self.botonEjecutar.setHidden(False)
        self.botonEjecutar.clicked.connect(self.metodoMod)

    def metodoMod(self):
        iter1 = self.tablaResultados.item(1, 0)
        iter1_text = iter1.text()
        iter2 = self.tablaResultados.item(1, 1)
        iter2_text = iter2.text()
        iter3 = self.tablaResultados.item(1, 2)
        iter3_text = iter3.text()
        iter4 = self.tablaResultados.item(1, 3)
        iter4_text = iter4.text()
        iter5 = self.tablaResultados.item(1, 4)
        iter5_text = iter5.text()

        if iter1_text == "_":
            print("Iteracion 1")
            bias = self.entradaBias.text()
            x1 = self.entradaX1.text()
            x2 = self.entradaX2.text()
            y = self.entradaY.text()
            w0 = self.entradaW0.text()
            eta = self.entradaETA.text()
            umbral = self.entradaUmbral.text()

            bias = bias.replace(' ', '')
            bias = bias.split(",")

            x1 = x1.replace(' ', '')
            x1 = x1.split(",")

            x2 = x2.replace(' ', '')
            x2 = x2.split(",")

            y = y.replace(' ', '')
            y = y.split(",")

            if w0 == "RANDOM":
                valorR1 = format(random.random(), '.4f')
                valorR2 = format(random.random(), '.4f')
                valorR3 = format(random.random(), '.4f')
                w0 = [valorR1, valorR2, valorR3]
            else:
                w0 = w0.replace(' ', '')
                w0 = w0.split(",")

            if eta == "RANDOM":
                eta = format(random.random(), '.4f')

            if umbral == "RANDOM":
                umbral = format(random.random(), '.4f')

            self.tablaResultados.setItem(1, 0, QTableWidgetItem(str(w0)))

            resultados = entrenamiento.asignarDatos(w0, eta, umbral, bias, x1, x2, y)

            self.tablaResultados.setItem(0, 0, QTableWidgetItem(str(resultados[0])))
            self.tablaResultados.setItem(2, 0, QTableWidgetItem(str(resultados[1])))
            self.tablaSecreta.setItem(0, 0, QTableWidgetItem(str(resultados[2])))
            self.textoETA.setText("ETA 2")
            self.entradaUmbral.setText(str(umbral))

        elif iter2_text == "_":
            print("Iteracion 2")
            bias = self.entradaBias.text()
            x1 = self.entradaX1.text()
            x2 = self.entradaX2.text()
            y = self.entradaY.text()
            w0 = self.entradaW0.text()
            eta = self.entradaETA.text()
            umbral = self.entradaUmbral.text()

            bias = bias.replace(' ', '')
            bias = bias.split(",")

            x1 = x1.replace(' ', '')
            x1 = x1.split(",")

            x2 = x2.replace(' ', '')
            x2 = x2.split(",")

            y = y.replace(' ', '')
            y = y.split(",")

            if w0 == "RANDOM":
                valorR1 = format(random.random(), '.4f')
                valorR2 = format(random.random(), '.4f')
                valorR3 = format(random.random(), '.4f')
                w0 = [valorR1, valorR2, valorR3]
            else:
                w0 = w0.replace(' ', '')
                w0 = w0.split(",")

            if eta == "RANDOM":
                eta = format(random.random(), '.4f')

            if umbral == "RANDOM":
                umbral = format(random.random(), '.4f')

            self.tablaResultados.setItem(1, 1, QTableWidgetItem(str(w0)))

            resultados = entrenamiento.asignarDatos(w0, eta, umbral, bias, x1, x2, y)

            self.tablaResultados.setItem(0, 1, QTableWidgetItem(str(resultados[0])))
            self.tablaResultados.setItem(2, 1, QTableWidgetItem(str(resultados[1])))
            self.tablaSecreta.setItem(0, 1, QTableWidgetItem(str(resultados[2])))
            self.textoETA.setText("ETA 3")
            self.entradaUmbral.setText(str(umbral))

        elif iter3_text == "_":
            print("Iteracion 3")
            bias = self.entradaBias.text()
            x1 = self.entradaX1.text()
            x2 = self.entradaX2.text()
            y = self.entradaY.text()
            w0 = self.entradaW0.text()
            eta = self.entradaETA.text()
            umbral = self.entradaUmbral.text()

            bias = bias.replace(' ', '')
            bias = bias.split(",")

            x1 = x1.replace(' ', '')
            x1 = x1.split(",")

            x2 = x2.replace(' ', '')
            x2 = x2.split(",")

            y = y.replace(' ', '')
            y = y.split(",")

            if w0 == "RANDOM":
                valorR1 = format(random.random(), '.4f')
                valorR2 = format(random.random(), '.4f')
                valorR3 = format(random.random(), '.4f')
                w0 = [valorR1, valorR2, valorR3]
            else:
                w0 = w0.replace(' ', '')
                w0 = w0.split(",")

            if eta == "RANDOM":
                eta = format(random.random(), '.4f')

            if umbral == "RANDOM":
                umbral = format(random.random(), '.4f')

            self.tablaResultados.setItem(1, 2, QTableWidgetItem(str(w0)))

            resultados = entrenamiento.asignarDatos(w0, eta, umbral, bias, x1, x2, y)

            self.tablaResultados.setItem(0, 2, QTableWidgetItem(str(resultados[0])))
            self.tablaResultados.setItem(2, 2, QTableWidgetItem(str(resultados[1])))
            self.tablaSecreta.setItem(0, 2, QTableWidgetItem(str(resultados[2])))
            self.textoETA.setText("ETA 4")
            self.entradaUmbral.setText(str(umbral))

        elif iter4_text == "_":
            print("Iteracion 4")
            bias = self.entradaBias.text()
            x1 = self.entradaX1.text()
            x2 = self.entradaX2.text()
            y = self.entradaY.text()
            w0 = self.entradaW0.text()
            eta = self.entradaETA.text()
            umbral = self.entradaUmbral.text()

            bias = bias.replace(' ', '')
            bias = bias.split(",")

            x1 = x1.replace(' ', '')
            x1 = x1.split(",")

            x2 = x2.replace(' ', '')
            x2 = x2.split(",")

            y = y.replace(' ', '')
            y = y.split(",")

            if w0 == "RANDOM":
                valorR1 = format(random.random(), '.4f')
                valorR2 = format(random.random(), '.4f')
                valorR3 = format(random.random(), '.4f')
                w0 = [valorR1, valorR2, valorR3]
            else:
                w0 = w0.replace(' ', '')
                w0 = w0.split(",")

            if eta == "RANDOM":
                eta = format(random.random(), '.4f')

            if umbral == "RANDOM":
                umbral = format(random.random(), '.4f')

            self.tablaResultados.setItem(1, 3, QTableWidgetItem(str(w0)))

            resultados = entrenamiento.asignarDatos(w0, eta, umbral, bias, x1, x2, y)

            self.tablaResultados.setItem(0, 3, QTableWidgetItem(str(resultados[0])))
            self.tablaResultados.setItem(2, 3, QTableWidgetItem(str(resultados[1])))
            self.tablaSecreta.setItem(0, 3, QTableWidgetItem(str(resultados[2])))
            self.textoETA.setText("ETA 5")
            self.entradaUmbral.setText(str(umbral))

        elif iter5_text == "_":
            print("Iteracion 5")
            bias = self.entradaBias.text()
            x1 = self.entradaX1.text()
            x2 = self.entradaX2.text()
            y = self.entradaY.text()
            w0 = self.entradaW0.text()
            eta = self.entradaETA.text()
            umbral = self.entradaUmbral.text()

            bias = bias.replace(' ', '')
            bias = bias.split(",")

            x1 = x1.replace(' ', '')
            x1 = x1.split(",")

            x2 = x2.replace(' ', '')
            x2 = x2.split(",")

            y = y.replace(' ', '')
            y = y.split(",")

            if w0 == "RANDOM":
                valorR1 = format(random.random(), '.4f')
                valorR2 = format(random.random(), '.4f')
                valorR3 = format(random.random(), '.4f')
                w0 = [valorR1, valorR2, valorR3]
            else:
                w0 = w0.replace(' ', '')
                w0 = w0.split(",")

            if eta == "RANDOM":
                eta = format(random.random(), '.4f')

            if umbral == "RANDOM":
                umbral = format(random.random(), '.4f')

            self.tablaResultados.setItem(1, 4, QTableWidgetItem(str(w0)))

            resultados = entrenamiento.asignarDatos(w0, eta, umbral, bias, x1, x2, y)

            self.tablaResultados.setItem(0, 4, QTableWidgetItem(str(resultados[0])))
            self.tablaResultados.setItem(2, 4, QTableWidgetItem(str(resultados[1])))
            self.tablaSecreta.setItem(0, 4, QTableWidgetItem(str(resultados[2])))
            self.textoETA.setText("ETA")
            self.entradaUmbral.setText(str(umbral))
            self.botonEjecutar.setText("Finalizar")

        else:
            print("Se acabo")
            self.textoBias.setHidden(True)
            self.entradaBias.setHidden(True)
            self.textoX1.setHidden(True)
            self.entradaX1.setHidden(True)
            self.textoX2.setHidden(True)
            self.entradaX2.setHidden(True)
            self.textoY.setHidden(True)
            self.entradaY.setHidden(True)
            self.textoW0.setHidden(True)
            self.entradaW0.setHidden(True)
            self.textoETA.setHidden(True)
            self.entradaETA.setHidden(True)
            self.textoUmbral.setHidden(True)
            self.entradaUmbral.setHidden(True)
            self.botonEjecutar.setHidden(True)
            self.botonOtraVez.setHidden(False)
            curva1 = self.tablaSecreta.item(0, 0)
            curva1_text = curva1.text()
            curva2 = self.tablaSecreta.item(0, 1)
            curva2_text = curva2.text()
            curva3 = self.tablaSecreta.item(0, 2)
            curva3_text = curva3.text()
            curva4 = self.tablaSecreta.item(0, 3)
            curva4_text = curva4.text()
            curva5 = self.tablaSecreta.item(0, 4)
            curva5_text = curva5.text()
            listaCurvas = [curva1_text, curva2_text, curva3_text, curva4_text, curva5_text]
            graficarCincoCurvas(listaCurvas)

    def OtraVez(self):
        sys.exit()


def graficarCincoCurvas(lista):
    l = []
    for i in lista:
        df = pd.DataFrame(eval(i))
        mostrarGrafica = {
            "iter": df.index.values,
            "eta": df["eta"][0],
            "magErr": df["magErr"],
        }
        l.append(mostrarGrafica)

    df = pd.DataFrame(l)
    print(df)
    plt.figure(figsize=[6, 6])
    plt.plot(df["iter"][0], df["magErr"][0], label="ETA 1: " + str(df["eta"][0]))
    plt.plot(df["iter"][1], df["magErr"][1], label="ETA 2: " + str(df["eta"][1]))
    plt.plot(df["iter"][2], df["magErr"][2], label="ETA 3: " + str(df["eta"][2]))
    plt.plot(df["iter"][3], df["magErr"][3], label="ETA 4: " + str(df["eta"][3]))
    plt.plot(df["iter"][4], df["magErr"][4], label="ETA 5: " + str(df["eta"][4]))
    plt.xlabel('Iteraciones')
    plt.ylabel('Magnitud del Error')
    plt.title('Grafica de las Cinco Curvas de Error')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = index()
    GUI.show()
    sys.exit(app.exec_())
