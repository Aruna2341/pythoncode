df_customers =df.groupby('CustomersID').agg(
    orders=('InvoiceNO', 'nunique'),
    skus=('StockCode', 'nunique'),
    quantity=('Quantity', 'sum'),
    revenue=('LinePrice', 'sum'),
).reset_index()

df_customers.head()
print(df_,customers)
