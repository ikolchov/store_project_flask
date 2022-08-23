import pandas as pd

from db import db


def pd_file_generator(file_dir, star_date, end_date):

    sold_item_query = 'select * from "user_products_logger"'
    item_info_query = 'select * from "products"'
    engine = db.engine.connect().connection
    sold_items = pd.read_sql_query(sold_item_query, con=engine)
    item_info = pd.read_sql_query(item_info_query, con=engine)
    df = pd.merge(item_info, sold_items, left_on='id', right_on='item_id')
    df['order_create_date'] = pd.to_datetime(df['order_create_date'])
    mask = (df['order_create_date'] >= star_date) & (df['order_create_date'] <= end_date)
    df = df.loc[mask]
    headers = ['order_create_date', "product_group", "brand", "model", 'sku', 'qty', 'price_x', 'discount']
    exporting_headers = ['sold on', 'pg', 'brand', 'model', 'sku', 'quantity', 'price', 'discount']
    df = df[headers]
    df.columns = exporting_headers
    summary_sales = df
    best_selling_products = df.groupby(['pg', 'brand'])['quantity'].sum()
    #
    with pd.ExcelWriter(file_dir) as w:
        best_selling_products.to_excel(w, sheet_name="top selling")
        summary_sales.to_excel(w, sheet_name='summary', index=False)