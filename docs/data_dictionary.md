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