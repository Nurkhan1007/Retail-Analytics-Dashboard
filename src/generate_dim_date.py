import pandas as pd
import configparser
import os
from logger import cleanup_logs, setup_logging

parent_dir = os.path.dirname(os.path.dirname(__file__))
config = configparser.ConfigParser()
config.read(os.path.join(parent_dir, 'config.ini'))
data_creds = config['DATA']
start_date = data_creds['start_date']
end_date = data_creds['end_date']

logger = setup_logging()


def generate_dim_date(start, end):
    logger.info('Старт генерации календаря')
    dates = pd.date_range(start=start, end = end, freq='D')
    df = pd.DataFrame({'date':dates})
    df['year'] = df['date'].dt.year
    df['quarter'] = 'Q' + df['date'].dt.quarter.astype(str)
    df['month'] = df['date'].dt.month
    df['month_name'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['week_day'] = df['date'].dt.day_name()
    df['year_quarter'] = df['year'].astype(str) + '-' + df['quarter'].astype(str)
    df['month_year'] = df['date'].dt.strftime('%Y-%m')
    df['week_number'] = df['date'].dt.isocalendar().week
    df['iso_year'] = df['date'].dt.isocalendar().year
    df['quarter_number'] = df['date'].dt.quarter
    df['days_in_month'] = df['date'].dt.days_in_month
    df['is_weekend'] = df['date'].dt.dayofweek>5
    logger.info(f'Календарь сформирован. Количество строк: {len(df)}')
    output_path = os.path.join(parent_dir, 'data', 'raw', 'dim_date.csv')
    df.to_csv(output_path, index=False)
    logger.info(f"Генерация календаря завершена. Создано {len(df)} дней")
    logger.info(f"Файл сохранен: {output_path}")
    return df

if __name__ == '__main__':
    cleanup_logs()
    generate_dim_date(start_date, end_date)




