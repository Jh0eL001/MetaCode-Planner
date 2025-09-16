import customtkinter as ctk

class VistaActividades(ctk.CTkToplevel):
    def __init__(self, padre):
        super().__init__(padre)
        self.title("Lista de Actividades")
        self.geometry("600x400")

        etiqueta = ctk.CTkLabel(self, text="Aquí se mostrará la lista de actividades registradas.")
        etiqueta.pack(pady=20)
