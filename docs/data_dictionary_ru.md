# Словарь данных (Data Dictionary)

## FactSales

### Описание

Таблица фактов, содержащая информацию о продажах и возвратах товаров в магазинах розничной сети.

| Поле            | Тип     | Описание                                                                 |
| --------------- | ------- | ------------------------------------------------------------------------ |
| sale_id         | INTEGER | Уникальный идентификатор продажи                                         |
| sale_date       | DATE    | Дата продажи                                                             |
| store_id        | INTEGER | Идентификатор магазина                                                   |
| employee_id     | INTEGER | Идентификатор сотрудника                                                 |
| product_id      | INTEGER | Идентификатор товара                                                     |
| customer_id     | INTEGER | Идентификатор клиента                                                    |
| quantity        | INTEGER | Количество проданных единиц товара. Для возвратов значение отрицательное |
| unit_price      | DECIMAL | Цена продажи одной единицы товара                                        |
| unit_cost       | DECIMAL | Себестоимость одной единицы товара                                       |
| discount_pct    | DECIMAL | Размер скидки в процентах                                                |
| discount_amount | DECIMAL | Сумма предоставленной скидки                                             |
| revenue         | DECIMAL | Выручка от продажи после применения скидки                               |
| cost            | DECIMAL | Себестоимость реализованного товара                                      |
| profit          | DECIMAL | Валовая прибыль                                                          |
| payment_method  | VARCHAR | Способ оплаты (Card, Cash, Online)                                       |
| is_return       | BOOLEAN | Признак возврата товара                                                  |

---

## DimProducts

### Описание

Справочник товаров.

| Поле          | Тип     | Описание                                           |
| ------------- | ------- | -------------------------------------------------- |
| product_id    | INTEGER | Уникальный идентификатор товара                    |
| product_code  | VARCHAR | Код товара                                         |
| product_name  | VARCHAR | Наименование товара                                |
| category      | VARCHAR | Категория товара                                   |
| subcategory   | VARCHAR | Подкатегория товара                                |
| brand         | VARCHAR | Бренд                                              |
| brand_segment | VARCHAR | Ценовой сегмент бренда (Budget, Standard, Premium) |
| unit_price    | DECIMAL | Базовая цена товара                                |
| margin_pct    | DECIMAL | Маржинальность товара                              |
| unit_cost     | DECIMAL | Себестоимость товара                               |

---

## DimStores

### Описание

Справочник магазинов.

| Поле               | Тип     | Описание                            |
| ------------------ | ------- | ----------------------------------- |
| store_id           | INTEGER | Уникальный идентификатор магазина   |
| store_code         | VARCHAR | Код магазина                        |
| store_name         | VARCHAR | Наименование магазина               |
| region             | VARCHAR | Регион расположения магазина        |
| city               | VARCHAR | Город                               |
| store_type         | VARCHAR | Тип магазина (Mall, Street, Outlet) |
| performance_factor | DECIMAL | Коэффициент эффективности магазина  |

---

## DimEmployees

### Описание

Справочник сотрудников.

| Поле          | Тип     | Описание                                |
| ------------- | ------- | --------------------------------------- |
| employee_id   | INTEGER | Уникальный идентификатор сотрудника     |
| employee_code | VARCHAR | Код сотрудника                          |
| employee_name | VARCHAR | Имя сотрудника                          |
| position      | VARCHAR | Должность                               |
| hire_date     | DATE    | Дата приема на работу                   |
| store_id      | INTEGER | Магазин, к которому закреплен сотрудник |

---

## DimCustomers

### Описание

Справочник клиентов.

| Поле              | Тип     | Описание                         |
| ----------------- | ------- | -------------------------------- |
| customer_id       | INTEGER | Уникальный идентификатор клиента |
| customer_code     | VARCHAR | Код клиента                      |
| customer_name     | VARCHAR | Имя клиента                      |
| gender            | VARCHAR | Пол клиента                      |
| age               | INTEGER | Возраст клиента                  |
| age_group         | VARCHAR | Возрастная группа                |
| loyalty_status    | VARCHAR | Уровень программы лояльности     |
| city              | VARCHAR | Город проживания                 |
| registration_date | DATE    | Дата регистрации клиента         |

---

## DimDate

### Описание

Календарное измерение для анализа временных рядов.

| Поле           | Тип     | Описание                 |
| -------------- | ------- | ------------------------ |
| date           | DATE    | Дата                     |
| year           | INTEGER | Год                      |
| quarter        | VARCHAR | Квартал                  |
| month          | INTEGER | Номер месяца             |
| month_name     | VARCHAR | Название месяца          |
| day            | INTEGER | День месяца              |
| week_day       | VARCHAR | День недели              |
| year_quarter   | VARCHAR | Год и квартал            |
| month_year     | VARCHAR | Месяц и год              |
| week_number    | INTEGER | Номер недели ISO         |
| iso_year       | INTEGER | ISO год                  |
| quarter_number | INTEGER | Номер квартала           |
| days_in_month  | INTEGER | Количество дней в месяце |
| is_weekend     | BOOLEAN | Признак выходного дня    |
