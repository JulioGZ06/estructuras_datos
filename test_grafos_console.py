from estructuras.no_lineales.grafos import Graph


def test_graph():
    graph = Graph()

    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")

    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "D")

    print("Vértices:")
    print(graph.get_vertices())

    print("\nLista de adyacencia:")
    for vertex, adjacent_vertices in graph.get_adjacency_list().items():
        adjacent_text = ", ".join(adjacent_vertices) if adjacent_vertices else "Sin conexiones"
        print(f"{vertex}: {adjacent_text}")

    print("\nMatriz de adyacencia:")
    vertices, matrix = graph.get_adjacency_matrix()

    print("   " + " ".join(vertices))
    for index, row in enumerate(matrix):
        values = " ".join(str(value) for value in row)
        print(f"{vertices[index]}  {values}")

    print("\nLista de arcos:")
    for vertex1, vertex2 in graph.get_edges():
        print(f"({vertex1}, {vertex2})")


if __name__ == "__main__":
    test_graph()