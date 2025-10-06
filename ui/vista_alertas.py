import customtkinter as ctk
from servicios.gestor_actividades import GestorActividades

class VistaAlertas(ctk.CTkToplevel):
    def __init__(self, padre):
        super().__init__(padre)
        self.title("Alertas próximas (24 horas)")
        self.geometry("700x420")

        self.gestor = GestorActividades()

        ctk.CTkLabel(self, text="Actividades en las próximas 24 horas:", font=("Arial", 16)).pack(pady=8)

        self.texto = ctk.CTkTextbox(self, width=660, height=320)
        self.texto.pack(padx=10, pady=10)
        self.texto.configure(state="disabled")

        ctk.CTkButton(self, text="Actualizar", command=self.cargar).pack(pady=6)

        self.cargar()

    def cargar(self):
        self.texto.configure(state="normal")
        self.texto.delete("1.0", "end")
        hay = False
        for linea in self.gestor.alertas_24h():   # generador (sin listas)
            self.texto.insert("end", linea + "\n")
            hay = True
        if not hay:
            self.texto.insert("end", "No hay actividades próximas en 24 horas.\n")
        self.texto.configure(state="disabled")
