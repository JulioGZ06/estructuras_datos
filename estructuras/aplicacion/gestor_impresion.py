from estructuras.lineales.queue import Queue
from estructuras.aplicacion.trabajo_impresion import TrabajoImpresion


class GestorImpresion:

    def __init__(self):
        self.cola = Queue()
        self.consecutivo = 1

    def agregarTrabajo(self, usuario, documento, paginas):

        trabajo = TrabajoImpresion(
            usuario,
            documento,
            paginas,
            self.consecutivo
        )

        self.cola.enqueue(trabajo)

        self.consecutivo += 1

    def imprimirSiguiente(self):
        return self.cola.dequeue()

    def consultarFrente(self):
        return self.cola.firstQueue()

    def mostrarCola(self):
        return self.cola.printQueue()

    def totalTrabajos(self):
        return self.cola.size()

    def estaVacia(self):
        return self.cola.isEmpty()