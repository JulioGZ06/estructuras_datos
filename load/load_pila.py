from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi

from estructuras.lineales.pila import Stack


class MenuPila(QDialog):
    def __init__(self):
        super().__init__()

        loadUi("ui/pila.ui", self)

        self.pila = Stack()

        self.btn_push.clicked.connect(self.push)
        self.btn_pop.clicked.connect(self.pop)
        self.btn_top.clicked.connect(self.top)
        self.btn_print.clicked.connect(self.imprimir)

    def push(self):
        dato = self.txt_dato.text().strip()

        if dato == "":
            QMessageBox.warning(self, "Error", "Ingrese un dato")
            return

        self.pila.push(dato)
        self.txt_dato.clear()
        self.imprimir()

    def pop(self):
        dato = self.pila.pop()

        if dato is None:
            QMessageBox.warning(self, "Error", "La pila está vacía")
            return

        QMessageBox.information(
            self,
            "Pop",
            f"Elemento eliminado: {dato}"
        )

        self.imprimir()

    def top(self):
        dato = self.pila.top_of_stack()

        if dato is None:
            QMessageBox.warning(self, "Error", "La pila está vacía")
            return

        QMessageBox.information(
            self,
            "Top",
            f"Tope: {dato}"
        )

    def imprimir(self):
        self.lbl_resultado.setText(
            self.pila.print_stack()
        )