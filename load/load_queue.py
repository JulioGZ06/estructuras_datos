from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi

from estructuras.lineales.queue import Queue


class MenuQueue(QDialog):

    def __init__(self):
        super().__init__()

        loadUi("ui/Queue.ui", self)

        self.queue = Queue()

        self.btn_enqueue.clicked.connect(self.enqueue)
        self.btn_dequeue.clicked.connect(self.dequeue)
        self.btn_first.clicked.connect(self.firstQueue)
        self.btn_last.clicked.connect(self.lastQueue)
        self.btn_print.clicked.connect(self.printQueue)

    def enqueue(self):
        dato = self.txt_dato.text()

        if dato == "":
            QMessageBox.warning(self, "Error", "Ingrese un dato")
            return

        self.queue.enqueue(dato)
        self.txt_dato.clear()
        self.printQueue()

    def dequeue(self):
        dato = self.queue.dequeue()

        if dato is None:
            QMessageBox.information(self, "Cola", "La cola está vacía")
        else:
            QMessageBox.information(self, "Dato eliminado", str(dato))

        self.printQueue()

    def firstQueue(self):
        dato = self.queue.firstQueue()

        if dato is None:
            self.lbl_resultado.setText("Cola vacía")
        else:
            self.lbl_resultado.setText("Primer elemento: " + str(dato))

    def lastQueue(self):
        dato = self.queue.lastQueue()

        if dato is None:
            self.lbl_resultado.setText("Cola vacía")
        else:
            self.lbl_resultado.setText("Último elemento: " + str(dato))

    def printQueue(self):
        self.lbl_resultado.setText(self.queue.printQueue())