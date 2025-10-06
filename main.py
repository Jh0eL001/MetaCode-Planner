import customtkinter as ctk
from ui.ventana_principal import VentanaPrincipal
from servicios.gestor_actividades import GestorActividades

if __name__ == "__main__":
    ctk.set_appearance_mode("System")   # "System", "Dark", "Light"
    ctk.set_default_color_theme("blue") # "green", "dark-blue", "blue"

    # Asegura el archivo de datos antes de abrir la app
    GestorActividades().asegurar_archivo()

    app = VentanaPrincipal()
    app.mainloop()
