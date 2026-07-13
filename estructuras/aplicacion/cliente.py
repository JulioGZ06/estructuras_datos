from datetime import datetime


class Cliente:

    def __init__(self, turno):
        self.turno = turno
        self.hora_entrada = datetime.now()

    def __str__(self):
        return (
            f"Turno: {self.turno}\n"
            f"Hora del turno: {self.hora_entrada.strftime('%H:%M:%S')}"
        )