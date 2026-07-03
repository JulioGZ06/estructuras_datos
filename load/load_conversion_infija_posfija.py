from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from estructuras.aplicacion.conversion_infija_posfija import ConversionInfijaPosfija


class MenuConversionInfijaPosfija(QDialog):

    def __init__(self):
        super().__init__()

        loadUi("ui/conversion_infija-posfija.ui", self)

        # Objeto que realiza la conversión
        self.conversion = ConversionInfijaPosfija()

        # Evento del botón Calcular
        self.btn_calcular.clicked.connect(self.calcular)

        # Evento del botón Evaluar
        self.btn_evaluar.clicked.connect(self.evaluar)

    def calcular(self):

        expresion = self.txt_expresion.text().strip()

        if expresion == "":
            self.lbl_resultado.setText("Ingrese una expresión")
            return

        posfija = self.conversion.convertir(expresion)

        self.lbl_resultado.setText(posfija)

        # Limpia el resultado anterior
        self.lbl_evaluacion.setText("")

    def evaluar(self):

        posfija = self.lbl_resultado.text()

        if posfija == "" or posfija == "Ingrese una expresión":
            self.lbl_evaluacion.setText("No hay expresión para evaluar")
            return

        resultado = self.conversion.evaluar_posfija(posfija)

        self.lbl_evaluacion.setText(str(resultado))