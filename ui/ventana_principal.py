import customtkinter as ctk
from ui.vista_actividades import VistaActividades
from ui.agregar_actividad import VistaAgregarActividad
from ui.vista_alertas import VistaAlertas

class VentanaPrincipal(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("MetaCode Planner - Planificador Deportivo (Club de Fútbol)")
        self.geometry("900x600")

        # Frame principal con padding
        marco = ctk.CTkFrame(self)
        marco.pack(padx=20, pady=20, fill="both", expand=True)

        # Título
        titulo = ctk.CTkLabel(marco, 
                            text="MetaCode Planner", 
                            font=("Arial", 24, "bold"))
        titulo.pack(pady=20)

        # Frame para botones
        button_frame = ctk.CTkFrame(marco)
        button_frame.pack(pady=20, fill="both", expand=True)

        # Estilo común para botones
        button_style = {
            "width": 300,
            "height": 50,
            "corner_radius": 10,
            "font": ("Arial", 16),
        }

        # Botones
        ctk.CTkButton(
            button_frame, 
            text="Agregar Actividad",
            command=self.abrir_agregar,
            fg_color="#2b62b0",
            hover_color="#1e4785",
            **button_style
        ).pack(pady=15)

        ctk.CTkButton(
            button_frame, 
            text="Ver Actividades",
            command=self.abrir_actividades,
            fg_color="#2b62b0",
            hover_color="#1e4785",
            **button_style
        ).pack(pady=15)

        ctk.CTkButton(
            button_frame, 
            text="Ver Alertas (24h)",
            command=self.abrir_alertas,
            fg_color="#2b62b0",
            hover_color="#1e4785",
            **button_style
        ).pack(pady=15)

        ctk.CTkButton(
            button_frame, 
            text="Salir",
            command=self.destroy,
            fg_color="#c0392b",
            hover_color="#a93226",
            **button_style
        ).pack(pady=15)

    def abrir_actividades(self):
        VistaActividades(self)

    def abrir_agregar(self):
        VistaAgregarActividad(self)

    def abrir_alertas(self):
        VistaAlertas(self)

    def mostrar_alerta(self, mensaje):
        dlg = ctk.CTkToplevel(self)
        dlg.title("Alerta")
        dlg.transient(self)
        dlg.grab_set()
        
        # Centrar el diálogo
        dlg.geometry("400x150")
        x = self.winfo_x() + (self.winfo_width() - 400) // 2
        y = self.winfo_y() + (self.winfo_height() - 150) // 2
        dlg.geometry(f"+{x}+{y}")
        
        ctk.CTkLabel(dlg, text=mensaje, wraplength=350).pack(padx=20, pady=15)
        btn = ctk.CTkButton(dlg, text="Cerrar", command=dlg.destroy)
        btn.pack(pady=10)
        btn.focus_set()
        
        dlg.bind("<Escape>", lambda e: dlg.destroy())
        dlg.bind("<Return>", lambda e: dlg.destroy())

    def verificar_alertas(self):
        gestor = GestorActividades()
        alertas = list(gestor.alertas_24h())
        if alertas:
            self.mostrar_alerta("\n".join(alertas))

