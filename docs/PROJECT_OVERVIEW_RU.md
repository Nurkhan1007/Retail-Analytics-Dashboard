# PROJECT_OVERVIEW_RU.md

# Retail Analytics Dashboard

## Описание проекта

Retail Analytics Dashboard — аналитический проект полного цикла, демонстрирующий навыки работы с данными от генерации и хранения до визуализации и анализа в Power BI.

Проект построен на синтетическом наборе данных розничной сети магазинов товаров для дома.

---

# Цели проекта

* Построение аналитического хранилища данных
* Реализация звездной схемы (Star Schema)
* Автоматизация генерации данных
* Загрузка данных в PostgreSQL
* Создание интерактивного Power BI дашборда
* Демонстрация навыков Data Analytics и Business Intelligence

---

# Используемый стек технологий

## Data Generation

* Python
* Pandas
* NumPy

## Data Storage

* PostgreSQL

## BI & Visualization

* Power BI
* DAX
* Power Query

## Version Control

* Git
* GitHub

---

# Архитектура проекта

CSV Files
↓
Python ETL
↓
PostgreSQL
↓
Power BI
↓
Interactive Dashboard

---

# Модель данных

Проект реализован по схеме Star Schema.

Fact Table:

* FactSales

Dimension Tables:

* DimDate
* DimStores
* DimProducts
* DimEmployees
* DimCustomers

---

# Основные показатели

* Revenue
* Profit
* Margin
* Quantity Sold
* Average Order Value
* Customer Segmentation
* Product Performance
* Store Performance

---

# Планируемые аналитические блоки

## Executive Dashboard

Общие показатели бизнеса.

## Sales Dashboard

Анализ продаж во времени.

## Product Analytics

Анализ категорий, брендов и товаров.

## Customer Analytics

Анализ клиентов и сегментация.

## Store Performance

Сравнение эффективности магазинов.

## Time Intelligence

* YTD
* MTD
* QTD
* YoY
* Rolling 12 Months

---

# Размер данных

* 200 000 продаж
* 30 000 клиентов
* 400 товаров
* ~350–450 сотрудников (генерируется динамически)
* 30 магазинов
* 1096 календарных дней
