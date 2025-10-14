import os
from datetime import datetime, timedelta
from modelos.actividad import Actividad
from typing import Dict, Iterator

# Rutas de datos
_RUTA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "datos")
_RUTA_ARCHIVO = os.path.join(_RUTA_DIR, "actividades.csv")

class GestorActividades:
    """Gestor que opera directamente sobre archivo (CSV) sin usar estructuras en memoria."""

    def __init__(self):
        self.actividades: Dict[int, Actividad] = {}
        self.cargar_actividades()

    def asegurar_archivo(self):
        os.makedirs(_RUTA_DIR, exist_ok=True)
        if not os.path.exists(_RUTA_ARCHIVO):
            with open(_RUTA_ARCHIVO, "w", encoding="utf-8"):
                pass  # crea archivo vacío

    def cargar_actividades(self) -> None:
        try:
            with open('datos/actividades.csv', 'r', encoding='utf-8') as f:
                for linea in f:
                    if linea.strip():
                        actividad = Actividad.desde_csv(linea)
                        self.actividades[actividad.id] = actividad
        except FileNotFoundError:
            pass

    def guardar_actividades(self) -> None:
        with open('datos/actividades.csv', 'w', encoding='utf-8') as f:
            for actividad in self.actividades.values():
                f.write(actividad.a_csv() + '\n')

    def _siguiente_id(self):
        """Obtiene el siguiente ID escaneando el archivo (sin listas)."""
        self.asegurar_archivo()
        ultimo = 0
        with open(_RUTA_ARCHIVO, "r", encoding="utf-8") as f:
            for linea in f:
                act = Actividad.desde_csv(linea)
                if act and act.id > ultimo:
                    ultimo = act.id
        return ultimo + 1

    def agregar(self, tipo, nombre, fecha, hora, responsable):
        """Valida y agrega una actividad al final del archivo."""
        try:
            dt = datetime.strptime(f"{fecha} {hora}", "%Y-%m-%d %H:%M")
        except ValueError:
            return False, "Fecha u hora inválidas. Formatos: AAAA-MM-DD y HH:MM (24h)."

        if not nombre.strip():
            return False, "El nombre no puede estar vacío."
        if not responsable.strip():
            return False, "El responsable no puede estar vacío."
        if not tipo.strip():
            tipo = "Entrenamiento"

        nuevo_id = self._siguiente_id()
        act = Actividad(
            nuevo_id, tipo.strip(), nombre.strip(),
            dt,  # Pasar el objeto datetime directamente
            responsable.strip(), "Pendiente"
        )
        with open(_RUTA_ARCHIVO, "a", encoding="utf-8") as f:
            f.write(act.a_csv() + "\n")
        return True, f"Actividad #{nuevo_id} guardada."

    def leer_todo(self) -> Iterator[str]:
        return (act.a_csv() for act in sorted(
            self.actividades.values(), 
            key=lambda x: x.fecha_hora
        ))

    def _reescribir_transformando(self, transformador):
        """Reescribe archivo aplicando una transformación línea a línea."""
        self.asegurar_archivo()
        tmp = _RUTA_ARCHIVO + ".tmp"
        hubo_cambio = False
        with open(_RUTA_ARCHIVO, "r", encoding="utf-8") as fin, open(tmp, "w", encoding="utf-8") as fout:
            for linea in fin:
                nueva_linea, mod = transformador(linea)
                if nueva_linea is not None and nueva_linea != "":
                    fout.write(nueva_linea)
                if mod:
                    hubo_cambio = True
        os.replace(tmp, _RUTA_ARCHIVO)
        return hubo_cambio

    def marcar_completada(self, idn: int):
        def _t(linea):
            act = Actividad.desde_csv(linea)
            if not act:
                return (linea, False)
            if act.id == idn:
                act.estado = "Completada"
                return (act.a_csv() + "\n", True)
            return (linea, False)
        return self._reescribir_transformando(_t)

    def eliminar(self, idn: int):
        if idn in self.actividades:
            del self.actividades[idn]
            self.guardar_actividades()
            return True
        return False

    def alertas_24h(self):
        """Generador de alertas para actividades en próximas 24h (no completadas)."""
        ahora = datetime.now()
        limite = ahora + timedelta(hours=24)
        self.asegurar_archivo()
        with open(_RUTA_ARCHIVO, "r", encoding="utf-8") as f:
            for linea in f:
                act = Actividad.desde_csv(linea)
                if not act or act.estado == "Completada":
                    continue
                try:
                    dt = datetime.strptime(act.fecha_hora, "%Y-%m-%d %H:%M")
                except ValueError:
                    continue
                if ahora <= dt <= limite:
                    yield f"#{act.id:03d} {act.tipo} - {act.nombre} | {act.fecha_hora} | Resp: {act.responsable}"
