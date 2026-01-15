
# Árbol de directorios:
proyecto_etl/
│
├── data/               # Local para pruebas
│   ├── raw/            # CSVs originales
│   └── processed/      # CSVs transformados
├── src/                # Código fuente
│   ├── __init__.py
│   ├── extract.py      # Lógica de descarga
│   ├── transform.py    # Limpieza y lógica
│   └── load.py         # Carga a DB
├── config/             # Credenciales (.env)
├── logs/               # Registro de errores
├── main.py             # Orquestador principal
└── requirements.txt    # Librerías (pandas, etc.)