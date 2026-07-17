from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from estructuras.aplicacion.gestor_impresion import GestorImpresion


class MenuImpresion(QDialog):

    def __init__(self):
        super().__init__()

        loadUi("ui/impresion.ui", self)

        self.gestor = GestorImpresion()

        self.btn_agregar.clicked.connect(self.agregar)
        self.btn_imprimir.clicked.connect(self.imprimir)
        self.btn_frente.clicked.connect(self.consultarFrente)

    def agregar(self):

        usuario = self.txt_usuario.text()
        documento = self.txt_documento.text()
        paginas = self.txt_paginas.text()

        if usuario == "" or documento == "" or paginas == "":
            self.lbl_mensaje.setText("Complete todos los campos.")
            return

        if int(paginas) < 1:
            self.lbl_mensaje.setText("Las páginas deben ser mayores que 0.")
            return

        self.gestor.agregarTrabajo(usuario, documento, int(paginas))

        self.txt_usuario.clear()
        self.txt_documento.clear()
        self.txt_paginas.clear()

        self.actualizar()

    def imprimir(self):

        if self.gestor.estaVacia():
            self.lbl_mensaje.setText("La cola está vacía.")
            return

        trabajo = self.gestor.imprimirSiguiente()

        self.lbl_mensaje.setText(
            f"Se imprimió: {trabajo.documento}"
        )

        self.actualizar()

    def consultarFrente(self):

        if self.gestor.estaVacia():
            self.lbl_frente.setText("Frente: Ninguno")
            return

        trabajo = self.gestor.consultarFrente()

        self.lbl_frente.setText(
            f"Frente: {trabajo.documento}"
        )

    def actualizar(self):

        self.txt_cola.setPlainText(
            self.gestor.mostrarCola()
        )

        self.lbl_total.setText(
            f"Trabajos pendientes: {self.gestor.totalTrabajos()}"
        )

        self.consultarFrente()