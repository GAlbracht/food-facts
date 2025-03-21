# Extract script placeholder
import requests
import json
import os

def fetch_data(pages=3):
    base_url = "https://world.openfoodfacts.org/api/v2/search"
    all_products = []

    for page in range(1, pages + 1):
        params = {
            "page": page,
            "page_size": 100,
            "fields": "product_name,nutriments,categories,ingredients_text,brands,packaging",
            "json": True
        }
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        all_products.extend(response.json().get("products", []))

    os.makedirs("data/raw", exist_ok=True)
    with open("data/raw/products.json", "w", encoding="utf-8") as f:
        json.dump(all_products, f, indent=2)
    print(f"✅ Fetched and saved {len(all_products)} products.")
