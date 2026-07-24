from estructuras.no_lineales.expression_tree import ExpressionTree


def main():

    arbol = ExpressionTree()

    expresion = input("Ingrese una expresión postfija: ")

    arbol.build_expression_tree(expresion)

    if arbol.root is None:
        print("No fue posible construir el árbol.")
        return

    print("\n===== RECORRIDOS =====")
    print("Inorden :", arbol.inorder())
    print("Preorden:", arbol.preorder())
    print("Postorden:", arbol.postorder())


if __name__ == "__main__":
    main()