import configparser
import pandas as pd
import random
import os
from logger import setup_logging, cleanup_logs

logger = setup_logging()
parent_dir = os.path.dirname(os.path.dirname(__file__))
config = configparser.ConfigParser()
config.read(os.path.join(parent_dir, "config.ini"))

data_creds = config["DATA"]
sales_rows = int(data_creds["sales_rows"])

data_path = os.path.join(parent_dir, "data", "raw")

customer_status_weights = {"Bronze": 1, "Silver": 2, "Gold": 4, "Platinum": 6}

employee_position_weights = {
    "Store Manager": 0.5,
    "Assistant Manager": 1,
    "Senior Sales Associate": 3,
    "Sales Associate": 5,
    "Cashier": 4,
}

brand_segment_weights = {"Budget": 5, "Standard": 3, "Premium": 1}

category_weights = {
    "Cleaning": 5,
    "Bathroom": 4,
    "Kitchen": 3,
    "Storage": 3,
    "Textile": 2,
    "Garden": 2,
}

quantity_weights = {1: 0.60, 2: 0.25, 3: 0.10, 4: 0.04, 5: 0.01}

payment_method_weights = {"Card": 0.65, "Cash": 0.20, "Online": 0.15}

discount_ranges = {
    "Bronze": (0.00, 0.05),
    "Silver": (0.00, 0.10),
    "Gold": (0.05, 0.15),
    "Platinum": (0.10, 0.20),
}

month_seasonality_weights = {
    1: 0.75,
    2: 0.85,
    3: 0.95,
    4: 1.00,
    5: 1.10,
    6: 1.15,
    7: 1.15,
    8: 1.10,
    9: 1.00,
    10: 1.05,
    11: 1.25,
    12: 1.45,
}

weekday_weights = {
    "Monday": 0.85,
    "Tuesday": 0.90,
    "Wednesday": 0.95,
    "Thursday": 1.00,
    "Friday": 1.15,
    "Saturday": 1.35,
    "Sunday": 1.25,
}

category_seasonality_weights = {
    "Cleaning": {
        1: 1.00,
        2: 1.00,
        3: 1.05,
        4: 1.10,
        5: 1.10,
        6: 1.00,
        7: 1.00,
        8: 1.00,
        9: 1.05,
        10: 1.10,
        11: 1.15,
        12: 1.20,
    },
    "Kitchen": {
        1: 0.90,
        2: 0.95,
        3: 1.00,
        4: 1.00,
        5: 1.05,
        6: 1.05,
        7: 1.00,
        8: 1.00,
        9: 1.05,
        10: 1.10,
        11: 1.25,
        12: 1.40,
    },
    "Textile": {
        1: 1.20,
        2: 1.10,
        3: 0.95,
        4: 0.90,
        5: 0.90,
        6: 0.85,
        7: 0.85,
        8: 0.90,
        9: 1.10,
        10: 1.20,
        11: 1.25,
        12: 1.35,
    },
    "Bathroom": {
        1: 1.00,
        2: 1.00,
        3: 1.00,
        4: 1.05,
        5: 1.05,
        6: 1.00,
        7: 1.00,
        8: 1.00,
        9: 1.05,
        10: 1.05,
        11: 1.10,
        12: 1.15,
    },
    "Storage": {
        1: 1.30,
        2: 1.15,
        3: 1.05,
        4: 1.00,
        5: 0.95,
        6: 0.95,
        7: 0.95,
        8: 1.00,
        9: 1.15,
        10: 1.10,
        11: 1.05,
        12: 1.00,
    },
    "Garden": {
        1: 0.40,
        2: 0.50,
        3: 0.80,
        4: 1.30,
        5: 1.60,
        6: 1.50,
        7: 1.30,
        8: 1.20,
        9: 0.90,
        10: 0.70,
        11: 0.50,
        12: 0.40,
    },
}

return_rate = 0.03

discount_season_multiplier = {
    1: 0.80,
    2: 0.90,
    3: 0.90,
    4: 1.00,
    5: 1.00,
    6: 1.00,
    7: 1.00,
    8: 1.00,
    9: 1.00,
    10: 1.10,
    11: 1.30,
    12: 1.40,
}


def generate_fact_sales():
    logger.info('Начата генерация продаж')
    # считываем табличные данные для подготовки к генерации продаж
    customers_df = pd.read_csv(os.path.join(data_path, "dim_customers.csv"))
    date_df = pd.read_csv(os.path.join(data_path, "dim_date.csv"))
    employees_df = pd.read_csv(os.path.join(data_path, "dim_employees.csv"))
    products_df = pd.read_csv(os.path.join(data_path, "dim_products.csv"))
    stores_df = pd.read_csv(os.path.join(data_path, "dim_stores.csv"))

    date_df["date"] = pd.to_datetime(date_df["date"])

    employees_by_store = {}
    for row in employees_df.itertuples():
        store_id = row.store_id
        employee_id = row.employee_id
        employees_by_store.setdefault(store_id, []).append(employee_id)

    customers_by_loyalty = {}
    for row in customers_df.itertuples():
        loyalty_status = row.loyalty_status
        customer_id = row.customer_id
        customers_by_loyalty.setdefault(loyalty_status, []).append(customer_id)

    products_by_category = {}
    product_info_by_id = {}
    for row in products_df.itertuples():
        category = row.category
        product_id = row.product_id
        products_by_category.setdefault(category, []).append(product_id)
        unit_price = row.unit_price
        unit_cost = row.unit_cost
        brand_segment = row.brand_segment
        info = {
            "unit_price": unit_price,
            "unit_cost": unit_cost,
            "category": category,
            "brand_segment": brand_segment,
        }
        product_info_by_id[product_id] = info

    store_ids = stores_df["store_id"].tolist()
    store_weights = stores_df["performance_factor"].tolist()

    dates = date_df["date"].tolist()
    date_weights = []
    for date in dates:
        weekday = date.day_name()
        month = date.month
        weight = round(weekday_weights[weekday] * month_seasonality_weights[month], 2)
        date_weights.append(weight)

    # готовим списки для выбора по весам на основе полученных словарей
    customer_statuses = list(customer_status_weights.keys())
    customer_weights = list(customer_status_weights.values())

    categories = list(category_weights.keys())

    quantities = list(quantity_weights.keys())
    quantity_weight_values = list(quantity_weights.values())

    payment_methods = list(payment_method_weights.keys())
    payment_weight_values = list(payment_method_weights.values())

    sales = []

    #пробная сборка одной продажи
    for sale_id in range(1, sales_rows+1):
        #sale_id = 1
        sale_date = random.choices(dates, weights=date_weights, k=1)[0]
        month = sale_date.month
        store_id = random.choices(store_ids, weights=store_weights, k=1)[0]
        employee_id = random.choice(employees_by_store[store_id])
        customer_status = random.choices(customer_statuses, weights=customer_weights, k=1)[0]
        customer_id = random.choice(customers_by_loyalty[customer_status])
        category_weights_values = [category_weights[category] * category_seasonality_weights[category][month] for category in categories]
        category = random.choices(categories, weights=category_weights_values, k=1)[0]
        product_id = random.choice(products_by_category[category])
        product_info = product_info_by_id[product_id]
        unit_price = product_info['unit_price']
        unit_cost = product_info['unit_cost']
        quantity = random.choices(quantities, weights=quantity_weight_values, k=1)[0]
        payment_method = random.choices(payment_methods, weights=payment_weight_values, k=1)[0]
        min_discount, max_discount = discount_ranges[customer_status]
        season_multiplier = discount_season_multiplier[month]
        discount_pct = round(random.uniform(min_discount, max_discount)*season_multiplier, 2)
        #ограничиваем максимальную скидку 30%
        discount_pct = min(discount_pct, 0.3)
        # расчеты валовой суммы, суммы скидки, выручки, себестоимости, прибыли
        gross_amount = round(unit_price*quantity, 2)
        discount_amount = round(gross_amount*discount_pct, 2)
        revenue = round(gross_amount-discount_amount, 2)
        cost = round(unit_cost*quantity, 2)
        profit = round(revenue-cost, 2)
        #возможность возврата
        is_return = random.random()<return_rate
        if is_return:
            quantity *= -1
            gross_amount *= -1
            discount_amount *= -1
            revenue *= -1
            cost *= -1
            profit *= -1
        sale_info = {'sale_id':sale_id,
                    'sale_date':sale_date,
                    'store_id':store_id,
                    'employee_id':employee_id,
                    'product_id':product_id,
                    'customer_id':customer_id,                 
                    'quantity':quantity,
                    'unit_price':unit_price,
                    'unit_cost':unit_cost,
                    'discount_pct':discount_pct,                 
                    'discount_amount':discount_amount,
                    'revenue':revenue,
                    'cost':cost,                 
                    'profit':profit,
                    'payment_method':payment_method,
                    'is_return':is_return
                    }
        sales.append(sale_info)
    sales_df = pd.DataFrame(sales)
    logger.info(f'Генерация продаж завершена. Сгенерировано {len(sales)} продаж.')
    output_path = os.path.join(data_path, "fact_sales.csv")
    sales_df.to_csv(output_path, index=False)
    return sales_df

if __name__ == "__main__":
    cleanup_logs()
    generate_fact_sales()




