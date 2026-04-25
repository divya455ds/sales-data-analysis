import pandas as pd

# STEP 1: Load dataset
df = pd.read_csv("sales_data.csv")

print("📊 FIRST 5 ROWS:")
print(df.head())

# STEP 2: Basic info
print("\n📌 DATA INFO:")
print(df.info())

print("\n📌 SHAPE (rows, columns):", df.shape)

# STEP 3: Handle missing values
print("\n❌ Missing Values Before:")
print(df.isnull().sum())

# Fill missing Quantity with mean
df['Quantity'].fillna(df['Quantity'].mean(), inplace=True)

print("\n✅ Missing Values After:")
print(df.isnull().sum())

# STEP 4: Create Revenue column
df['Revenue'] = df['Quantity'] * df['Price']

# STEP 5: Analysis
total_sales = df['Revenue'].sum()
avg_sales = df['Revenue'].mean()
max_sales = df['Revenue'].max()

# Best-selling product
best_product = df.groupby('Product')['Revenue'].sum().idxmax()

# STEP 6: Report
print("\n📊 SALES REPORT")
print("------------------------")
print(f"Total Sales: ₹{total_sales}")
print(f"Average Sale: ₹{avg_sales}")
print(f"Highest Sale: ₹{max_sales}")
print(f"Best Selling Product: {best_product}")