from estructuras.lineales.pila import Stack
from estructuras.no_lineales.node_expression import NodeExpression


class ExpressionTree:

    def __init__(self):
        self.root = None

    def build_expression_tree(self, expression):

        stack = Stack()

        tokens = expression.split()

        for token in tokens:

            if token.isdigit():

                node = NodeExpression(token)
                stack.push(node)

            elif token in ['+', '-', '*', '/', '$']:

                if stack.is_empty():
                    print("Expresión inválida")
                    return

                right = stack.pop()

                if stack.is_empty():
                    print("Expresión inválida")
                    return

                left = stack.pop()

                operator = NodeExpression(token)

                operator.left = left
                operator.right = right

                stack.push(operator)

            else:
                print("Token inválido:", token)
                return

        if stack.is_empty():
            print("No se pudo construir el árbol")
            return

        self.root = stack.pop()

        if not stack.is_empty():
            print("Expresión inválida")
            self.root = None

    def inorder(self):
        return self._inorder(self.root)

    def _inorder(self, node):

        if node is None:
            return ""

        if node.left is None and node.right is None:
            return str(node.value)

        return "(" + self._inorder(node.left) + " " + str(node.value) + " " + self._inorder(node.right) + ")"

    def preorder(self):
        return self._preorder(self.root)

    def _preorder(self, node):

        if node is None:
            return ""

        resultado = str(node.value)

        izquierdo = self._preorder(node.left)
        derecho = self._preorder(node.right)

        if izquierdo:
            resultado += " " + izquierdo

        if derecho:
            resultado += " " + derecho

        return resultado

    def postorder(self):
        return self._postorder(self.root)

    def _postorder(self, node):

        if node is None:
            return ""

        resultado = ""

        izquierdo = self._postorder(node.left)
        derecho = self._postorder(node.right)

        if izquierdo:
            resultado += izquierdo + " "

        if derecho:
            resultado += derecho + " "

        resultado += str(node.value)

        return resultado