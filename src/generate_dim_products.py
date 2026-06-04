import random
import pandas as pd
import os
from logger import cleanup_logs, setup_logging

price_ranges = {
    'Cleaning': (5, 30),
    'Kitchen': (20, 150),
    'Textile': (15, 100),
    'Bathroom': (5, 50),
    'Storage': (10, 80),
    'Garden': (10, 120)
}

margin_ranges = {'Cleaning': (0.2, 0.35),
    'Kitchen': (0.3, 0.5),
    'Textile': (0.25, 0.45),
    'Bathroom': (0.2, 0.4),
    'Storage': (0.25, 0.45),
    'Garden': (0.25, 0.50)}

categories = {
    'Cleaning': [
        'Detergents',
        'Surface Cleaners',
        'Air Fresheners',
        'Dishwashing',
        'Laundry Care'
    ],
    'Kitchen': [
        'Cookware',
        'Utensils',
        'Food Storage',
        'Small Appliances',
        'Tableware'
    ],
    'Textile': [
        'Bedding',
        'Towels',
        'Curtains',
        'Blankets',
        'Pillows'
    ],
    'Bathroom': [
        'Personal Care',
        'Bath Accessories',
        'Shower Products',
        'Toilet Accessories',
        'Cleaning Tools'
    ],
    'Storage': [
        'Boxes',
        'Shelving',
        'Organizers',
        'Hangers',
        'Containers'
    ],
    'Garden': [
        'Plant Care',
        'Garden Tools',
        'Outdoor Decor',
        'Watering',
        'Seeds'
    ]
}

brand_segments = {
    'Premium': [
        'PrimeHouse',
        'NovaHouse',
        'UrbanHome'
    ],
    'Standard': [
        'HomePro',
        'ComfortLine',
        'SmartHome',
        'PureLife',
        'GreenLeaf',
        'BrightHome'
    ],
    'Budget': [
        'CleanMax',
        'EasyCare',
        'DailyChoice',
        'FreshWay',
        'FamilyPlus',
        'EcoLiving'
    ]
}

brand_price_factor = {'Premium': (1.3, 1.6),'Standard': (0.9, 1.2),'Budget': (0.7, 0.9)}

adjectives = ['Organic','Compact','Ergonomic','Durable','Eco-Friendly','Premium','Smart','Modern',
    'Classic','Lightweight','Multi-Purpose','Professional','Comfort','Advanced','Essential']

logger = setup_logging()
parent_dir = os.path.dirname(os.path.dirname(__file__))

def generate_dim_products():
    products = []
    prod_id = 1
    subcategory_counter = 1
    remainder = 10
    base_count = 13
    logger.info('Начата генерация продуктов')
    for category, subcategoryes in categories.items():
        for subcategory in subcategoryes:
            if subcategory_counter<=remainder:
                products_count = base_count+1
            else:
                products_count = base_count
            subcategory_counter += 1
            for product in range(products_count):
                product_id = prod_id
                product_code = 'PROD_'+f'{prod_id:03d}'
                brand_segment = random.choice(list(brand_segments.keys()))
                brand = random.choice(brand_segments[brand_segment])
                adjective = random.choice(adjectives)
                product_name = f'{brand} {adjective} {subcategory} {prod_id:03d}'
                min_price, max_price = price_ranges[category]
                min_factor, max_factor = brand_price_factor[brand_segment]
                price = round(random.uniform(min_price, max_price), 2)
                factor = round(random.uniform(min_factor, max_factor), 2)
                unit_price = round(price*factor, 2)
                min_margin, max_margin = margin_ranges[category]
                margin_pct = round(random.uniform(min_margin, max_margin), 2)
                unit_cost = round(unit_price * (1 - margin_pct), 2)
                product_info = {
                                'product_id': product_id,
                                'product_code': product_code,
                                'product_name': product_name,
                                'category': category,
                                'subcategory': subcategory,
                                'brand': brand,
                                'brand_segment': brand_segment,
                                'unit_price': unit_price,
                                'margin_pct': margin_pct,
                                'unit_cost': unit_cost}
                products.append(product_info)
                prod_id += 1
    logger.info(f"Генерация товаров завершена. Создано {len(products)} товаров")
    df = pd.DataFrame(products)
    output_path = os.path.join(parent_dir, 'data', 'raw', 'dim_products.csv')
    df.to_csv(output_path, index=False)
    return pd.DataFrame(products)

if __name__ == "__main__":
    cleanup_logs()
    generate_dim_products()






            

