# Load to SQL Server script placeholder
import pandas as pd
import pyodbc
import json

def load_to_sqlserver():
    with open("config/sqlserver_config.json") as f:
        cfg = json.load(f)

    conn_str = (
        f"DRIVER={{{cfg['driver']}}};"
        f"SERVER={cfg['server']};"
        f"UID={cfg['username']};"
        f"PWD={cfg['password']}"
    )
    conn = pyodbc.connect(conn_str, autocommit=True)
    cursor = conn.cursor()

    try:
        cursor.execute("CREATE DATABASE OpenFood")
    except:
        pass

    cursor.execute("USE OpenFood")

    cursor.execute("IF OBJECT_ID('products') IS NOT NULL DROP TABLE products")
    cursor.execute("""
        CREATE TABLE products (
            id INT IDENTITY(1,1) PRIMARY KEY,
            product_name NVARCHAR(255),
            brands NVARCHAR(255),
            categories NVARCHAR(255),
            ingredients_text NVARCHAR(MAX),
            packaging NVARCHAR(255),
            energy_kcal FLOAT,
            fat FLOAT,
            sugars FLOAT,
            proteins FLOAT,
            salt FLOAT
        )
    """)

    df = pd.read_csv("data/processed/products_clean.csv")

    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO products (
                product_name, brands, categories, ingredients_text, packaging,
                energy_kcal, fat, sugars, proteins, salt
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, tuple(row.fillna("").values))

    conn.commit()
    cursor.close()
    conn.close()
    print("✅ Loaded data into SQL Server.")
