import customtkinter as ctk
from ui.vista_actividades import VistaActividades
from ui.agregar_actividad import VistaAgregarActividad
from ui.vista_alertas import VistaAlertas

class VentanaPrincipal(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Planificador Deportivo")
        self.geometry("800x600")

        # Marco principal
        self.marco = ctk.CTkFrame(self)
        self.marco.pack(pady=20, padx=20, fill="both", expand=True)

        # Título
        self.etiqueta = ctk.CTkLabel(self.marco, text="Planificador de Actividades", font=("Arial", 20))
        self.etiqueta.pack(pady=10)

        # Botones principales
        self.btn_actividades = ctk.CTkButton(self.marco, text="Ver Actividades", command=self.abrir_actividades)
        self.btn_actividades.pack(pady=5)

        self.btn_agregar = ctk.CTkButton(self.marco, text="Agregar Actividad", command=self.abrir_agregar)
        self.btn_agregar.pack(pady=5)

        self.btn_alertas = ctk.CTkButton(self.marco, text="Ver Alertas", command=self.abrir_alertas)
        self.btn_alertas.pack(pady=5)

    def abrir_actividades(self):
        VistaActividades(self)

    def abrir_agregar(self):
        VistaAgregarActividad(self)

    def abrir_alertas(self):
        VistaAlertas(self)
