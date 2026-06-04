import pandas as pd
import os

parent_dir = os.path.dirname(os.path.dirname(__file__))
data_path = os.path.join(parent_dir, 'data', 'raw')

dim_customers = pd.read_csv(os.path.join(data_path, "dim_customers.csv"))
dim_date = pd.read_csv(os.path.join(data_path, "dim_date.csv"))
dim_employees = pd.read_csv(os.path.join(data_path, "dim_employees.csv"))
dim_products = pd.read_csv(os.path.join(data_path, "dim_products.csv"))
dim_stores = pd.read_csv(os.path.join(data_path, "dim_stores.csv"))
fact_sales = pd.read_csv(os.path.join(data_path, 'fact_sales.csv'))

# 1. Проверка размеров таблиц
print(dim_date.shape)
print(dim_stores.shape)
print(dim_products.shape)
print(dim_employees.shape)
print(dim_customers.shape)
print(fact_sales.shape)

# 2. Проверка уникальности primary key в dimension-таблицах
print(dim_date['date'].is_unique)
print(dim_stores['store_id'].is_unique)
print(dim_products['product_id'].is_unique)
print(dim_employees['employee_id'].is_unique)
print(dim_customers['customer_id'].is_unique)
print(fact_sales['sale_id'].is_unique)

# 3. Проверка пропущенных значений
tables = {
    'DimDate': dim_date,
    'DimStores': dim_stores,
    'DimProducts': dim_products,
    'DimEmployees': dim_employees,
    'DimCustomers': dim_customers,
    'FactSales': fact_sales
}

for name, df in tables.items():
    print(f'\n{name}')
    print(df.isna().sum())

# 4. Проверка внешних ключей FactSales

print('store_id:', fact_sales['store_id'].isin(dim_stores['store_id']).all())
print('employee_id:', fact_sales['employee_id'].isin(dim_employees['employee_id']).all())
print('product_id:', fact_sales['product_id'].isin(dim_products['product_id']).all())
print('customer_id:', fact_sales['customer_id'].isin(dim_customers['customer_id']).all())
print('sale_date:', fact_sales['sale_date'].isin(dim_date['date']).all())

# 5. Проверка числовых показателей
numeric_cols = [
    'quantity',
    'unit_price',
    'unit_cost',
    'discount_pct',
    'discount_amount',
    'revenue',
    'cost',
    'profit'
]

for col in numeric_cols:
    print(col, fact_sales[col].min(), fact_sales[col].max())

invalid_sales = fact_sales[
    (fact_sales['is_return'] == False) &
    (fact_sales['quantity'] < 0)
]

invalid_returns = fact_sales[
    (fact_sales['is_return'] == True) &
    (fact_sales['quantity'] > 0)
]

print(len(invalid_sales))
print(len(invalid_returns))

revenue_check = (
    fact_sales['quantity'] *
    fact_sales['unit_price'] -
    fact_sales['discount_amount']
)

print((abs(revenue_check - fact_sales['revenue']) > 0.01).sum())

profit_check = (
    fact_sales['revenue'] -
    fact_sales['cost']
)

print((abs(profit_check - fact_sales['profit']) > 0.01).sum())