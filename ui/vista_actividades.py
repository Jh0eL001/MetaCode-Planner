import customtkinter as ctk
from servicios.gestor_actividades import GestorActividades

class VistaActividades(ctk.CTkToplevel):
    def __init__(self, padre):
        super().__init__(padre)
        self.title("Lista de Actividades")
        self.geometry("860x540")

        self.gestor = GestorActividades()

        ctk.CTkLabel(self, text="Actividades registradas", font=("Arial", 16)).pack(pady=8)

        self.texto = ctk.CTkTextbox(self, width=820, height=360)
        self.texto.pack(padx=10, pady=8)
        self.texto.configure(state="disabled")

        cont = ctk.CTkFrame(self)
        cont.pack(fill="x", padx=10, pady=8)

        ctk.CTkLabel(cont, text="ID:").grid(row=0, column=0, padx=5, pady=5)
        self.ent_id = ctk.CTkEntry(cont, width=120, placeholder_text="ID numérico")
        self.ent_id.grid(row=0, column=1, padx=5, pady=5)

        ctk.CTkButton(cont, text="Marcar Completada", command=self.marcar).grid(row=0, column=2, padx=6, pady=5)
        ctk.CTkButton(cont, text="Eliminar", command=self.eliminar).grid(row=0, column=3, padx=6, pady=5)
        ctk.CTkButton(cont, text="Actualizar Lista", command=self.cargar).grid(row=0, column=4, padx=6, pady=5)

        self.cargar()

    def cargar(self):
        self.texto.configure(state="normal")
        self.texto.delete("1.0", "end")
        self.texto.insert("end", "ID  | Tipo | Nombre | FechaHora        | Responsable | Estado\n")
        self.texto.insert("end", "-"*95 + "\n")
        for linea in self.gestor.leer_todo():   # generador, sin listas en memoria
            self.texto.insert("end", linea + "\n")
        self.texto.configure(state="disabled")

    def marcar(self):
        id_txt = self.ent_id.get().strip()
        if not id_txt.isdigit():
            return self._mensaje("Ingrese un ID válido.")
        ok = self.gestor.marcar_completada(int(id_txt))
        self._mensaje("Actualizado." if ok else "No se encontró el ID.")
        self.cargar()

    def eliminar(self):
        id_txt = self.ent_id.get().strip()
        if not id_txt.isdigit():
            return self._mensaje("Ingrese un ID válido.")
        ok = self.gestor.eliminar(int(id_txt))
        self._mensaje("Eliminado." if ok else "No se encontró el ID.")
        self.cargar()

    def _mensaje(self, msj):
        dlg = ctk.CTkToplevel(self)
        dlg.title("Mensaje")
        ctk.CTkLabel(dlg, text=msj).pack(padx=20, pady=15)
        ctk.CTkButton(dlg, text="Cerrar", command=dlg.destroy).pack(pady=10)

