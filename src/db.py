import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os
from logger import setup_logging

parent_dir = os.path.dirname(os.path.dirname(__file__))
load_dotenv(os.path.join(parent_dir, '.env'))

logger = setup_logging()

class PostgreSQLLoader:
    def __init__(self):
        self.host = os.getenv('host')
        self.port = os.getenv('port')
        self.database = os.getenv('dbname')
        self.user = os.getenv('user')
        self.password = os.getenv('password')
        self.engine = self.create_db_engine()
    
    def create_db_engine(self):
        connection_string = (
            f"postgresql+psycopg2://{self.user}:{self.password}"
            f"@{self.host}:{self.port}/{self.database}")
        engine = create_engine(connection_string)
        logger.info('Соединение к БД успешно установлено')
        return engine
    
    def load_csv(self, filepath, table_name):
        try:
            df = pd.read_csv(filepath)
            df.to_sql(name = table_name,
                    con = self.engine,
                    if_exists='append',
                    index = False,
                    method = 'multi',
                    chunksize=10000)
            logger.info(f'{table_name} загружена в БД: {len(df)} строк.')
        except Exception as e:
            logger.error(f'Ошибка загрузки таблицы {table_name}: {e}')
            raise
    
    def get_row_count(self, table_name):
        query = text(f'SELECT COUNT (*) FROM public.{table_name}')

        with self.engine.connect() as connection:
            result = connection.execute(query)
            count = result.scalar()
        logger.info(f'{table_name}:{count} строк в БД')
        return count
    
    def truncate_tables(self):
        tables = [
            "fact_sales",
            "dim_customers",
            "dim_employees",
            "dim_products",
            "dim_stores",
            "dim_date"
        ]

        with self.engine.begin() as connection:
            for table in tables:
                connection.execute(
                    text(f"TRUNCATE TABLE public.{table} CASCADE")
                )
                logger.info(f"{table} очищена")
            logger.info('Все таблицы успешно очищены')
    
    def close(self):
        self.engine.dispose()
        logger.info('Соединение с БД закрыто')

        
        

