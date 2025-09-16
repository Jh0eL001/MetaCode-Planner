import customtkinter as ctk

class VistaAlertas(ctk.CTkToplevel):
    def __init__(self, padre):
        super().__init__(padre)
        self.title("Alertas")
        self.geometry("400x300")

        etiqueta = ctk.CTkLabel(self, text="Aquí se mostrarán las alertas de actividades próximas.")
        etiqueta.pack(pady=20)
