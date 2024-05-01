import os
from src.inicio import buscar_en_csv, buscar_en_csv
class Aereopueto:
    def __init__(self,valor_buscado):
            ruta_script = os.path.dirname(
                os.path.dirname(os.path.abspath(__file__)))  # Obtiene la ruta del directorio del script actual
            ruta_archivo = os.path.join(ruta_script, 'Archivos', 'flights_final.csv')  # Construye la ruta al archivo
            encontrado = buscar_en_csv(ruta_archivo, 'Source Airport Code', valor_buscado)
            if encontrado:
                self.codigo = encontrado['Codigo']
                self.nombre = encontrado['Nombre']
                self.ciudad = encontrado['Ciudad']
                self.pais = encontrado['Pais']
                self.latitud = encontrado['Latitud']
                self.longitud = encontrado['Longitud']
            else:
                print("No se encontró el código ingresado. Por favor, intenta de nuevo.")  # Si no se encontró una coincidencia, se pide al usuario que intente de nuevo

    def get_AllInfo(self):
        return f'{self.codigo} - {self.nombre} - {self.ciudad} - {self.pais}- {self.latitud} - {self.longitud}'
    def get_Codigo(self):
        return self.codigo
    def get_Nombre(self):
        return self.nombre
    def get_Ciudad(self):
        return self.ciudad
    def get_Pais(self):
        return self.pais
    def get_Latitud(self):
        return self.latitud
    def get_Longitud(self):
        return self.longitud
