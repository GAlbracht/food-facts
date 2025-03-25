import requests
import time

def fetch_data(pages=10):
    base_url = "https://world.openfoodfacts.org/api/v2/search"
    all_products = []

    for page in range(1, pages + 1):
        params = {
            "page": page,
            "page_size": 100,
            "fields": "product_name,nutriments,categories,ingredients_text,brands,packaging",
            "json": True
        }

        print(f"Fetching page {page}...")

        for attempt in range(3):
            try:
                response = requests.get(base_url, params=params, timeout=10)
                response.raise_for_status()
                products = response.json().get("products", [])
                all_products.extend(products)
                break # Exit retry loop if successful
            except requests.exceptions.RequestException as e:
                print(f"Attempt {attempt + 1} failed: {e}")
                time.sleep(2)

        else:
            print(f"Skipping page {page} after 3 failed attempts.")

    print(f"Fetched total: {len(all_products)} products")
    
    import os
    import json
    os.makedirs("data/raw", exist_ok=True)
    with open("data/raw/products.json", "w", encoding="utf-8") as f:
        json.dump(all_products, f, indent=2)
