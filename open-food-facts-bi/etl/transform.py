# Transform script placeholder
import json
import pandas as pd
import os

def transform_data():
    with open("data/raw/products.json", encoding="utf-8") as f:
        products = json.load(f)

    df = pd.json_normalize(products)
    df = df[[
        "product_name", "brands", "categories", "ingredients_text", "packaging",
        "nutriments.energy-kcal_100g", "nutriments.fat_100g", "nutriments.sugars_100g",
        "nutriments.proteins_100g", "nutriments.salt_100g"
    ]].dropna()

    df.rename(columns={
        "nutriments.energy-kcal_100g": "energy_kcal",
        "nutriments.fat_100g": "fat",
        "nutriments.sugars_100g": "sugars",
        "nutriments.proteins_100g": "proteins",
        "nutriments.salt_100g": "salt"
    }, inplace=True)

    os.makedirs("data/processed", exist_ok=True)
    df.to_csv("data/processed/products_clean.csv", index=False)
    print(f"✅ Transformed and saved {df.shape[0]} cleaned rows.")
