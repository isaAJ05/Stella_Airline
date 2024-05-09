import csv
import os

class Aeropuerto:
    # Constructor
    def __init__(self, codigo, nombre, ciudad, pais, latitud, longitud):
        self.codigo = codigo
        self.nombre = nombre
        self.ciudad = ciudad
        self.pais = pais
        self.latitud = latitud
        self.longitud = longitud

    @classmethod
    # Método para cargar la información de los aeropuertos desde un archivo CSV
    def cargar_aeropuertos(cls, nombre_archivo):
        aeropuertos = []
        try:
            with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
                lector = csv.DictReader(archivo)
                for fila in lector:
                    aeropuerto = cls(
                        fila['Source Airport Code'],
                        fila['Source Airport Name'],
                        fila['Source Airport City'],
                        fila['Source Airport Country'],
                        fila['Source Airport Latitude'],
                        fila['Source Airport Longitude']
                    )
                    aeropuertos.append(aeropuerto)
        except Exception as e:
            print(f"Error al cargar los aeropuertos: {e}")
        finally:
            return aeropuertos
        
    def get_info_aeropuerto(self):
        return f"{self.codigo} - {self.nombre} - {self.ciudad} - {self.pais} - {self.latitud} - {self.longitud}"
        
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