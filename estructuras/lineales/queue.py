from estructuras.lineales.nodo import Node


class Queue(object):

    def __init__(self):
        self.first = None
        self.last = None

    def isEmpty(self):
        return self.first is None

    # Agrega un elemento al final
    def enqueue(self, valor):

        nuevo = Node(valor)

        if self.isEmpty():
            self.first = nuevo
            self.last = nuevo
        else:
            self.last.next = nuevo
            self.last = nuevo

    # Elimina el primer elemento
    def dequeue(self):

        if self.isEmpty():
            return None

        dato = self.first.data
        self.first = self.first.next

        if self.first is None:
            self.last = None

        return dato

    # Devuelve el primer elemento
    def firstQueue(self):

        if self.isEmpty():
            return None

        return self.first.data

    # Devuelve el último elemento
    def lastQueue(self):

        if self.isEmpty():
            return None

        return self.last.data

    # Muestra toda la cola
    def printQueue(self):

        if self.isEmpty():
            return "La cola está vacía"

        aux = self.first
        resultado = "FRENTE\n↓\n"

        while aux is not None:
            resultado += str(aux.data)

            if aux.next is not None:
                resultado += "\n"

            aux = aux.next

        resultado += "\n↑\nFINAL"

        return resultado
    def size(self):
        contador = 0
        aux = self.first

        while aux is not None:
            contador += 1
            aux = aux.next

        return contador