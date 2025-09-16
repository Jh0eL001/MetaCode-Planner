import customtkinter as ctk

class VistaAgregarActividad(ctk.CTkToplevel):
    def __init__(self, padre):
        super().__init__(padre)
        self.title("Agregar Actividad")
        self.geometry("400x300")

        etiqueta = ctk.CTkLabel(self, text="Formulario para nueva actividad")
        etiqueta.pack(pady=20)

        self.campo_nombre = ctk.CTkEntry(self, placeholder_text="Nombre de la actividad")
        self.campo_nombre.pack(pady=5)

        self.campo_fecha = ctk.CTkEntry(self, placeholder_text="Fecha (DD/MM/AA)")
        self.campo_fecha.pack(pady=5)

        self.campo_responsable = ctk.CTkEntry(self, placeholder_text="Responsable")
        self.campo_responsable.pack(pady=5)

        self.btn_guardar = ctk.CTkButton(self, text="Guardar", command=self.guardar_actividad)
        self.btn_guardar.pack(pady=10)

    def guardar_actividad(self):
        print("Actividad guardada (demo).")
        self.destroy()
