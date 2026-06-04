import pandas as pd
import random
import os
from logger import cleanup_logs, setup_logging

logger = setup_logging()
parent_dir = os.path.dirname(os.path.dirname(__file__))


# regions = ['Capital', 'Central', 'South', 'North', 'East', 'West']
store_types = ["Mall", "Street", "Outlet"]
cities = {
    "North": ["North City", "River Town", "Pine Hills", "Silver Lake"],
    "South": ["South City", "Sunny Bay", "Palm Coast", "Golden Beach"],
    "East": ["East City", "Mountain View", "Crystal Valley", "Sunrise Point"],
    "West": ["West City", "Lake Point", "Blue Harbor", "Rocky Creek"],
    "Central": [
        "Central City",
        "Green Valley",
        "Oakwood",
        "Maple Grove",
        "Stonebridge",
    ],
    "Capital": [
        "Capital City",
        "Downtown",
        "Business District",
        "Tech Park",
        "Financial Center",
    ],
}
shops_count = {"North": 4, "South": 5, "East": 3, "West": 3, "Central": 7, "Capital": 8}

store_type_weights = {
    "North": (0.1, 0.5, 0.4),
    "South": (0.1, 0.5, 0.4),
    "East": (0.1, 0.6, 0.3),
    "West": (0.1, 0.6, 0.3),
    "Central": (0.4, 0.4, 0.2),
    "Capital": (0.6, 0.3, 0.1),
}

performance_factors = {
    "North": (0.8, 1.10),
    "South": (0.9, 1.20),
    "East": (0.75, 1.05),
    "West": (0.7, 1.00),
    "Central": (1.00, 1.25),
    "Capital": (1.10, 1.40),
}


def generate_dim_stores():
    stores = []
    store_id = 1
    logger.info("Начата генерация магазинов")
    for region, shops in shops_count.items():
        for shop in range(shops):
            city = random.choice(cities[region])
            store_type = random.choices(store_types, store_type_weights[region], k=1)[0]
            store_code = "STORE_" + f"{store_id:03d}"
            store_name = "Store_" + f"{store_id:03d}"
            min_performance, max_performance = performance_factors[region]
            performance_factor = round(
                random.uniform(min_performance, max_performance), 2
            )
            shop_info = {
                "store_id": store_id,
                "store_code": store_code,
                "store_name": store_name,
                "region": region,
                "city": city,
                "store_type": store_type,
                "performance_factor": performance_factor,
            }
            store_id += 1
            stores.append(shop_info)
    shops_df = pd.DataFrame(stores)
    output_path = os.path.join(parent_dir, "data", "raw", "dim_stores.csv")
    shops_df.to_csv(output_path, index=False)
    logger.info(f"Генерация магазинов завершена. Создано {len(shops_df)} магазинов")
    logger.info(f"Файл сохранен: {output_path}")
    return shops_df


if __name__ == "__main__":
    cleanup_logs()
    generate_dim_stores()

