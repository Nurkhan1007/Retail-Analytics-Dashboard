import configparser
import pandas as pd
import os
import random
from faker import Faker
from logger import setup_logging, cleanup_logs

logger = setup_logging()

parent_dir = os.path.dirname(os.path.dirname(__file__))
config = configparser.ConfigParser()
config.read(os.path.join(parent_dir, 'config.ini'))

data_creds = config['DATA']
customers_number = int(data_creds['customers'])

fake = Faker()

genders = ['Male', 'Female']
loyalty_statuses = {'Bronze': 0.50, 'Silver': 0.30, 'Gold': 0.15, 'Platinum': 0.05}

loyalty_names = list(loyalty_statuses.keys())
loyalty_weights = list(loyalty_statuses.values())

age_groups = {'18-25': (18, 25), '26-35': (26, 35), '36-45': (36, 45), '46-60': (46, 60), '60+': (61, 75)}
age_group_name = list(age_groups.keys())

age_group_weights = {'18-25': 0.15, '26-35': 0.30, '36-45': 0.25, '46-60': 0.20, '60+': 0.10}
age_weights = list(age_group_weights.values())

#file_path = os.path.join(parent_dir, 'data', 'raw', 'dim_stores.csv')
#df = pd.read_csv(file_path)
#cities = df['city'].unique().tolist()

def generate_dim_customers():
    logger.info('Начата генерация списка клиентов')
    file_path = os.path.join(parent_dir, 'data', 'raw', 'dim_stores.csv')
    df = pd.read_csv(file_path)
    cities = df['city'].unique().tolist()
    customers = []
    for customer_id in range(1, customers_number+1):
        customer_code = 'CUST_'+f'{customer_id:05d}'
        customer_name = fake.name()
        gender = random.choice(genders)
        age_group = random.choices(age_group_name, weights=age_weights, k=1)[0]
        min_age, max_age = age_groups[age_group]
        age = random.randint(min_age, max_age)
        loyalty_status = random.choices(loyalty_names, weights=loyalty_weights, k=1)[0]
        city = random.choice(cities)
        registration_date = fake.date_between(start_date='-8y', end_date='-1y')
        customer_info = {'customer_id':customer_id,
                         'customer_code':customer_code,
                         'customer_name':customer_name,
                         'gender':gender,
                         'age':age,
                         'age_group':age_group,
                         'loyalty_status':loyalty_status,
                         'city':city,
                         'registration_date':registration_date}
        customers.append(customer_info)
    logger.info(f'Генерация клиентов завершена. Создано {len(customers)} клиентов')
    df = pd.DataFrame(customers)
    output_path = os.path.join(parent_dir, "data", "raw", "dim_customers.csv")
    df.to_csv(output_path, index=False)  
    return pd.DataFrame(customers)

if __name__ == "__main__":
    cleanup_logs()
    generate_dim_customers()

   






