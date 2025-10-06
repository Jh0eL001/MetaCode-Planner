class GeneradorReportes:
    def __init__(self, actividades):
        self.actividades = actividades

    def generar_resumen(self):
        total = len(self.actividades)
        pendientes = len([a for a in self.actividades if a.estado == "Pendiente"])
        completadas = total - pendientes
        return f"Total: {total}, Pendientes: {pendientes}, Completadas: {completadas}"
