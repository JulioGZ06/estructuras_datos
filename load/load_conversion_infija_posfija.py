from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from estructuras.aplicacion.conversion_infija_posfija import ConversionInfijaPosfija


class MenuConversionInfijaPosfija(QDialog):

    def __init__(self):
        super().__init__()

        loadUi("ui/conversion_infija-posfija.ui", self)

        # Objeto que realiza la conversión
        self.conversion = ConversionInfijaPosfija()

        # Evento del botón
        self.btn_calcular.clicked.connect(self.calcular)

    def calcular(self):

        expresion = self.txt_expresion.text().strip()

        if expresion == "":
            self.lbl_resultado.setText("Ingrese una expresión")
            return

        resultado = self.conversion.convertir(expresion)

        self.lbl_resultado.setText(resultado)