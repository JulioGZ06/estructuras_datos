from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi
from datetime import datetime

from estructuras.lineales.queue import Queue
from estructuras.aplicacion.cliente import Cliente


class MenuBanco(QDialog):

    def __init__(self):
        super().__init__()

        loadUi("ui/banco.ui", self)

        self.queue = Queue()

        self.turno = 1
        self.clientes_atendidos = 0
        self.tiempo_total = 0
        self.banco_cerrado = False

        self.btn_turno.clicked.connect(self.turnoCliente)
        self.btn_atender.clicked.connect(self.atenderCliente)
        self.btn_cerrar.clicked.connect(self.cerrarBanco)

        self.lbl_atender.setText("")
        self.lbl_cerrar.setText("")
        self.plainTextEdit.setPlainText("No hay clientes en espera.")

    def turnoCliente(self):

        if self.banco_cerrado:
            self.lbl_cerrar.setText(
                "El banco está cerrado.\nNo se pueden generar más turnos."
            )
            return

        cliente = Cliente(self.turno)

        self.queue.enqueue(cliente)

        self.turno += 1

        self.printQueue()

    def atenderCliente(self):

        cliente = self.queue.dequeue()

        if cliente is None:

            self.lbl_atender.setText("No hay clientes en espera.")

            if self.banco_cerrado:

                promedio = 0

                if self.clientes_atendidos > 0:
                    promedio = self.tiempo_total / self.clientes_atendidos

                self.lbl_cerrar.setText(
                    f"Banco cerrado\n\n"
                    f"Clientes atendidos: {self.clientes_atendidos}\n"
                    f"Tiempo promedio de espera: {promedio:.2f} segundos"
                )

            self.printQueue()
            return

        hora_salida = datetime.now()

        tiempo = (hora_salida - cliente.hora_entrada).total_seconds()

        self.clientes_atendidos += 1
        self.tiempo_total += tiempo

        self.lbl_atender.setText(
            f"Cliente atendido\n\n"
            f"Turno: {cliente.turno}\n"
            f"Hora de entrada: {cliente.hora_entrada.strftime('%H:%M:%S')}\n"
            f"Hora de salida: {hora_salida.strftime('%H:%M:%S')}\n"
            f"Tiempo de espera: {int(tiempo)} segundos"
        )

        self.printQueue()

        if self.banco_cerrado and self.queue.isEmpty():

            promedio = self.tiempo_total / self.clientes_atendidos

            self.lbl_cerrar.setText(
                f"Banco cerrado\n\n"
                f"Clientes atendidos: {self.clientes_atendidos}\n"
                f"Tiempo promedio de espera: {promedio:.2f} segundos"
            )

    def cerrarBanco(self):

        self.banco_cerrado = True

        self.txt_cliente.setEnabled(False)
        self.btn_turno.setEnabled(False)

        if not self.queue.isEmpty():

            self.lbl_cerrar.setText(
                "Banco cerrado.\n"
                "No se pueden generar más turnos.\n"
                "Atienda a los clientes pendientes."
            )

            return

        promedio = 0

        if self.clientes_atendidos > 0:
            promedio = self.tiempo_total / self.clientes_atendidos

        self.lbl_cerrar.setText(
            f"Banco cerrado\n\n"
            f"Clientes atendidos: {self.clientes_atendidos}\n"
            f"Tiempo promedio de espera: {promedio:.2f} segundos"
        )

    def printQueue(self):

        if self.queue.isEmpty():
            self.plainTextEdit.setPlainText("No hay clientes en espera.")
            return

        texto = ""

        aux = self.queue.first

        while aux is not None:

            texto += (
                f"Turno: {aux.data.turno}\n"
                f"Hora del turno: {aux.data.hora_entrada.strftime('%H:%M:%S')}\n\n"
            )

            aux = aux.next

        self.plainTextEdit.setPlainText(texto)