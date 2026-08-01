from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic

from load.load_lista_enlazada_simple import MenuListaEnlazada
from load.load_pila import MenuPila
from load.load_conversion_infija_posfija import MenuConversionInfijaPosfija 
from load.load_queue import MenuQueue  
from load.load_banco import MenuBanco
from load.load_impresion import MenuImpresion
from load.load_arbol_expresion import LoadArbolExpresion
from load.load_grafos import LoadGrafos

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
        
        self.actionQueue.triggered.connect(
            self.abrir_queue
        )
        
        self.actionBanco.triggered.connect(
            self.abrir_banco
        )
        
        self.actionCola_Impresion.triggered.connect(
            self.abrir_impresion
       )
        
        self.actionArbol_expresion.triggered.connect(self.abrir_arbol_expresion)

        self.actionGrafos.triggered.connect(self.abrir_grafos)

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
        
    def abrir_queue(self):
        self.ventana_queue = MenuQueue()
        self.ventana_queue.show()
        
    def abrir_banco(self):
        self.ventana_banco = MenuBanco()
        self.ventana_banco.show()
        
    def abrir_impresion(self):
        self.ventana_impresion = MenuImpresion()
        self.ventana_impresion.show()
        
    def abrir_arbol_expresion(self):

        ventana = LoadArbolExpresion()
        ventana.exec_()

    def abrir_grafos(self):
        self.ventana_grafos = LoadGrafos()
        self.ventana_grafos.show()