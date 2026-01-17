from src.extract import run_extraction

def main():
    print("--- Iniciando Pipeline ETL ---")
    
    # 1. EXTRACCIÓN
    archivos_crudos = run_extraction()
    
    if len(archivos_crudos) == 2:
        print("\nTodos los archivos se descargaron correctamente.")
        # El siguiente paso será pasar 'archivos_crudos' a la transformación
    else:
        print("\nAtención: Algunas fuentes no se pudieron descargar.")

if __name__ == "__main__":
    main()

