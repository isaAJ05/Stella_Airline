from math import sin, cos, sqrt, atan2, radians
import networkx as nx

class Grafito:
    def __init__(self) -> None:
        # Inicializa el grafo y el diccionario de nodos
        self.G = nx.Graph()
        self.nodes = {}

    def calcular_distancia(self, lat1, lon1, lat2, lon2):
        # Calcula la distancia entre dos puntos geográficos
        R = 6371  # radio de la Tierra en kilómetros
        dlon = radians(lon2) - radians(lon1)
        dlat = radians(lat2) - radians(lat1)
        a = sin(dlat / 2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        return R * c

    def add_vertex(self, codigo, nombre, ciudad, pais, latitud, longitud) -> None:
        # Añade un vértice al grafo y al diccionario de nodos
        self.G.add_node(codigo)
        self.nodes[codigo] = {'nombre': nombre, 'ciudad': ciudad, 'pais': pais, 'latitud': latitud, 'longitud': longitud}

    def add_edge(self, vi: str, vf: str, peso: float) -> bool:
        # Añade una arista al grafo si ambos vértices existen
        if not ((vi in self.nodes) and (vf in self.nodes)):
            return False
        self.G.add_edge(vi, vf, weight=peso)
        return True

    def mostrar_informacion_aeropuerto(self, codigo):
        # Muestra la información de un aeropuerto
        aeropuerto = self.nodes[codigo]
        print(f"Código: {codigo}")
        print(f"Nombre: {aeropuerto['nombre']}")
        print(f"Ciudad: {aeropuerto['ciudad']}")
        print(f"País: {aeropuerto['pais']}")
        print(f"Latitud: {aeropuerto['latitud']}")
        print(f"Latitud: {aeropuerto['longitud']}")

    def dijkstra(self, start):
        # Calcula las distancias más cortas desde un nodo de inicio usando el algoritmo de Dijkstra
        return nx.single_source_dijkstra_path_length(self.G, start)

    def diez_aeropuertos_mas_lejanos(self, codigo_origen):
        # Encuentra los diez aeropuertos más lejanos desde un aeropuerto de origen
        distancias = self.dijkstra(codigo_origen)
        del distancias[codigo_origen]
        distancias_ordenadas = sorted(distancias.items(), key=lambda x: x[1], reverse=True)[:10]
        for codigo, distancia in distancias_ordenadas:
            print(f"\nAeropuerto: {codigo}")
            self.mostrar_informacion_aeropuerto(codigo)
            print(f"Distancia desde {codigo_origen}: {distancia} km")