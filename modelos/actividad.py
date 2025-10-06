class Actividad:
    def __init__(self, id_num, tipo, nombre, fecha_hora, responsable, estado):
        self.id = id_num                 # int
        self.tipo = tipo                 # str
        self.nombre = nombre             # str
        self.fecha_hora = fecha_hora     # "AAAA-MM-DD HH:MM"
        self.responsable = responsable   # str
        self.estado = estado             # "Pendiente" / "Completada"

    def a_csv(self):
        # Limpieza básica de campos
        campos = [
            str(self.id),
            self.tipo.replace("|", "/").replace("\n", " "),
            self.nombre.replace("|", "/").replace("\n", " "),
            self.fecha_hora.replace("|", "/").replace("\n", " "),
            self.responsable.replace("|", "/").replace("\n", " "),
            self.estado.replace("|", "/").replace("\n", " "),
        ]
        return "|".join(campos)

    @staticmethod
    def desde_csv(linea):
        linea = linea.strip()
        if not linea:
            return None
        partes = linea.split("|")
        if len(partes) != 6:
            return None
        try:
            idn = int(partes[0])
        except ValueError:
            return None
        return Actividad(idn, partes[1], partes[2], partes[3], partes[4], partes[5])
