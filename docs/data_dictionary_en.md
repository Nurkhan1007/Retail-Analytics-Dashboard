# DATA_DICTIONARY_EN.md

# Data Dictionary

## FactSales

### Description

Fact table containing sales and return transactions generated for the retail analytics project.

| Column          | Data Type | Description                                     |
| --------------- | --------- | ----------------------------------------------- |
| sale_id         | INTEGER   | Unique transaction identifier                   |
| sale_date       | DATE      | Transaction date                                |
| store_id        | INTEGER   | Store identifier                                |
| employee_id     | INTEGER   | Employee identifier                             |
| product_id      | INTEGER   | Product identifier                              |
| customer_id     | INTEGER   | Customer identifier                             |
| quantity        | INTEGER   | Quantity sold. Negative values indicate returns |
| unit_price      | DECIMAL   | Selling price per unit                          |
| unit_cost       | DECIMAL   | Cost per unit                                   |
| discount_pct    | DECIMAL   | Discount percentage applied to the transaction  |
| discount_amount | DECIMAL   | Total discount amount                           |
| revenue         | DECIMAL   | Net revenue after discount                      |
| cost            | DECIMAL   | Cost of goods sold                              |
| profit          | DECIMAL   | Gross profit                                    |
| payment_method  | VARCHAR   | Payment method (Card, Cash, Online)             |
| is_return       | BOOLEAN   | Return transaction flag                         |

---

## DimProducts

### Description

Product dimension containing product hierarchy and pricing information.

| Column        | Data Type | Description                               |
| ------------- | --------- | ----------------------------------------- |
| product_id    | INTEGER   | Unique product identifier                 |
| product_code  | VARCHAR   | Product code                              |
| product_name  | VARCHAR   | Product name                              |
| category      | VARCHAR   | Product category                          |
| subcategory   | VARCHAR   | Product subcategory                       |
| brand         | VARCHAR   | Product brand                             |
| brand_segment | VARCHAR   | Brand segment (Budget, Standard, Premium) |
| unit_price    | DECIMAL   | Base product price                        |
| margin_pct    | DECIMAL   | Product margin percentage                 |
| unit_cost     | DECIMAL   | Product cost                              |

---

## DimStores

### Description

Store dimension containing information about retail locations.

| Column             | Data Type | Description                         |
| ------------------ | --------- | ----------------------------------- |
| store_id           | INTEGER   | Unique store identifier             |
| store_code         | VARCHAR   | Store code                          |
| store_name         | VARCHAR   | Store name                          |
| region             | VARCHAR   | Store region                        |
| city               | VARCHAR   | Store city                          |
| store_type         | VARCHAR   | Store format (Mall, Street, Outlet) |
| performance_factor | DECIMAL   | Store performance coefficient       |

---

## DimEmployees

### Description

Employee dimension containing information about store personnel.

| Column        | Data Type | Description                |
| ------------- | --------- | -------------------------- |
| employee_id   | INTEGER   | Unique employee identifier |
| employee_code | VARCHAR   | Employee code              |
| employee_name | VARCHAR   | Employee full name         |
| position      | VARCHAR   | Employee position          |
| hire_date     | DATE      | Employment start date      |
| store_id      | INTEGER   | Assigned store identifier  |

---

## DimCustomers

### Description

Customer dimension containing demographic and loyalty information.

| Column            | Data Type | Description                |
| ----------------- | --------- | -------------------------- |
| customer_id       | INTEGER   | Unique customer identifier |
| customer_code     | VARCHAR   | Customer code              |
| customer_name     | VARCHAR   | Customer name              |
| gender            | VARCHAR   | Customer gender            |
| age               | INTEGER   | Customer age               |
| age_group         | VARCHAR   | Customer age segment       |
| loyalty_status    | VARCHAR   | Loyalty program level      |
| city              | VARCHAR   | Customer city              |
| registration_date | DATE      | Customer registration date |

---

## DimDate

### Description

Calendar dimension used for time intelligence analysis.

| Column         | Data Type | Description             |
| -------------- | --------- | ----------------------- |
| date           | DATE      | Calendar date           |
| year           | INTEGER   | Calendar year           |
| quarter        | VARCHAR   | Quarter label           |
| month          | INTEGER   | Month number            |
| month_name     | VARCHAR   | Month name              |
| day            | INTEGER   | Day of month            |
| week_day       | VARCHAR   | Weekday name            |
| year_quarter   | VARCHAR   | Year and quarter        |
| month_year     | VARCHAR   | Month and year          |
| week_number    | INTEGER   | ISO week number         |
| iso_year       | INTEGER   | ISO year                |
| quarter_number | INTEGER   | Quarter number          |
| days_in_month  | INTEGER   | Number of days in month |
| is_weekend     | BOOLEAN   | Weekend flag            |
