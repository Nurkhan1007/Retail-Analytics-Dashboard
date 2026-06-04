import os
import configparser

from generate_dim_date import generate_dim_date
from generate_dim_stores import generate_dim_stores
from generate_dim_products import generate_dim_products
from generate_dim_employees import generate_dim_employees
from generate_dim_customers import generate_dim_customers
from generate_fact_sales import generate_fact_sales
from db import PostgreSQLLoader
from logger import setup_logging

logger = setup_logging()

parent_dir = os.path.dirname(os.path.dirname(__file__))
raw_dir = os.path.join(parent_dir, 'data', 'raw')

config = configparser.ConfigParser()
config.read(os.path.join(parent_dir, 'config.ini'))
data_creds = config['DATA']
start_date = data_creds['start_date']
end_date = data_creds['end_date']


def main():
    logger.info('Запуск Retail Analytics ETL pipeline')

    # 1. Генерация CSV-файлов
    generate_dim_date(start_date, end_date)
    generate_dim_stores()
    generate_dim_products()
    generate_dim_employees()
    generate_dim_customers()
    generate_fact_sales()

    logger.info('Генерация CSV-файлов завершена')

    # 2. Загрузка в PostgreSQL
    loader = PostgreSQLLoader()

    tables = {
        'dim_date': os.path.join(raw_dir, 'dim_date.csv'),
        'dim_stores': os.path.join(raw_dir, 'dim_stores.csv'),
        'dim_products': os.path.join(raw_dir, 'dim_products.csv'),
        'dim_employees': os.path.join(raw_dir, 'dim_employees.csv'),
        'dim_customers': os.path.join(raw_dir, 'dim_customers.csv'),
        'fact_sales': os.path.join(raw_dir, 'fact_sales.csv'),
    }

    try:
        loader.truncate_tables()

        for table_name, filepath in tables.items():
            logger.info(f"Загрузка файла: {filepath}")
            loader.load_csv(filepath, table_name)
            loader.get_row_count(table_name)

        logger.info('Загрузка данных в PostgreSQL успешно завершена')

    finally:
        loader.close()


if __name__ == '__main__':
    main()