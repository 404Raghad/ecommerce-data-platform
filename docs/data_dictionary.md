# E-Commerce Data Platform - Data Dictionary

## 1. Orders

Source: olist_orders_dataset.csv
Total Rows: 99,441
Primary Key: order_id

| Column | Description |
|---|---|
| order_id | Unique identifier for each order |
| customer_id | Customer record associated with the order |
| order_status | Current order status |
| order_purchase_timestamp | Date and time the order was placed |
| order_approved_at | Date and time the order was approved |
| order_delivered_carrier_date | Date the order was handed to the carrier |
| order_delivered_customer_date | Actual customer delivery date |
| order_estimated_delivery_date | Estimated delivery date |

## 2. Customers

Source: olist_customers_dataset.csv
Total Rows: 99,441
Primary Key: customer_id

| Column | Description |
|---|---|
| customer_id | Unique customer record identifier |
| customer_unique_id | Identifies the same customer across orders |
| customer_zip_code_prefix | Customer ZIP code prefix |
| customer_city | Customer city |
| customer_state | Customer state |

## 3. Order Items

Source: olist_order_items_dataset.csv
Total Rows: 112,650
Composite Primary Key: (order_id, order_item_id)

| Column | Description |
|---|---|
| order_id | Associated order identifier |
| order_item_id | Sequential item number within an order |
| product_id | Product identifier |
| seller_id | Seller identifier |
| shipping_limit_date | Shipping deadline |
| price | Item price |
| freight_value | Freight cost |

## 4. Relationships

Orders.customer_id -> Customers.customer_id

Order Items.order_id -> Orders.order_id

Order Items.product_id -> Products.product_id
(Not yet validated)

Order Items.seller_id -> Sellers.seller_id
(Not yet validated)

One order can contain multiple order items.

## 5. Data Quality Findings

### Orders

Total orders: 99,441
Unique order IDs: 99,441
Duplicate rows: 0

Missing values:
- order_approved_at: 160
- order_delivered_carrier_date: 1,783
- order_delivered_customer_date: 2,965

Delivered orders missing delivery date: 8
Canceled orders with delivery date: 6

### Customers

Total customer records: 99,441
Unique customer IDs: 99,441
Unique actual customers: 96,096

Missing customer references from Orders: 0

### Order Items

Total item records: 112,650
Unique orders: 98,666
Unique products: 32,951
Maximum items in one order: 21

### Orders Without Items

Total: 775

| Status | Count |
|---|---|
| unavailable | 603 |
| canceled | 164 |
| created | 5 |
| invoiced | 2 |
| shipped | 1 |

## 6. Data Quality Notes

- Missing delivery dates can be normal for undelivered orders.
- Delivered orders without delivery dates need investigation.
- Canceled orders with delivery dates need investigation.
- Orders without items should not be deleted automatically.
- Timestamp columns need conversion from strings to datetime.
- Raw datasets must remain unchanged.

## 7. Next Steps

- Explore the remaining six datasets.
- Validate primary and foreign keys.
- Check missing values and duplicates.
- Prepare the PostgreSQL database schema.

## 8. Products

Source: olist_products_dataset.csv
Total Rows: 32,951
Primary Key Candidate: product_id

| Column | Description |
|---|---|
| product_id | Unique product identifier |
| product_category_name | Product category |
| product_name_lenght | Number of characters in product name |
| product_description_lenght | Number of characters in product description |
| product_photos_qty | Number of product photos |
| product_weight_g | Product weight in grams |
| product_length_cm | Product length in centimeters |
| product_height_cm | Product height in centimeters |
| product_width_cm | Product width in centimeters |

### Data Quality Findings

- Unique product IDs: 32,951
- Duplicate product IDs: 0
- Missing product categories: 610
- The same 610 products also have missing name length,
  description length, and photo quantity.
- Missing product weights: 2
- Missing product lengths: 2
- Missing product heights: 2
- Missing product widths: 2
- Order items with missing product references: 0

### Notes

- product_id is a valid primary key candidate.
- The relationship from Order Items to Products was validated.
- Missing product metadata should be investigated before cleaning.
- The source columns use "lenght" instead of "length".

## 9. Sellers

Source: olist_sellers_dataset.csv
Total Rows: 3,095
Primary Key Candidate: seller_id

| Column | Description |
|---|---|
| seller_id | Unique seller identifier |
| seller_zip_code_prefix | Seller ZIP code prefix |
| seller_city | Seller city |
| seller_state | Seller state |

### Data Quality Findings

- Unique seller IDs: 3,095
- Duplicate seller IDs: 0
- Missing values: 0
- Order items with missing seller references: 0

### Notes

- seller_id is a valid primary key candidate.
- The relationship from Order Items to Sellers was validated.
- ZIP code prefixes were read as integers but may be better
  represented as strings to preserve leading zeros.

  ## 10. Order Payments

Source: olist_order_payments_dataset.csv
Total Rows: 103,886
Composite Primary Key: (order_id, payment_sequential)

| Column | Description |
|---|---|
| order_id | Associated order identifier |
| payment_sequential | Sequential payment number within an order |
| payment_type | Payment method |
| payment_installments | Number of payment installments |
| payment_value | Payment amount |

### Data Quality Findings

- Total payment records: 103,886
- Unique order IDs: 99,440
- Additional rows sharing an existing order ID: 4,446
- Missing values: 0
- Duplicate composite payment keys: 0
- Orders without payment records: 1
- Payments referencing missing orders: 0

### Notes

- One order can have multiple payment records.
- order_id alone is not unique in this table.
- (order_id, payment_sequential) is a valid primary key candidate.
- The order without a payment record requires further investigation.


## 11. Order Reviews

Source: olist_order_reviews_dataset.csv
Total Rows: 99,224
Composite Primary Key Candidate: (review_id, order_id)

| Column | Description |
|---|---|
| review_id | Review identifier |
| order_id | Associated order identifier |
| review_score | Customer rating score |
| review_comment_title | Optional review title |
| review_comment_message | Optional review message |
| review_creation_date | Review creation date |
| review_answer_timestamp | Timestamp when the review was submitted |

### Data Quality Findings

- Total review records: 99,224
- Unique review IDs: 98,410
- Unique order IDs: 98,673
- Duplicate review IDs beyond first occurrence: 814
- Duplicate order IDs beyond first occurrence: 551
- Duplicate (review_id, order_id) pairs: 0
- Fully duplicated rows: 0
- Missing review titles: 87,656
- Missing review messages: 58,247
- Reviews referencing missing orders: 0
- Orders without reviews: 768

### Notes

- review_id alone is not unique in this dataset.
- (review_id, order_id) is a valid composite primary key candidate.
- Review titles and messages may be optional.
- Missing review text should not automatically cause row deletion.
- Date columns need conversion from strings to datetime.


## 12. Geolocation

Source: olist_geolocation_dataset.csv
Total Rows: 1,000,163
Primary Key: Not identified in the raw dataset

| Column | Description |
|---|---|
| geolocation_zip_code_prefix | Geographic ZIP code prefix |
| geolocation_lat | Latitude coordinate |
| geolocation_lng | Longitude coordinate |
| geolocation_city | City name |
| geolocation_state | State abbreviation |

### Data Quality Findings

- Total rows: 1,000,163
- Unique ZIP code prefixes: 19,015
- Repeated ZIP prefix occurrences beyond first: 981,148
- Fully duplicated rows: 261,831
- Missing values: 0
- Maximum rows per ZIP prefix: 1,146
- Average rows per ZIP prefix: 52.6
- Most frequent ZIP prefix: 24220 (1,146 rows)

### Notes

- ZIP code prefixes are not unique.
- Direct joins using ZIP code prefixes may cause join fanout.
- A future transformation may create one representative
  geographic record per ZIP code prefix.
- ZIP code prefixes should be treated as identifiers,
  not numerical measurements.
- Raw geographic records must remain unchanged.

## 13. Product Category Translation

Source: product_category_name_translation.csv
Total Rows: 71
Primary Key Candidate: product_category_name

| Column | Description |
|---|---|
| product_category_name | Original Portuguese category name |
| product_category_name_english | English category name |

### Data Quality Findings

- Total translation records: 71
- Unique Portuguese categories: 71
- Duplicate Portuguese categories: 0
- Fully duplicated rows: 0
- Missing values: 0

### Relationship Validation

- Products with missing category names: 610
- Products with categories missing translations: 13
- Untranslated categories:
  - portateis_cozinha_e_preparadores_de_alimentos: 10 products
  - pc_gamer: 3 products
- Total products without an available English category: 623

### Notes

- product_category_name is a valid primary key candidate.
- Multiple products can belong to the same category.
- INNER JOIN would exclude products without matching translations.
- LEFT JOIN can preserve all products during analysis.
- Missing category names and missing translations
  should be treated as separate data quality issues.