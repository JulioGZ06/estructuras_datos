from estructuras.lineales.pila import Stack


class ConversionInfijaPosfija:

    def __init__(self):
        self.pila = Stack()

    # Regresa la prioridad de los operadores
    def prioridad(self, operador):
        if operador == "$":
            return 3
        elif operador == "*" or operador == "/":
            return 2
        elif operador == "+" or operador == "-":
            return 1
        return 0

    # Verifica si el caracter es un operador
    def es_operador(self, caracter):
        return caracter in "+-*/$"

    # Convierte una expresión infija a posfija
    def convertir(self, expresion):

        resultado = ""

        for caracter in expresion:

            # Ignora espacios
            if caracter == " ":
                continue

            # Si es un operando, lo agrega al resultado
            if caracter.isalnum():
                resultado += caracter

            # Si es un paréntesis izquierdo
            elif caracter == "(":
                self.pila.push(caracter)

            # Si es un paréntesis derecho
            elif caracter == ")":

                while (not self.pila.is_empty() and
                       self.pila.top_of_stack() != "("):
                    resultado += self.pila.pop()

                if not self.pila.is_empty():
                    self.pila.pop()

            # Si es un operador
            elif self.es_operador(caracter):

                while (not self.pila.is_empty() and
                       self.pila.top_of_stack() != "(" and
                       self.prioridad(self.pila.top_of_stack()) >= self.prioridad(caracter)):
                    resultado += self.pila.pop()

                self.pila.push(caracter)

        # Vacía la pila
        while not self.pila.is_empty():
            resultado += self.pila.pop()

        return resultado
        # Evalúa una expresión posfija
    def evaluar_posfija(self, expresion):

        # Vaciar la pila por si contiene datos anteriores
        while not self.pila.is_empty():
            self.pila.pop()

        for caracter in expresion:

            # Ignorar espacios
            if caracter == " ":
                continue

            # Si es un número
            if caracter.isdigit():
                self.pila.push(int(caracter))

            # Si es un operador
            elif self.es_operador(caracter):

                operador2 = self.pila.pop()
                operador1 = self.pila.pop()

                if caracter == "+":
                    resultado = operador1 + operador2

                elif caracter == "-":
                    resultado = operador1 - operador2

                elif caracter == "*":
                    resultado = operador1 * operador2

                elif caracter == "/":
                    resultado = operador1 / operador2

                elif caracter == "$":
                    resultado = operador1 ** operador2

                self.pila.push(resultado)

        return self.pila.pop()