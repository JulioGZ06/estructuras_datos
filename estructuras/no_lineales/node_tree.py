
class NodeTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insertar(self, value):
        self.root = self._insertar(self.root, value)

    def _insertar(self, node, value):
        if node is None:
            return NodeTree(value)
        
        if value < node.value:
            node.left = self._insertar(node.left, value)
        elif value > node.value:
            node.right = self._insertar(node.right, value)
        else:
            print(f"El valor {value} ya existe en el árbol.")
            
        return node

    def buscar(self, value):
        return self._buscar(self.root, value)

    def _buscar(self, node, value):
        if node is None:
            return False
        if value == node.value:
            return True
        if value < node.value:
            return self._buscar(node.left, value)
        return self._buscar(node.right, value)

    def preorden(self):
        self._preorden(self.root)
        print()

    def _preorden(self, node):
        if node is not None:
            print(node.value, end=" ")
            self._preorden(node.left)
            self._preorden(node.right)

    def inorden(self):
        self._inorden(self.root)
        print()

    def _inorden(self, node):
        if node is not None:
            self._inorden(node.left)
            print(node.value, end=" ")
            self._inorden(node.right)

    def posorden(self):
        self._posorden(self.root)
        print()

    def _posorden(self, node):
        if node is not None:
            self._posorden(node.left)
            self._posorden(node.right)
            print(node.value, end=" ")
            
    def contar(self):
        return self._contar(self.root)

    def _contar(self, node):
        if node is None:
            return 0
        return 1 + self._contar(node.left) + self._contar(node.right)
#Ese método funciona con recursión: el primero (contar) 
# es solo una fachada para que el menú no toque la raíz,
# y el segundo (_contar) hace la chamba pesada dividiendo el problema. 
# Su lógica es que si llega a una rama vacía (None), no suma nada y regresa un 0,
# pero si encuentra un nodo real, se apunta un 1 por estar parado ahí y 
# le suma lo que encuentre al mandar a llamar a la misma función para que revise
# todo el lado izquierdo y luego todo el lado derecho. Al final, cuando todas las ramas terminan 
# de contar sus propios nodos hacia abajo, los resultados van rebotando hacia arriba y se van 
# sumando en cadena hasta entregarle al menú el total exacto de bolitas que tiene el árbol.