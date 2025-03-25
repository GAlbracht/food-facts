import json
import pandas as pd
import os

CATEGORY_MAP = {
    "breakfast": "Breakfast",
    "cereal": "Grains",
    "pasta": "Grains",
    "snack": "Snacks",
    "chocolate": "Sweets",
    "sugar": "Sweets",
    "candy": "Sweets",
    "beverage": "Beverages",
    "drink": "Beverages",
    "juice": "Beverages",
    "milk": "Dairy",
    "yogurt": "Dairy",
    "cheese": "Dairy",
    "bread": "Grains",
    "soup": "Meals",
    "meal": "Meals",
    "meat": "Meat",
    "fish": "Meat",
    "seafood": "Meat",
    "sauce": "Condiments",
    "spread": "Condiments",
    "oil": "Condiments",
    "baby": "Baby Food",
    "plant-based": "Plant-Based",
    "vegan": "Plant-Based",
    "fruit": "Produce",
    "vegetable": "Produce"
}

def map_general_category(raw_category):
    if pd.isna(raw_category):
        return "Other"
    
    category_lower = raw_category.lower()
    
    for keyword, general in CATEGORY_MAP.items():
        if keyword in category_lower:
            return general
    return "Other"

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

    df["general_category"] = df["categories"].apply(map_general_category)

    # Ensure folder exists before saving
    os.makedirs("data/processed", exist_ok=True)
    df.to_csv("data/processed/products_clean.csv", index=False)

    print(f"=Transformed and saved {df.shape[0]} cleaned rows.")
