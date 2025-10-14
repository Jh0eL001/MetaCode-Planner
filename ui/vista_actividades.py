import customtkinter as ctk
from tkinter import ttk
import tkinter as tk
from servicios.gestor_actividades import GestorActividades

class VistaActividades(ctk.CTkToplevel):
    def __init__(self, padre):
        super().__init__(padre)
        self.title("Lista de Actividades")
        self.geometry("960x640")
        
        # Hacer la ventana modal
        self.transient(padre)
        self.grab_set()
        
        self.gestor = GestorActividades()
        
        # Título
        ctk.CTkLabel(self, text="Actividades registradas", 
                     font=("Arial", 20, "bold")).pack(pady=10)
        
        # Frame para la tabla
        frame_tabla = ctk.CTkFrame(self)
        frame_tabla.pack(padx=10, pady=5, fill="both", expand=True)
        
        # Crear y configurar el Treeview
        style = ttk.Style()
        style.theme_use('default')
        style.configure("Treeview",
                       background="#2a2d2e",
                       foreground="white",
                       fieldbackground="#2a2d2e",
                       rowheight=25)
        
        # Configurar selección
        style.map('Treeview', background=[('selected', '#22559b')])
        
        # Crear tabla
        self.tabla = ttk.Treeview(frame_tabla, columns=("ID", "Tipo", "Nombre", "FechaHora", "Responsable", "Estado"),
                                 show='headings', style="Treeview")
        
        # Configurar columnas
        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Tipo", text="Tipo")
        self.tabla.heading("Nombre", text="Nombre")
        self.tabla.heading("FechaHora", text="Fecha y Hora")
        self.tabla.heading("Responsable", text="Responsable")
        self.tabla.heading("Estado", text="Estado")
        
        # Ajustar anchos de columna
        self.tabla.column("ID", width=50)
        self.tabla.column("Tipo", width=100)
        self.tabla.column("Nombre", width=200)
        self.tabla.column("FechaHora", width=150)
        self.tabla.column("Responsable", width=150)
        self.tabla.column("Estado", width=100)
        
        # Agregar scrollbar
        scrollbar = ttk.Scrollbar(frame_tabla, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=scrollbar.set)
        
        # Empaquetar tabla y scrollbar
        self.tabla.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Frame de controles
        cont = ctk.CTkFrame(self)
        cont.pack(fill="x", padx=10, pady=8)
        
        ctk.CTkLabel(cont, text="ID:").grid(row=0, column=0, padx=5, pady=5)
        self.ent_id = ctk.CTkEntry(cont, width=120, placeholder_text="ID numérico")
        self.ent_id.grid(row=0, column=1, padx=5, pady=5)
        
        ctk.CTkButton(cont, text="Marcar Completada", 
                     command=self.marcar).grid(row=0, column=2, padx=6, pady=5)
        ctk.CTkButton(cont, text="Eliminar", 
                     command=self.eliminar).grid(row=0, column=3, padx=6, pady=5)
        ctk.CTkButton(cont, text="Actualizar Lista", 
                     command=self.cargar).grid(row=0, column=4, padx=6, pady=5)
        
        self.cargar()
    
    def cargar(self):
        # Recargar datos desde archivo
        self.gestor.cargar_actividades()
        
        # Limpiar tabla
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        
        # Insertar datos actualizados
        for linea in self.gestor.leer_todo():
            datos = linea.split("|")
            tag = "completada" if datos[5].strip() == "Completada" else "pendiente"
            self.tabla.insert("", "end", values=datos, tags=(tag,))

    def marcar(self):
        id_txt = self.ent_id.get().strip()
        if not id_txt.isdigit():
            return self._mensaje("Ingrese un ID válido.")
        ok = self.gestor.marcar_completada(int(id_txt))
        if ok:
            self.cargar()  # Recargar después de marcar
            self._mensaje("Actualizado.")
        else:
            self._mensaje("No se encontró el ID.")

    def eliminar(self):
        id_txt = self.ent_id.get().strip()
        if not id_txt.isdigit():
            return self._mensaje("Ingrese un ID válido.")
        
        # Mostrar diálogo de confirmación
        dlg = ctk.CTkToplevel(self)
        dlg.title("Confirmar")
        dlg.transient(self)
        dlg.grab_set()
        
        # Centrar diálogo
        dlg.geometry("300x150")
        x = self.winfo_x() + (self.winfo_width() - 300) // 2
        y = self.winfo_y() + (self.winfo_height() - 150) // 2
        dlg.geometry(f"+{x}+{y}")
        
        ctk.CTkLabel(dlg, text="¿Está seguro de eliminar esta actividad?").pack(pady=15)
        
        def confirmar():
            ok = self.gestor.eliminar(int(id_txt))
            dlg.destroy()
            if ok:
                self.gestor.cargar_actividades()  # Recargar datos
                self.cargar()  # Actualizar vista
                self._mensaje("Actividad eliminada.")
            else:
                self._mensaje("No se encontró el ID.")
        
        frame_botones = ctk.CTkFrame(dlg)
        frame_botones.pack(fill="x", pady=10)
        
        ctk.CTkButton(frame_botones, text="Sí", command=confirmar).pack(side="left", padx=10, expand=True)
        ctk.CTkButton(frame_botones, text="No", command=dlg.destroy).pack(side="right", padx=10, expand=True)

    def _mensaje(self, msj):
        dlg = ctk.CTkToplevel(self)
        dlg.title("Mensaje")
        dlg.transient(self)
        dlg.grab_set()
        
        # Centrar el diálogo
        dlg.geometry("300x150")
        x = self.winfo_x() + (self.winfo_width() - 300) // 2
        y = self.winfo_y() + (self.winfo_height() - 150) // 2
        dlg.geometry(f"+{x}+{y}")
        
        ctk.CTkLabel(dlg, text=msj).pack(padx=20, pady=15)
        btn = ctk.CTkButton(dlg, text="Cerrar", command=dlg.destroy)
        btn.pack(pady=10)
        btn.focus_set()
        
        # Cerrar con Escape o Enter
        dlg.bind("<Escape>", lambda e: dlg.destroy())
        dlg.bind("<Return>", lambda e: dlg.destroy())

