# DATA_QUALITY_REPORT_EN.md

# Data Quality Report

## Project

Retail Analytics Dashboard

## Validation Date

June 1, 2026

---

# Scope

The purpose of this validation process was to verify the integrity, consistency, completeness, and business correctness of the generated retail dataset before loading it into PostgreSQL and building Power BI dashboards.

The following tables were validated:

* DimDate
* DimStores
* DimProducts
* DimEmployees
* DimCustomers
* FactSales

---

# Dataset Summary

| Table        |    Rows |
| ------------ | ------: |
| DimDate      |   1,096 |
| DimStores    |      30 |
| DimProducts  |     400 |
| DimEmployees |     416 |
| DimCustomers |  30,000 |
| FactSales    | 200,000 |

---

# Validation Results

## Primary Key Validation

All primary key columns were checked for uniqueness.

| Table        | Result |
| ------------ | ------ |
| DimDate      | PASS   |
| DimStores    | PASS   |
| DimProducts  | PASS   |
| DimEmployees | PASS   |
| DimCustomers | PASS   |
| FactSales    | PASS   |

No duplicate primary keys were detected.

---

## Missing Values Validation

All tables were checked for null and missing values.

Result: PASS

No missing values were found in any table.

---

## Referential Integrity Validation

Foreign key relationships between FactSales and dimension tables were verified.

Validated relationships:

* FactSales.sale_date → DimDate.date
* FactSales.store_id → DimStores.store_id
* FactSales.product_id → DimProducts.product_id
* FactSales.employee_id → DimEmployees.employee_id
* FactSales.customer_id → DimCustomers.customer_id

Result: PASS

No orphan records were identified.

---

## Business Logic Validation

The following business rules were verified:

### Returns Validation

* Sales transactions contain positive quantities.
* Return transactions contain negative quantities.
* No inconsistencies were detected.

Result: PASS

### Revenue Calculation Validation

Revenue values were compared against the following formula:

Revenue = Quantity × Unit Price − Discount Amount

Result: PASS

No calculation discrepancies were found.

### Profit Calculation Validation

Profit values were compared against the following formula:

Profit = Revenue − Cost

Result: PASS

No calculation discrepancies were found.

### Payment Method Distribution

Observed distribution:

* Card ≈ 65%
* Cash ≈ 20%
* Online ≈ 15%

Distribution matches expected business assumptions.

Result: PASS

### Seasonality Validation

Sales distribution was analyzed by month.

Key findings:

* Strong seasonal pattern observed.
* December is the highest-performing month.
* Monthly distribution follows the intended retail seasonality model.

Result: PASS

---

# Overall Assessment

The dataset successfully passed all quality validation checks.

The data is considered:

* Complete
* Consistent
* Accurate
* Referentially valid
* Business-rule compliant

The dataset is approved for:

* PostgreSQL data warehouse loading
* Star schema implementation
* Power BI reporting and dashboard development

Status: APPROVED
