import pandas as pd
from pathlib import Path

# 1. Define the data folder
DATA_PATH = Path("data/raw")

# 2. Read orders dataset
orders = pd.read_csv(DATA_PATH / "olist_orders_dataset.csv")

# 3. Display basic information
print("=== ORDERS DATASET ===")

print ("\nRows and Columns:")
print(orders.shape)

print("\nFirst 5 Rows:")
print(orders.head())

print("\nColumn Names:")
print(orders.columns.tolist())

print("\nData Types:")
print(orders.dtypes)

print("\nMissing Values:")
print(orders.isnull().sum())

print("\nDuplicate Rows:")
print(orders.duplicated().sum())


# Analyze order statuses
print("\n=== ORDER STATUS ANALYSIS ===")

print("\nOrders by Status:")
print(orders["order_status"].value_counts())

print("\nMissing Delivery Dates by Status:")
print(
    orders.groupby("order_status")[
        "order_delivered_customer_date"
    ].apply(lambda column: column.isna().sum())
)

print("\nUnique Order IDs:")
print(orders["order_id"].nunique())



# Explore customers and order items
customers = pd.read_csv(
    DATA_PATH / "olist_customers_dataset.csv"
)

items = pd.read_csv(
    DATA_PATH / "olist_order_items_dataset.csv"
)

print("\n=== RELATIONSHIP ANALYSIS ===")

print("\nCustomers:")
print("Rows:", len(customers))
print("Unique customer IDs:", customers["customer_id"].nunique())
print("Unique actual customers:", customers["customer_unique_id"].nunique())

print("\nOrder Items:")
print("Rows:", len(items))
print("Unique orders:", items["order_id"].nunique())
print("Unique products:", items["product_id"].nunique())

print("\nItems per Order:")
print(items.groupby("order_id").size().describe())


# Find orders without items
print("\n=== ORDERS WITHOUT ITEMS ===")

orders_without_items = orders[
    ~orders["order_id"].isin(items["order_id"])
]

print("\nTotal Orders Without Items:")
print(len(orders_without_items))

print("\nStatus Distribution:")
print(orders_without_items["order_status"].value_counts())

print("\nMissing Customer References:")
print(
    (~orders["customer_id"].isin(customers["customer_id"])).sum()
)

# Explore Products Dataset
products = pd.read_csv(DATA_PATH / "olist_products_dataset.csv")

print("\n=== PRODUCTS DATASET ===")
print("Shape:", products.shape)
print("\nColumns:", products.columns.tolist())
print("\nData Types:")
print(products.dtypes)
print("\nMissing Values:")
print(products.isnull().sum())
print("\nUnique Product IDs:", products["product_id"].nunique())
print("Duplicate Product IDs:", products["product_id"].duplicated().sum())


missing_category = products[products["product_category_name"].isna()]

print("\n=== PRODUCTS MISSING CATEGORY ===")
print("Products missing category:", len(missing_category))

print("\nMissing values within these products:")
print(
    missing_category[
        [
            "product_name_lenght",
            "product_description_lenght",
            "product_photos_qty"
        ]
    ].isna().sum()
)

missing_product_refs = ~items["product_id"].isin(products["product_id"])

print("\n=== PRODUCT RELATIONSHIP CHECK ===")
print("Order items with missing product references:", missing_product_refs.sum())


# Explore Sellers Dataset
sellers = pd.read_csv(DATA_PATH / "olist_sellers_dataset.csv")

print("\n=== SELLERS DATASET ===")
print("Shape:", sellers.shape)
print("\nColumns:", sellers.columns.tolist())

print("\nData Types:")
print(sellers.dtypes)

print("\nMissing Values:")
print(sellers.isnull().sum())

print("\nUnique Seller IDs:", sellers["seller_id"].nunique())
print("Duplicate Seller IDs:", sellers["seller_id"].duplicated().sum())
print("\n=== SELLER RELATIONSHIP CHECK ===")

missing_seller_refs = ~items["seller_id"].isin(sellers["seller_id"])

print(
    "Order items with missing seller references:",
    missing_seller_refs.sum()
)


# Explore Order Payments Dataset
payments = pd.read_csv(
    DATA_PATH / "olist_order_payments_dataset.csv"
)

print("\n=== ORDER PAYMENTS DATASET ===")
print("Shape:", payments.shape)
print("\nColumns:", payments.columns.tolist())

print("\nData Types:")
print(payments.dtypes)

print("\nMissing Values:")
print(payments.isnull().sum())

print("\nUnique Order IDs:", payments["order_id"].nunique())
print("Duplicate Order IDs:", payments["order_id"].duplicated().sum())
print("\n=== PAYMENT RELATIONSHIP CHECK ===")

print(
    "Orders without payments:",
    (~orders["order_id"].isin(payments["order_id"])).sum()
)

print(
    "Payments referencing missing orders:",
    (~payments["order_id"].isin(orders["order_id"])).sum()
)

print(
    "Duplicate composite payment keys:",
    payments.duplicated(
        subset=["order_id", "payment_sequential"]
    ).sum()
)

# Explore Order Reviews Dataset
reviews = pd.read_csv(
    DATA_PATH / "olist_order_reviews_dataset.csv"
)

print("\n=== ORDER REVIEWS DATASET ===")
print("Shape:", reviews.shape)
print("\nColumns:", reviews.columns.tolist())

print("\nData Types:")
print(reviews.dtypes)

print("\nMissing Values:")
print(reviews.isnull().sum())

print("\nUnique Review IDs:", reviews["review_id"].nunique())
print("Duplicate Review IDs:", reviews["review_id"].duplicated().sum())

print("\nUnique Order IDs:", reviews["order_id"].nunique())
print("Duplicate Order IDs:", reviews["order_id"].duplicated().sum())

print("\n=== REVIEW RELATIONSHIP CHECK ===")

print(
    "Duplicate review_id + order_id pairs:",
    reviews.duplicated(
        subset=["review_id", "order_id"]
    ).sum()
)

print(
    "Reviews referencing missing orders:",
    (~reviews["order_id"].isin(orders["order_id"])).sum()
)

print(
    "Orders without reviews:",
    (~orders["order_id"].isin(reviews["order_id"])).sum()
)

print(
    "Fully duplicated review rows:",
    reviews.duplicated().sum()
)


# Explore Geolocation Dataset
geo = pd.read_csv(
    DATA_PATH / "olist_geolocation_dataset.csv"
)

print("\n=== GEOLOCATION DATASET ===")
print("Shape:", geo.shape)

print("\nColumns:")
print(geo.columns.tolist())

print("\nData Types:")
print(geo.dtypes)

print("\nMissing Values:")
print(geo.isnull().sum())

print(
    "\nUnique ZIP Code Prefixes:",
    geo["geolocation_zip_code_prefix"].nunique()
)

print(
    "Duplicate ZIP Code Prefixes:",
    geo["geolocation_zip_code_prefix"].duplicated().sum()
)

print(
    "Fully Duplicated Rows:",
    geo.duplicated().sum()
)

print("\n=== GEOLOCATION ZIP DISTRIBUTION ===")

zip_counts = geo["geolocation_zip_code_prefix"].value_counts()

print("Maximum rows for one ZIP prefix:", zip_counts.max())
print("Average rows per ZIP prefix:", zip_counts.mean())

print("\nTop 5 most frequent ZIP prefixes:")
print(zip_counts.head(5))


# Explore Product Category Translation Dataset
translations = pd.read_csv(
    DATA_PATH / "product_category_name_translation.csv"
)

print("\n=== CATEGORY TRANSLATION DATASET ===")
print("Shape:", translations.shape)

print("\nColumns:")
print(translations.columns.tolist())

print("\nData Types:")
print(translations.dtypes)

print("\nMissing Values:")
print(translations.isnull().sum())

print(
    "\nUnique Portuguese Categories:",
    translations["product_category_name"].nunique()
)

print(
    "Duplicate Portuguese Categories:",
    translations["product_category_name"].duplicated().sum()
)

print(
    "\nFully Duplicated Rows:",
    translations.duplicated().sum()
)

print("\n=== CATEGORY TRANSLATION RELATIONSHIP CHECK ===")

missing_translations = products[
    products["product_category_name"].notna()
    & ~products["product_category_name"].isin(
        translations["product_category_name"]
    )
]

print(
    "Products with categories missing translations:",
    len(missing_translations)
)

print(
    "\nUntranslated category names:"
)

print(
    missing_translations["product_category_name"]
    .value_counts()
)