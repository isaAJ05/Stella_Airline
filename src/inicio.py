import csv
import os

def buscar_en_csv(nombre_archivo, nombre_columna, valor_buscado):
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            if fila[nombre_columna] == valor_buscado:
                resultado = {
                    'Codigo': fila['Source Airport Code'],
                    'Nombre': fila['Source Airport Name'],
                    'Ciudad': fila['Source Airport City'],
                    'Pais': fila['Source Airport Country'],
                    'Latitud': fila['Source Airport Latitude'],
                    'Longitud': fila['Source Airport Longitude']
                }
                print(resultado)
                return True  # Retorna True si encuentra una coincidencia
    return False  # Retorna False si no encuentra una coincidencia

print("\nBienvenido a Stella Airline")

while True:  # Bucle Validación
    valor_buscado = input("\n-> Introduce el código del aeropuerto: ")
    ruta_script = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Obtiene la ruta del directorio del script actual
    ruta_archivo = os.path.join(ruta_script, 'Archivos', 'flights_final.csv')  # Construye la ruta al archivo
    encontrado = buscar_en_csv(ruta_archivo, 'Source Airport Code', valor_buscado)
    if encontrado:
        continuar = input("\n¿Desea continuar? (s/n): ")
        if continuar.lower() != 's':
            print("\n¡Gracias por usar Stella Airline! ¡Hasta pronto!")
            break  # Si el usuario no desea continuar, se rompe el bucle
    else:
        print("No se encontró el código ingresado. Por favor, intenta de nuevo.")  # Si no se encontró una coincidencia, se pide al usuario que intente de nuevo
    print("*************************************************************\n")