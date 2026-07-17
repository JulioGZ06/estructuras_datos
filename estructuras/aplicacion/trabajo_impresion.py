class TrabajoImpresion:

    def __init__(self, usuario, documento, paginas, consecutivo):
        self.usuario = usuario
        self.documento = documento
        self.paginas = paginas
        self.consecutivo = consecutivo

    def __str__(self):
        return (f"{self.consecutivo}. "
                f"{self.usuario} - "
                f"{self.documento} "
                f"({self.paginas} páginas)")