from estructuras.lineales.pila import Stack
from estructuras.no_lineales.node_expression import NodeExpression


class ArbolExpresion:

    def __init__(self):
        self.root = None

    def build_expression_tree(self, expression):

        self.root = None

        stack = Stack()

        tokens = expression.split()

        if len(tokens) == 0:
            return False

        for token in tokens:

            if token.isdigit():

                node = NodeExpression(token)
                stack.push(node)

            elif token in ['+', '-', '*', '/', '$']:

                if stack.is_empty():
                    return False

                right = stack.pop()

                if stack.is_empty():
                    return False

                left = stack.pop()

                operator = NodeExpression(token)

                operator.left = left
                operator.right = right

                stack.push(operator)

            else:
                return False

        if stack.is_empty():
            return False

        self.root = stack.pop()

        if not stack.is_empty():
            self.root = None
            return False

        return True

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

        if izquierdo != "":
            resultado += " " + izquierdo

        if derecho != "":
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

        if izquierdo != "":
            resultado += izquierdo + " "

        if derecho != "":
            resultado += derecho + " "

        resultado += str(node.value)

        return resultado

    def get_root(self):
        return self.root