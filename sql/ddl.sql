'Создаем таблицу dim_date'
CREATE TABLE public.dim_date (
	"date" date NOT NULL,
	"year" int4 NOT NULL,
	quarter varchar NOT NULL,
	"month" int4 NOT NULL,
	month_name varchar NOT NULL,
	"day" int4 NOT NULL,
	week_day varchar NOT NULL,
	year_quarter varchar NOT NULL,
	month_year varchar NOT NULL,
	week_number int4 NOT NULL,
	iso_year int4 NOT NULL,
	quarter_number int4 NOT NULL,
	days_in_month int4 NOT NULL,
	is_weekend bool NOT NULL,
	CONSTRAINT dim_date_pkey PRIMARY KEY (date)
);
'Создаем таблицу dim_stores'
CREATE TABLE public.dim_stores (
    store_id INT4 NOT NULL,
    store_code VARCHAR NOT NULL,
    store_name VARCHAR NOT NULL,
    region VARCHAR NOT NULL,
    city VARCHAR NOT NULL,
    store_type VARCHAR NOT NULL,
    performance_factor NUMERIC(4,2) NOT NULL,
    CONSTRAINT dim_stores_pkey PRIMARY KEY (store_id)
);

'Создаем таблицу dim_products'
CREATE TABLE public.dim_products (
    product_id INT4 NOT NULL,
    product_code VARCHAR(20) NOT NULL,
    product_name VARCHAR(200) NOT NULL,
    category VARCHAR(50) NOT NULL,
    subcategory VARCHAR(50) NOT NULL,
    brand VARCHAR(50) NOT NULL,
    brand_segment VARCHAR(20) NOT NULL,
    unit_price NUMERIC(10,2) NOT NULL,
    margin_pct NUMERIC(5,2) NOT NULL,
    unit_cost NUMERIC(10,2) NOT NULL,
    CONSTRAINT dim_products_pkey PRIMARY KEY (product_id)
);

'Создаем таблицу dim_employees'
CREATE TABLE public.dim_employees (
    employee_id INT4 NOT NULL,
    employee_code VARCHAR NOT NULL,
    employee_name VARCHAR NOT NULL,
    position VARCHAR NOT NULL,
    hire_date DATE NOT NULL,
    store_id INT4 NOT NULL,
    CONSTRAINT dim_employees_pkey PRIMARY KEY (employee_id),
    CONSTRAINT fk_employees_store
        FOREIGN KEY (store_id)
        REFERENCES public.dim_stores(store_id)
);

'Создаем таблицу dim_customers'
CREATE TABLE public.dim_customers (
    customer_id INT4 NOT NULL,
    customer_code VARCHAR NOT NULL,
    customer_name VARCHAR NOT NULL,
    gender VARCHAR NOT NULL,
    age INT4 NOT NULL,
    age_group VARCHAR NOT NULL,
    loyalty_status VARCHAR NOT NULL,
    city VARCHAR NOT NULL,
    registration_date DATE NOT NULL,
    CONSTRAINT dim_customers_pkey PRIMARY KEY (customer_id)
);

'Создаем таблицу fact_sales'
CREATE TABLE public.fact_sales (
    sale_id INT4 NOT NULL,
    sale_date DATE NOT NULL,
    store_id INT4 NOT NULL,
    employee_id INT4 NOT NULL,
    product_id INT4 NOT NULL,
    customer_id INT4 NOT NULL,
    quantity INT4 NOT NULL,
    unit_price NUMERIC(10,2) NOT NULL,
    unit_cost NUMERIC(10,2) NOT NULL,
    discount_pct NUMERIC(5,2) NOT NULL,
    discount_amount NUMERIC(10,2) NOT NULL,
    revenue NUMERIC(12,2) NOT NULL,
    cost NUMERIC(12,2) NOT NULL,
    profit NUMERIC(12,2) NOT NULL,
    payment_method VARCHAR(20) NOT NULL,
    is_return BOOLEAN NOT NULL,
    CONSTRAINT fact_sales_pkey PRIMARY KEY (sale_id),
    CONSTRAINT fk_sales_date
        FOREIGN KEY (sale_date)
        REFERENCES public.dim_date(date),
    CONSTRAINT fk_sales_store
        FOREIGN KEY (store_id)
        REFERENCES public.dim_stores(store_id),
    CONSTRAINT fk_sales_employee
        FOREIGN KEY (employee_id)
        REFERENCES public.dim_employees(employee_id),
    CONSTRAINT fk_sales_product
        FOREIGN KEY (product_id)
        REFERENCES public.dim_products(product_id),
    CONSTRAINT fk_sales_customer
        FOREIGN KEY (customer_id)
        REFERENCES public.dim_customers(customer_id)
);