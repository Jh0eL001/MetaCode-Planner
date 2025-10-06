import customtkinter as ctk
from ui.vista_actividades import VistaActividades
from ui.agregar_actividad import VistaAgregarActividad
from ui.vista_alertas import VistaAlertas

class VentanaPrincipal(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("MetaCode Planner - Planificador Deportivo (Club de Fútbol)")
        self.geometry("900x600")

        marco = ctk.CTkFrame(self)
        marco.pack(pady=20, padx=20, fill="both", expand=True)

        titulo = ctk.CTkLabel(marco, text="Planificador de Actividades del Club", font=("Arial", 22))
        titulo.pack(pady=10)

        ctk.CTkButton(marco, text="Ver Actividades", command=self.abrir_actividades).pack(pady=6)
        ctk.CTkButton(marco, text="Agregar Actividad", command=self.abrir_agregar).pack(pady=6)
        ctk.CTkButton(marco, text="Ver Alertas (24h)", command=self.abrir_alertas).pack(pady=6)

    def abrir_actividades(self):
        VistaActividades(self)

    def abrir_agregar(self):
        VistaAgregarActividad(self)

    def abrir_alertas(self):
        VistaAlertas(self)

