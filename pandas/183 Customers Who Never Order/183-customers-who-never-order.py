import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = customers.merge(orders, left_on="id", right_on="customerId", how="left")
    noorders = df[df["id_y"].isna()]
    df = noorders.rename(columns={"name":"Customers"})
    return df