from estructuras.lineales.queue import Queue


class MenuQueue(object):

    def __init__(self):
        self.queue = Queue()

    def mostrar_menu(self):
        print("\n===== MENU COLA =====")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Primer elemento")
        print("4. Último elemento")
        print("5. Imprimir cola")
        print("6. Salir")

    def ejecutar_opcion(self):

        while True:

            self.mostrar_menu()

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                dato = input("Ingrese el dato: ")
                self.queue.enqueue(dato)
                print("Dato agregado correctamente.")

            elif opcion == "2":
                dato = self.queue.dequeue()

                if dato is None:
                    print("La cola está vacía.")
                else:
                    print("Dato eliminado:", dato)

            elif opcion == "3":
                dato = self.queue.firstQueue()

                if dato is None:
                    print("La cola está vacía.")
                else:
                    print("Primer elemento:", dato)

            elif opcion == "4":
                dato = self.queue.lastQueue()

                if dato is None:
                    print("La cola está vacía.")
                else:
                    print("Último elemento:", dato)

            elif opcion == "5":
                print(self.queue.printQueue())

            elif opcion == "6":
                print("Saliendo...")
                break

            else:
                print("Opción inválida.")