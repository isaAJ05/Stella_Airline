from math import sin, cos, sqrt, atan2, radians
import networkx as nx
import folium
import webbrowser, os,random

class Grafito:
    def __init__(self) -> None:
        # Inicializa el grafo y el diccionario de nodos
        self.G = nx.Graph()
        self.nodes = {}

    def calcular_distancia(self, lat1, lon1, lat2, lon2):
        # Calcula la distancia entre dos puntos geográficos
        R = 6371  # radio de la Tierra en kilómetros
        dlon = radians(lon2) - radians(lon1) # diferencia de longitudes
        dlat = radians(lat2) - radians(lat1) # diferencia de latitudes
        a = sin(dlat / 2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2)**2 # fórmula de Haversine
        # a es la distancia angular en radianes
        # c es la distancia en la superficie de la Tierra
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
        aeropuerto = self.nodes[codigo] # Obtiene el aeropuerto del diccionario de nodos
        print(f"Código: {codigo}")
        print(f"Nombre: {aeropuerto['nombre']}")
        print(f"Ciudad: {aeropuerto['ciudad']}")
        print(f"País: {aeropuerto['pais']}")
        print(f"Latitud: {aeropuerto['latitud']}")
        print(f"Longitud: {aeropuerto['longitud']}")

    def dijkstra(self, start):
        # Calcula las distancias más cortas desde un nodo de inicio usando el algoritmo de Dijkstra
        return nx.single_source_dijkstra_path_length(self.G, start)

    def diez_aeropuertos_mas_lejanos(self, codigo_origen):
        # Encuentra los diez aeropuertos más lejanos desde un aeropuerto de origen
        distancias = self.dijkstra(codigo_origen)
        del distancias[codigo_origen]
        distancias_ordenadas = sorted(distancias.items(), key=lambda x: x[1], reverse=True)[:10]
        
        lat1, lon1 = self.nodes[codigo_origen]['latitud'], self.nodes[codigo_origen]['longitud']
        m2 = folium.Map(location=[lat1, lon1], zoom_start=2)
        
        for codigo, distancia in distancias_ordenadas:
            print(f"\nAeropuerto: {codigo}")
            self.mostrar_informacion_aeropuerto(codigo)
            print(f"Distancia desde {codigo_origen}: {distancia} km")
            self.dibujar_mUchOS_camino_minimo(codigo_origen, codigo,m2)

          # Guardar el mapa como un archivo HTML
        m2.save('mapa2.html')
        os.startfile('mapa2.html')
        
    def mostrar_todos_aeropuertos(self):
    # Inicializar un mapa con una ubicación central y un nivel de zoom inicial
        m = folium.Map(location=[0, 0], zoom_start=2)

        # Iterar sobre todos los nodos en el grafo
        for codigo in self.nodes:
            # Obtener la latitud y longitud del nodo
            lat, lon = self.nodes[codigo]['latitud'], self.nodes[codigo]['longitud']

            # Crear un marcador en el mapa en la ubicación del nodo
            folium.Marker([lat, lon], popup=f"Código: {codigo}\nNombre: {self.nodes[codigo]['nombre']}\nCiudad: {self.nodes[codigo]['ciudad']}\nPaís: {self.nodes[codigo]['pais']}\nLatitud: {lat}\nLongitud: {lon}", icon=folium.Icon(color="red", icon = "plane")).add_to(m)

        # Guardar el mapa como un archivo HTML
        m.save('todos_aeropuertos.html')
        os.startfile('todos_aeropuertos.html')    
           
    def diez_aeropuertos_mas_lejanos(self, codigo_origen,r,t):
        # Encuentra los diez aeropuertos más lejanos desde un aeropuerto de origen
        distancias = self.dijkstra(codigo_origen)
        del distancias[codigo_origen]
        distancias_ordenadas = sorted(distancias.items(), key=lambda x: x[1], reverse=True)[:10]
        if(r=='1'):
            lat1, lon1 = self.nodes[codigo_origen]['latitud'], self.nodes[codigo_origen]['longitud']
            m2 = folium.Map(location=[lat1, lon1], zoom_start=2)
        
        for codigo, distancia in distancias_ordenadas:
            print(f"\nAeropuerto: {codigo}")
            self.mostrar_informacion_aeropuerto(codigo)
            print(f"Distancia desde {codigo_origen}: {distancia} km")
            if(r=='1'):
                self.dibujar_mUchOS_camino_minimo(codigo_origen, codigo,m2,t)
                
            # Obtener el camino mínimo entre el aeropuerto de origen y el aeropuerto actual
            camino_minimo = self.camino_minimo(codigo_origen, codigo)
            print(f"Camino mínimo desde {codigo_origen} a {codigo}: {camino_minimo}")

        # Guardar el mapa como un archivo HTML
       
        if(r=='1'):
            m2.save('mapa2.html')
            os.startfile('mapa2.html')

    def dibujar_mUchOS_camino_minimo(self, codigo_origen, codigo_destino, m,t):
    # Obtiene el camino más corto entre dos aeropuertos
        camino = self.camino_minimo(codigo_origen, codigo_destino)
        # Crea un conjunto para almacenar las coordenadas de los marcadores ya añadidos
        marcadores = set()
        # Lista de colores
        colores = ["red", "blue", "green", "yellow", "pink", "black", "purple", "orange", "brown"]
        colorRandom = random.choice(colores)
        # Dibuja el camino en el mapa existente
        
        for i in range(len(camino) - 1):
            # Aquí va el código para dibujar el camino en el mapa  
            if i==0:
                col="pink"
            else:
                col="blue"
                
            lat1, lon1 = self.nodes[camino[i]]['latitud'], self.nodes[camino[i]]['longitud']
            lat2, lon2 = self.nodes[camino[i+1]]['latitud'], self.nodes[camino[i+1]]['longitud']

            # Dibuja una línea entre los aeropuertos
            if t=='1':
                folium.PolyLine([(lat1, lon1), (lat2, lon2)], color=colorRandom, weight=2.5, opacity=1).add_to(m)

            # Añade un marcador para cada aeropuerto, si no se ha añadido ya uno en esas coordenadas
            if (lat1, lon1) not in marcadores and i==0: # NO SE DESEA VISUALIZAR LAS RUTAS
                folium.Marker([lat1, lon1], popup=f"Código: {camino[i]}\nNombre: {self.nodes[camino[i]]['nombre']}\nCiudad: {self.nodes[camino[i]]['ciudad']}\nPaís: {self.nodes[camino[i]]['pais']}\nLatitud: {lat1}\nLongitud: {lon1}",icon=folium.Icon(color=col, icon="plane")).add_to(m)
                marcadores.add((lat1, lon1))
                
          

       
        # Añade un marcador para el último aeropuerto, si no se ha añadido ya uno en esas coordenadas
        if (lat2, lon2) not in marcadores:
            folium.Marker([lat2, lon2], popup=f"Código: {camino[-1]}\nNombre: {self.nodes[camino[-1]]['nombre']}\nCiudad: {self.nodes[camino[-1]]['ciudad']}\nPaís: {self.nodes[camino[-1]]['pais']}\nLatitud: {lat2}\nLongitud: {lon2}",icon=folium.Icon(color="cadetblue",icon="cloud")).add_to(m)          
        
                  
    
    def camino_minimo(self, codigo_origen, codigo_destino):
        # Calcula el camino más corto desde un aeropuerto de origen a un aeropuerto de destino
        return nx.dijkstra_path(self.G, codigo_origen, codigo_destino)

    def dibujar_camino_minimo(self, codigo_origen, codigo_destino):
        # Obtiene el camino más corto entre dos aeropuertos
        camino = self.camino_minimo(codigo_origen, codigo_destino)

        # Crea un mapa centrado en el primer aeropuerto del camino
        lat1, lon1 = self.nodes[camino[0]]['latitud'], self.nodes[camino[0]]['longitud']
        m = folium.Map(location=[lat1, lon1], zoom_start=2)

        # Dibuja el camino en el mapa
        for i in range(len(camino) - 1):
            lat1, lon1 = self.nodes[camino[i]]['latitud'], self.nodes[camino[i]]['longitud']
            lat2, lon2 = self.nodes[camino[i+1]]['latitud'], self.nodes[camino[i+1]]['longitud']

            # Dibuja una línea entre los aeropuertos
            folium.PolyLine([(lat1, lon1), (lat2, lon2)], color="blue", weight=2.5, opacity=1).add_to(m)

            # Añade un marcador para cada aeropuerto
            if i == 0:
                folium.Marker([lat1, lon1], popup=f"Código: {camino[i]}\nNombre: {self.nodes[camino[i]]['nombre']}\nCiudad: {self.nodes[camino[i]]['ciudad']}\nPaís: {self.nodes[camino[i]]['pais']}\nLatitud: {lat1}\nLongitud: {lon1}", icon=folium.Icon(color="pink", icon = "plane")).add_to(m)
            else:
                folium.Marker([lat1, lon1], popup=f"Código: {camino[i]}\nNombre: {self.nodes[camino[i]]['nombre']}\nCiudad: {self.nodes[camino[i]]['ciudad']}\nPaís: {self.nodes[camino[i]]['pais']}\nLatitud: {lat1}\nLongitud: {lon1}", icon=folium.Icon(color="cadetblue", icon = "cloud")).add_to(m)

        # Añade un marcador para el último aeropuerto
        folium.Marker([lat2, lon2], popup=f"Código: {camino[-1]}\nNombre: {self.nodes[camino[-1]]['nombre']}\nCiudad: {self.nodes[camino[-1]]['ciudad']}\nPaís: {self.nodes[camino[-1]]['pais']}\nLatitud: {lat2}\nLongitud: {lon2}", icon=folium.Icon(color="pink", icon = "plane")).add_to(m)

        # Muestra el mapa
        return m
