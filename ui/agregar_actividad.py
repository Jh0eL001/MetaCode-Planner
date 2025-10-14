import customtkinter as ctk
from datetime import datetime, timedelta
from servicios.gestor_actividades import GestorActividades

class SelectorFecha(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        
        # Crear listas para día, mes y año
        self.dias = [str(i).zfill(2) for i in range(1, 32)]
        self.meses = [str(i).zfill(2) for i in range(1, 13)]
        años = range(datetime.now().year, datetime.now().year + 5)
        self.años = [str(i) for i in años]

        # Crear selectores
        self.dia = ctk.CTkOptionMenu(self, values=self.dias, width=60)
        self.mes = ctk.CTkOptionMenu(self, values=self.meses, width=60)
        self.año = ctk.CTkOptionMenu(self, values=self.años, width=80)

        # Valores por defecto
        hoy = datetime.now()
        self.dia.set(str(hoy.day).zfill(2))
        self.mes.set(str(hoy.month).zfill(2))
        self.año.set(str(hoy.year))

        # Layout
        self.dia.grid(row=0, column=0, padx=2)
        ctk.CTkLabel(self, text="/").grid(row=0, column=1)
        self.mes.grid(row=0, column=2, padx=2)
        ctk.CTkLabel(self, text="/").grid(row=0, column=3)
        self.año.grid(row=0, column=4, padx=2)

    def get(self):
        return f"{self.año.get()}-{self.mes.get()}-{self.dia.get()}"

class SelectorHora(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        
        # Crear spinboxes para hora y minuto
        self.hora = ctk.CTkOptionMenu(self, 
                                    values=[f"{i:02d}" for i in range(24)],
                                    width=60)
        self.minuto = ctk.CTkOptionMenu(self, 
                                       values=[f"{i:02d}" for i in range(0, 60, 5)],
                                       width=60)
        
        self.hora.grid(row=0, column=0, padx=2)
        ctk.CTkLabel(self, text=":").grid(row=0, column=1)
        self.minuto.grid(row=0, column=2, padx=2)
        
    def get(self):
        return f"{self.hora.get()}:{self.minuto.get()}"

class VistaAgregarActividad(ctk.CTkToplevel):
    def __init__(self, padre):
        super().__init__(padre)
        self.title("Agregar Actividad")
        self.geometry("500x600")
        
        # Hacer la ventana modal
        self.transient(padre)
        self.grab_set()
        self.focus_set()
        
        self.gestor = GestorActividades()

        marco = ctk.CTkFrame(self)
        marco.pack(padx=10, pady=10, fill="both", expand=True)

        # Tipo con OptionMenu en lugar de Entry
        ctk.CTkLabel(marco, text="Tipo:").pack(pady=5)
        self.campo_tipo = ctk.CTkOptionMenu(marco, 
            values=["Entrenamiento", "Partido", "Reunión", "Otro"])
        self.campo_tipo.pack(pady=3, fill="x", padx=10)

        ctk.CTkLabel(marco, text="Nombre:").pack(pady=5)
        self.campo_nombre = ctk.CTkEntry(marco, placeholder_text="Ej. Sesión táctica")
        self.campo_nombre.pack(pady=3, fill="x", padx=10)

        # Nuevo selector de fecha
        ctk.CTkLabel(marco, text="Fecha:").pack(pady=5)
        self.fecha = SelectorFecha(marco)
        self.fecha.pack(pady=3)

        ctk.CTkLabel(marco, text="Hora:").pack(pady=5)
        self.hora = SelectorHora(marco)
        self.hora.pack(pady=3)

        ctk.CTkLabel(marco, text="Responsable:").pack(pady=5)
        self.campo_responsable = ctk.CTkEntry(marco, placeholder_text="Nombre del responsable")
        self.campo_responsable.pack(pady=3, fill="x", padx=10)

        # Frame para botones
        frame_botones = ctk.CTkFrame(marco)
        frame_botones.pack(fill="x", pady=20)
        
        ctk.CTkButton(frame_botones, text="Guardar", 
                     command=self.guardar).pack(side="left", padx=10, expand=True)
        ctk.CTkButton(frame_botones, text="Cancelar", 
                     command=self.destroy).pack(side="right", padx=10, expand=True)

    def guardar(self):
        tipo = self.campo_tipo.get()
        nombre = self.campo_nombre.get().strip()
        fecha = self.fecha.get()
        hora = self.hora.get()
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

