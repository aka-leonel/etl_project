import requests
import os
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

# Se cargan las variables del archivo .env
load_dotenv()
fuentes = {
        "museos": "https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/4207def0-2ff7-41d5-9095-d42ae8207a5d/download/museos_datosabiertos.csv",
        "bibliotecas": "https://datos.cultura.gob.ar/dataset/37305de4-3cce-4d4b-9d9a-fec3ca61d09f/resource/01c6c048-dbeb-44e0-8efa-6944f73715d7/download/bibliotecas-populares.csv"
    }
def get_path(categoria):
    """Genera la ruta: categoria/año-mes/categoria-dia-mes-año.csv"""
    ahora = datetime.now()

    # Nombres de meses en español  
    meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", 
             "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    nombre_mes = meses[ahora.month -1]

    anio_mes = f"{ahora.year}-{nombre_mes}"
    nombre_archivo = f"{categoria}-{ahora.strftime('%d-%m-%Y')}.csv"

    # Construimos la ruta completa dentro de data/raw
    ruta = Path("data") /"raw" / categoria /anio_mes

    # Creamos las carpetas si no existen
    ruta.mkdir(parents=True, exist_ok=True)

    return ruta / nombre_archivo

def download_data(categoria, url):
    output_path = get_path(categoria)

    try:
        print(f"Iniciando descarga de {categoria} desde: {url}...") # Reemplazar por log
        response= requests.get(url, timeout=10)
        response.raise_for_status() # Tira error si la descarga falla
        # Reemplazar por log

        # Se guarda el archivo en data/raw/
        with open(output_path, 'wb') as f:
            f.write(response.content)

        print(f"Archivo guardado en: {output_path}")
        return output_path
    
    except Exception as e:
        print(f"Error descargando {categoria}: {e}")
        return None

def run_extraction():
    
    rutas_descargadas = {}
    for categ, url in fuentes.items():
        ruta = download_data(categ, url)
        if ruta:
            rutas_descargadas[categ] =ruta
        
    return rutas_descargadas

if __name__ == "__main__":
    run_extraction()