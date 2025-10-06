import customtkinter as ctk
from servicios.gestor_actividades import GestorActividades

class VistaAgregarActividad(ctk.CTkToplevel):
    def __init__(self, padre):
        super().__init__(padre)
        self.title("Agregar Actividad")
        self.geometry("500x500")

        self.gestor = GestorActividades()

        marco = ctk.CTkFrame(self)
        marco.pack(padx=10, pady=10, fill="both", expand=True)

        ctk.CTkLabel(marco, text="Tipo (Entrenamiento/Partido/Reunión):").pack(pady=5)
        self.campo_tipo = ctk.CTkEntry(marco, placeholder_text="Entrenamiento")
        self.campo_tipo.pack(pady=3, fill="x", padx=10)

        ctk.CTkLabel(marco, text="Nombre:").pack(pady=5)
        self.campo_nombre = ctk.CTkEntry(marco, placeholder_text="Ej. Sesión táctica")
        self.campo_nombre.pack(pady=3, fill="x", padx=10)

        ctk.CTkLabel(marco, text="Fecha (AAAA-MM-DD):").pack(pady=5)
        self.campo_fecha = ctk.CTkEntry(marco, placeholder_text="2025-09-12")
        self.campo_fecha.pack(pady=3, fill="x", padx=10)

        ctk.CTkLabel(marco, text="Hora (HH:MM 24h):").pack(pady=5)
        self.campo_hora = ctk.CTkEntry(marco, placeholder_text="18:00")
        self.campo_hora.pack(pady=3, fill="x", padx=10)

        ctk.CTkLabel(marco, text="Responsable:").pack(pady=5)
        self.campo_responsable = ctk.CTkEntry(marco, placeholder_text="Nombre del responsable")
        self.campo_responsable.pack(pady=3, fill="x", padx=10)

        ctk.CTkButton(marco, text="Guardar", command=self.guardar).pack(pady=12)

    def guardar(self):
        tipo = (self.campo_tipo.get() or "Entrenamiento").strip()
        nombre = self.campo_nombre.get().strip()
        fecha = self.campo_fecha.get().strip()
        hora = self.campo_hora.get().strip()
        responsable = self.campo_responsable.get().strip()

        ok, msg = self.gestor.agregar(tipo, nombre, fecha, hora, responsable)
        self._mensaje(msg)
        if ok:
            self.destroy()

    def _mensaje(self, msj):
        dlg = ctk.CTkToplevel(self)
        dlg.title("Mensaje")
        ctk.CTkLabel(dlg, text=msj).pack(padx=20, pady=15)
        ctk.CTkButton(dlg, text="Cerrar", command=dlg.destroy).pack(pady=10)

