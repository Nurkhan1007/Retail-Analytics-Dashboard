import pandas as pd
import os
from faker import Faker
from logger import setup_logging, cleanup_logs
import random

logger = setup_logging()
parent_dir = os.path.dirname(os.path.dirname(__file__))

employee_structure = {
    'Mall': {
        'Store Manager': (1, 1),
        'Assistant Manager': (1, 2),
        'Senior Sales Associate': (2, 4),
        'Sales Associate': (8, 12),
        'Cashier': (3, 5)
    },

    'Street': {
        'Store Manager': (1, 1),
        'Assistant Manager': (0, 1),
        'Senior Sales Associate': (1, 2),
        'Sales Associate': (4, 7),
        'Cashier': (2, 3)
    },

    'Outlet': {
        'Store Manager': (1, 1),
        'Assistant Manager': (0, 1),
        'Senior Sales Associate': (1, 1),
        'Sales Associate': (3, 5),
        'Cashier': (1, 2)
    }
}

fake = Faker()

def generate_dim_employees():
    logger.info('Начата генерация сотрудников')
    employees = []
    filepath = os.path.join(parent_dir, 'data', 'raw', 'dim_stores.csv')
    df=pd.read_csv(filepath)
    employee_id = 1
    for store in df.itertuples():
        store_id = store.store_id
        store_type = store.store_type
        positions = employee_structure[store_type]
        for position, count_range in positions.items():
            min_count, max_count = count_range
            employees_count = random.randint(min_count, max_count)
            for _ in range(employees_count):
                employee_code = 'EMP_'+f'{employee_id:03d}'
                hire_date = fake.date_between(start_date='-8y', end_date='-1y')
                employee_name = fake.name()
                employee_info = {'employee_id':employee_id,
                                 'employee_code':employee_code,
                                 'employee_name':employee_name,
                                 'position':position,
                                 'hire_date':hire_date,
                                 'store_id':store_id}
                employees.append(employee_info)
                employee_id += 1
    logger.info(f'Генерация сотрудников завершена. Создано {len(employees)} сотрудников')
    df = pd.DataFrame(employees)
    output_path = os.path.join(parent_dir, "data", "raw", "dim_employees.csv")
    df.to_csv(output_path, index=False)    
    return pd.DataFrame(employees)

if __name__ == "__main__":
    cleanup_logs()
    generate_dim_employees()




