from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic

from load.load_lista_enlazada_simple import MenuListaEnlazada
from load.load_pila import MenuPila
from load.load_conversion_infija_posfija import MenuConversionInfijaPosfija   


class MenuPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi("ui/menu_principal.ui", self)

        self.actionLista_Enlazada.triggered.connect(
            self.abrir_lista_enlazada
        )

        self.actionPila.triggered.connect(
            self.abrir_pila
        )

        self.actionConversion_Infija_Posfija.triggered.connect(
            self.abrir_conversion
        )

        self.action5_Salir.triggered.connect(
            self.close
        )

    def abrir_lista_enlazada(self):
        self.ventana_lista = MenuListaEnlazada()
        self.ventana_lista.show()

    def abrir_pila(self):
        self.ventana_pila = MenuPila()
        self.ventana_pila.show()

    def abrir_conversion(self):
        self.ventana_conversion = MenuConversionInfijaPosfija()
        self.ventana_conversion.show()