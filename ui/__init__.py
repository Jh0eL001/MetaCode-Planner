import customtkinter as ctk
from ui.ventana_principal import VentanaPrincipal

if __name__ == "__main__":
    ctk.set_appearance_mode("System")   # Opciones: "System", "Dark", "Light"
    ctk.set_default_color_theme("blue") # Otros: "green", "dark-blue"

    app = VentanaPrincipal()
    app.mainloop()