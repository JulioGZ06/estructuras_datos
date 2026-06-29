from estructuras.lineales.nodo import Node


class Stack(object):
    def __init__(self):
        self.top = None
        
    def is_empty(self):
        return self.top is None

    # Inserta un elemento
    def push(self, data):
        new_node = Node(data)

        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    # Elimina un elemento
    # Retorna el valor eliminado
    def pop(self):
        if self.top is None:
            return None

        dato = self.top.data
        self.top = self.top.next

        return dato

    # Retorna el valor del nodo en el tope
    def top_of_stack(self):
        if self.top is None:
            return None

        return self.top.data

    # Muestra el contenido de la pila
    def print_stack(self):
        aux = self.top
        resultado = "TOPE\n↓\n"

        while aux is not None:
            resultado += str(aux.data) + "\n"
            aux = aux.next

        return resultado