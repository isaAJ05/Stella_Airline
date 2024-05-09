import pandas as pd
import webbrowser 
from Grafo import Grafito

print("\n¡Bienvenido a Stella Airline!") #INICIOOOOOO
# Leer el archivo CSV
df = pd.read_csv('Archivos/flights_final.csv')
# Crear un grafo
G = Grafito()

# Añadir los nodos y las aristas al grafo
for _, row in df.iterrows():
    G.add_vertex(row['Source Airport Code'], row['Source Airport Name'], row['Source Airport City'], row['Source Airport Country'], row['Source Airport Latitude'], row['Source Airport Longitude'])
    G.add_vertex(row['Destination Airport Code'], row['Destination Airport Name'], row['Destination Airport City'], row['Destination Airport Country'], row['Destination Airport Latitude'], row['Destination Airport Longitude'])
    peso = G.calcular_distancia(row['Source Airport Latitude'], row['Source Airport Longitude'], row['Destination Airport Latitude'], row['Destination Airport Longitude'])
    G.add_edge(row['Source Airport Code'], row['Destination Airport Code'], peso)

while True :  # Bucle para continuar o salir del programa
    print("\n1.Comenzar")
    print("2. Salir")
    opcion = input("\n-> Introduce el número de la opción que deseas: ")
    
    if opcion == '1':
        aeropuerto1 = input("\nIntroduce el código del aeropuerto: ")
        while aeropuerto1 in G.nodes:
            op=input("\n¿Qué desea hacer con el aeropuerto?\n 1. Mostrar información\n 2. Consultar los 10 aeropuertos más lejanos\n 3. Dibujar camino mínimo con otro aeropuerto\n-> ")
            if op=='1':
                print("\nInformación del aeropuerto:")
                G.mostrar_informacion_aeropuerto(aeropuerto1)
            elif op=='2':
                r=input("\n¿Desea visualizar los aereopuertos en el mapa? 1. Si 2. No\n-> ")
                if r=='1':
                    t=input("\n¿Desea visualizar las rutas tambien en el mapa? 1. Si 2. No\n-> ")
                else:
                    t='0'
                print("\nLos 10 aeropuertos más lejanos son:")
                G.diez_aeropuertos_mas_lejanos(aeropuerto1,r,t)
                # Mostrar en el mapa las rutas a los 10 aeropuertos mas lejanos
            elif op=='3':
                aeropuerto2 = input("\nIntroduce el código del aeropuerto de destino: ")
                if aeropuerto2 in G.nodes:
                    camino_minimo = G.camino_minimo(aeropuerto1, aeropuerto2)
                    print("\nEl camino mínimo entre el aeropuerto", aeropuerto1, "y el aeropuerto", aeropuerto2, "es:")
                    print("->", camino_minimo) # Obtener el camino mínimo en consola
                    mapa = G.dibujar_camino_minimo(aeropuerto1, aeropuerto2)
                    # Guardar el mapa como un archivo HTML
                    mapa.save('mapa.html') 
                    webbrowser.open('mapa.html')  # Abrir el mapa en el navegador
                else:
                    print("No se encontró el código del segundo aeropuerto ingresado. Por favor, intenta de nuevo.")  # Si no se encontró una coincidencia, se pide al usuario que intente de nuevo 
            print("\n¿Desea continuar con el aeropuerto ", aeropuerto1, "? 1. Si 2. No") # Mini submenú para continuar con el mismo aeropuerto o no
            continuar = input("-> ")
            if continuar == '1':
                continue
            else:
                break
        else:
            print("No se encontró el código ingresado. Por favor, intenta de nuevo.")  # Si no se encontró una coincidencia, se pide al usuario que intente de nuevo
    elif opcion == '2':
        print("\n¡Gracias por usar Stella Airline! ¡Hasta pronto!")
        break  # Si el usuario no desea continuar, se rompe el bucle
    else:
        print("Opción no válida. Por favor, intenta de nuevo.")
    
    print("*************************************************************\n")  