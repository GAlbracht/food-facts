import os

# Project folder and structure
structure = {
    "open-food-facts-bi": {
        "etl": [
            "extract.py",
            "transform.py",
            "load_sqlserver.py"
        ],
        "data/raw": [],
        "data/processed": [],
        "docker": ["docker-compose.yml"],
        "config": ["sqlserver_config.json"],
        "": ["main.py", "requirements.txt", "README.md"]
    }
}

# Boilerplate content
boilerplate = {
    "requirements.txt": "pandas\nrequests\npyodbc\n",
    "README.md": "# Open Food Facts BI Project\n\nPython ETL → SQL Server → SSRS → Tableau Public pipeline.",
    "etl/extract.py": "# Extract script placeholder\n",
    "etl/transform.py": "# Transform script placeholder\n",
    "etl/load_sqlserver.py": "# Load to SQL Server script placeholder\n",
    "main.py": "# Main ETL script placeholder\n",
    "docker/docker-compose.yml": '''version: '3.9'
services:
  sqlserver:
    image: mcr.microsoft.com/mssql/server:2022-lts
    container_name: sqlserver
    environment:
      SA_PASSWORD: "YourStrong!Passw0rd"
      ACCEPT_EULA: "Y"
    ports:
      - "1433:1433"
    volumes:
      - sql_data:/var/opt/mssql
volumes:
  sql_data:
''',
    "config/sqlserver_config.json": '''{
  "driver": "ODBC Driver 17 for SQL Server",
  "server": "localhost,1433",
  "database": "OpenFood",
  "username": "sa",
  "password": "YourStrong!Passw0rd"
}
'''
}

def create_structure(base_path, layout):
    for top_folder, substructure in layout.items():
        top_path = os.path.join(base_path, top_folder)
        os.makedirs(top_path, exist_ok=True)

        for subfolder, files in substructure.items():
            target_path = os.path.join(top_path, subfolder)
            os.makedirs(target_path, exist_ok=True)

            for file in files:
                file_path = os.path.join(target_path, file)
                # Figure out boilerplate content
                key = f"{subfolder}/{file}" if subfolder else file
                content = boilerplate.get(key, "")
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)

if __name__ == "__main__":
    create_structure(".", structure)
    print(" Project structure created successfully.")
