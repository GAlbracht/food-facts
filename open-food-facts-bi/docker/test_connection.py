import pyodbc
import json

with open("E:\\Projects\\Project1\\open-food-facts-bi\\config\\sqlserver_config.json") as f:
    cfg = json.load(f)

conn_str = (
    f"DRIVER={{{cfg['driver']}}};"
    f"SERVER={cfg['server']};"
    f"UID={cfg['username']};"
    f"PWD={cfg['password']};"
    f"Encrypt=no;TrustServerCertificate=yes;"
)

try:
    conn = pyodbc.connect(conn_str, timeout=5)
    print("Connected to SQL Server!")
    conn.close()
except Exception as e:
    print("Connection failed:")
    print(e)
