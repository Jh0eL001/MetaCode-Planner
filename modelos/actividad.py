from dataclasses import dataclass
from datetime import datetime

@dataclass
class Actividad:
    id: int
    tipo: str
    nombre: str
    fecha_hora: datetime  # Ahora esperamos un objeto datetime
    responsable: str
    estado: str = "Pendiente"

    def a_csv(self) -> str:
        fecha_str = self.fecha_hora.strftime("%Y-%m-%d %H:%M")
        return f"{self.id}|{self.tipo}|{self.nombre}|{fecha_str}|{self.responsable}|{self.estado}"

    @classmethod
    def desde_csv(cls, linea: str) -> 'Actividad':
        id, tipo, nombre, fecha_hora, responsable, estado = linea.strip().split('|')
        return cls(
            id=int(id),
            tipo=tipo,
            nombre=nombre,
            fecha_hora=datetime.strptime(fecha_hora, "%Y-%m-%d %H:%M"),
            responsable=responsable,
            estado=estado
        )
