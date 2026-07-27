from PyQt5.QtWidgets import QDialog, QMessageBox, QGraphicsScene
from PyQt5.uic import loadUi
from PyQt5.QtGui import QBrush, QPen
from PyQt5.QtCore import Qt

from estructuras.no_lineales.arbol_expresion import ArbolExpresion


class LoadArbolExpresion(QDialog):

    def __init__(self):
        super().__init__()

        loadUi("ui/arbol_expresion.ui", self)

        self.scene = QGraphicsScene()
        self.graphicsView.setScene(self.scene)

        self.arbol = ArbolExpresion()

        self.btnConstruir.clicked.connect(self.construir_arbol)
        self.btnLimpiar.clicked.connect(self.limpiar)
        self.btnCerrar.clicked.connect(self.close)


    def construir_arbol(self):

        expresion = self.txtExpresion.text().strip()

        if expresion == "":
            QMessageBox.warning(
                self,
                "Error",
                "Ingrese una expresión postfija."
            )
            return


        construido = self.arbol.build_expression_tree(expresion)


        if not construido:
            QMessageBox.warning(
                self,
                "Error",
                "La expresión es inválida."
            )
            return


        self.txtInorden.setPlainText(
            self.arbol.inorder()
        )

        self.txtPreorden.setPlainText(
            self.arbol.preorder()
        )

        self.txtPostorden.setPlainText(
            self.arbol.postorder()
        )


        self.scene.clear()


        raiz = self.arbol.get_root()


        if raiz:
            self.dibujar_arbol(
                raiz,
                350,
                40,
                160
            )


    def limpiar(self):

        self.txtExpresion.clear()

        self.txtInorden.clear()
        self.txtPreorden.clear()
        self.txtPostorden.clear()

        self.scene.clear()

        self.txtExpresion.setFocus()



    def dibujar_arbol(self, nodo, x, y, espacio):

        if nodo is None:
            return


        radio = 20


        self.scene.addEllipse(
            x,
            y,
            radio * 2,
            radio * 2,
            QPen(Qt.black),
            QBrush(Qt.white)
        )


        texto = self.scene.addText(
            str(nodo.value)
        )

        texto.setPos(
            x + 12,
            y + 7
        )


        if nodo.left:

            self.scene.addLine(
                x + radio,
                y + radio * 2,
                x - espacio + radio,
                y + 80,
                QPen(Qt.black)
            )


            self.dibujar_arbol(
                nodo.left,
                x - espacio,
                y + 80,
                espacio // 2
            )


        if nodo.right:

            self.scene.addLine(
                x + radio,
                y + radio * 2,
                x + espacio + radio,
                y + 80,
                QPen(Qt.black)
            )


            self.dibujar_arbol(
                nodo.right,
                x + espacio,
                y + 80,
                espacio // 2
            )