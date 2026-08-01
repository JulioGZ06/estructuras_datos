import math

from PyQt5.QtWidgets import QDialog, QMessageBox, QTableWidgetItem, QAbstractItemView, QGraphicsScene
from PyQt5.uic import loadUi
from PyQt5.QtGui import QBrush, QPen, QPainter
from PyQt5.QtCore import Qt, QRectF, QTimer

from estructuras.no_lineales.grafos import Graph


class LoadGrafos(QDialog):
    def __init__(self):
        super().__init__()

        loadUi("ui/grafos.ui", self)

        self.graph = Graph()
        self.scene = QGraphicsScene(self)
        self.scene.setBackgroundBrush(QBrush(Qt.white))
        self.graphicsViewGraph.setScene(self.scene)
        self.graphicsViewGraph.setRenderHint(QPainter.Antialiasing, True)

        self.btnAddVertex.clicked.connect(self.add_vertex)
        self.btnDeleteVertex.clicked.connect(self.delete_vertex)
        self.btnAddEdge.clicked.connect(self.add_edge)
        self.btnDeleteEdge.clicked.connect(self.delete_edge)
        self.btnRedrawGraph.clicked.connect(self.redraw_graph)
        self.btnClearGraph.clicked.connect(self.clear_graph)

        self.tabWidgetGraph.setCurrentWidget(self.tabVisual)
        self.tabWidgetGraph.setCurrentIndex(0)
        self.graphicsViewGraph.setVisible(True)
        self.btnRedrawGraph.setVisible(True)
        self.btnRedrawGraph.setEnabled(True)
        self.graphicsViewGraph.setMinimumSize(300, 250)

        self.tblAdjacencyMatrix.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tblEdges.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.refresh_ui()
        self._schedule_redraw()

    def showEvent(self, event):
        super().showEvent(event)
        self._schedule_redraw()

    def add_vertex(self):
        vertex = self.txtVertex.text().strip()

        if not vertex:
            QMessageBox.warning(self, "Error", "Ingrese un nombre para el vértice.")
            return

        added = self.graph.add_vertex(vertex)
        if not added:
            QMessageBox.information(self, "Información", "El vértice ya existe.")
        self.txtVertex.clear()
        self.refresh_ui()

    def delete_vertex(self):
        vertex = self.cmbVertex.currentText()

        if not vertex:
            QMessageBox.warning(self, "Error", "No hay vértices para eliminar.")
            return

        self.graph.remove_vertex(vertex)
        self.refresh_ui()

    def add_edge(self):
        vertex1 = self.cmbOrigin.currentText()
        vertex2 = self.cmbDestination.currentText()

        if not vertex1 or not vertex2:
            QMessageBox.warning(self, "Error", "Seleccione dos vértices válidos.")
            return

        if vertex1 == vertex2:
            QMessageBox.warning(self, "Error", "No se permite conectar un vértice consigo mismo.")
            return

        try:
            added = self.graph.add_edge(vertex1, vertex2)
        except ValueError as error:
            QMessageBox.warning(self, "Error", str(error))
            return

        if not added:
            QMessageBox.information(self, "Información", "El arco ya existe.")

        self.refresh_ui()

    def delete_edge(self):
        vertex1 = self.cmbOrigin.currentText()
        vertex2 = self.cmbDestination.currentText()

        if not vertex1 or not vertex2:
            QMessageBox.warning(self, "Error", "Seleccione dos vértices válidos.")
            return

        removed = self.graph.remove_edge(vertex1, vertex2)
        if not removed:
            QMessageBox.information(self, "Información", "El arco no existe.")

        self.refresh_ui()

    def _schedule_redraw(self):
        QTimer.singleShot(0, self.redraw_graph)

    def redraw_graph(self):
        self.scene.clear()
        self.scene.setSceneRect(QRectF(0, 0, 700, 500))

        if self.graph.vertex_count() == 0:
            empty_text = self.scene.addText("Grafo vacío")
            empty_text.setDefaultTextColor(Qt.darkGray)
            empty_text.setPos(300, 220)
            self.graphicsViewGraph.resetTransform()
            self.graphicsViewGraph.setRenderHint(QPainter.Antialiasing, True)
            self.graphicsViewGraph.fitInView(self.scene.sceneRect(), Qt.KeepAspectRatio)
            self.graphicsViewGraph.viewport().update()
            return

        vertices = self.graph.get_vertices()
        positions = self._calculate_positions(vertices)

        edge_pen = QPen(Qt.darkGreen, 2)
        vertex_pen = QPen(Qt.blue, 2)
        vertex_brush = QBrush(Qt.lightGray)

        for edge in self.graph.get_edges():
            vertex1, vertex2 = edge
            x1, y1 = positions[vertex1]
            x2, y2 = positions[vertex2]
            self.scene.addLine(x1 + 20, y1 + 20, x2 + 20, y2 + 20, edge_pen)

        for vertex in vertices:
            x, y = positions[vertex]
            self.scene.addEllipse(x, y, 40, 40, vertex_pen, vertex_brush)
            text_item = self.scene.addText(vertex)
            text_item.setPos(x + 10, y + 10)
            text_item.setDefaultTextColor(Qt.darkBlue)

        self.graphicsViewGraph.resetTransform()
        self.graphicsViewGraph.setRenderHint(QPainter.Antialiasing, True)
        self.graphicsViewGraph.fitInView(self.scene.sceneRect(), Qt.KeepAspectRatio)
        self.graphicsViewGraph.centerOn(self.scene.sceneRect().center())
        self.graphicsViewGraph.ensureVisible(self.scene.sceneRect(), 20, 20)

        self.graphicsViewGraph.viewport().update()

    def _calculate_positions(self, vertices):
        positions = {}

        if len(vertices) == 1:
            positions[vertices[0]] = (330, 220)
            return positions

        center_x = 350
        center_y = 220
        radius = 180 if len(vertices) <= 6 else 240
        angle_step = 360 / len(vertices)

        for index, vertex in enumerate(vertices):
            angle = math.radians(90 - index * angle_step)
            x = center_x + math.cos(angle) * radius - 20
            y = center_y + math.sin(angle) * radius - 20
            positions[vertex] = (x, y)

        return positions

    def clear_graph(self):
        self.scene.clear()
        self.scene.setSceneRect(QRectF(0, 0, 700, 500))

        empty_text = self.scene.addText("Vista limpiada")
        empty_text.setDefaultTextColor(Qt.darkGray)
        empty_text.setPos(300, 220)

        self.graphicsViewGraph.resetTransform()
        self.graphicsViewGraph.setRenderHint(QPainter.Antialiasing, True)
        self.graphicsViewGraph.fitInView(self.scene.sceneRect(), Qt.KeepAspectRatio)
        self.graphicsViewGraph.viewport().update()

    def refresh_ui(self):
        vertices = self.graph.get_vertices()

        self._refresh_comboboxes(vertices)
        self._refresh_status_label()
        self._refresh_adjacency_matrix(vertices)
        self._refresh_adjacency_list(vertices)
        self._refresh_edges_table()
        self.redraw_graph()

    def _refresh_comboboxes(self, vertices):
        current_vertex = self.cmbVertex.currentText()
        current_origin = self.cmbOrigin.currentText()
        current_destination = self.cmbDestination.currentText()

        self.cmbVertex.clear()
        self.cmbOrigin.clear()
        self.cmbDestination.clear()
        self.cmbVertex.addItems(vertices)
        self.cmbOrigin.addItems(vertices)
        self.cmbDestination.addItems(vertices)

        if current_vertex in vertices:
            self.cmbVertex.setCurrentText(current_vertex)
        elif vertices:
            self.cmbVertex.setCurrentIndex(0)

        if current_origin in vertices:
            self.cmbOrigin.setCurrentText(current_origin)
        elif vertices:
            self.cmbOrigin.setCurrentIndex(0)

        if current_destination in vertices:
            self.cmbDestination.setCurrentText(current_destination)
        elif vertices:
            self.cmbDestination.setCurrentIndex(0)

    def _refresh_status_label(self):
        self.lblGraphStatus.setText(
            f"Vértices: {self.graph.vertex_count()} | Arcos: {self.graph.edge_count()}"
        )

    def _refresh_adjacency_matrix(self, vertices):
        self.tblAdjacencyMatrix.setRowCount(len(vertices))
        self.tblAdjacencyMatrix.setColumnCount(len(vertices))
        self.tblAdjacencyMatrix.setHorizontalHeaderLabels(vertices)
        self.tblAdjacencyMatrix.setVerticalHeaderLabels(vertices)

        for row_index, row_vertex in enumerate(vertices):
            for column_index, column_vertex in enumerate(vertices):
                value = 1 if self.graph.contains_edge(row_vertex, column_vertex) else 0
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignCenter)
                self.tblAdjacencyMatrix.setItem(row_index, column_index, item)

        self.tblAdjacencyMatrix.resizeColumnsToContents()

    def _refresh_adjacency_list(self, vertices):
        if not vertices:
            self.txtAdjacencyList.setPlainText("")
            return

        lines = []
        for vertex in vertices:
            adjacent = self.graph.get_adjacent_vertices(vertex)
            lines.append(f"{vertex}: {', '.join(adjacent) if adjacent else '-'}")

        self.txtAdjacencyList.setPlainText("\n".join(lines))

    def _refresh_edges_table(self):
        edges = self.graph.get_edges()
        self.tblEdges.setRowCount(len(edges))
        self.tblEdges.setColumnCount(2)
        self.tblEdges.setHorizontalHeaderLabels(["Vértice 1", "Vértice 2"])

        for row_index, edge in enumerate(edges):
            vertex1, vertex2 = edge
            self.tblEdges.setItem(row_index, 0, QTableWidgetItem(vertex1))
            self.tblEdges.setItem(row_index, 1, QTableWidgetItem(vertex2))

        self.tblEdges.resizeColumnsToContents()
