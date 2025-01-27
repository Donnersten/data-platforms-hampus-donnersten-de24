from pathlib import Path
import pandas as pd
import json
from pprint import pprint

data_path = Path(__file__).parents[0] / "data"

with open(data_path / "orders.json", "r") as file:
    order_data = json.load(file)

#pprint(order_data)

for order in order_data:
    print(f"Input: {order}")
    total_price = 0
    for p in order["products"]:
        print(f"Product: {p["name"]} Quantity: {p["quantity"]} Price: {p["price"]}")
        total_price = p["quantity"] * p["price"] + total_price
    print(f"Total price: {total_price}:.2f")

    


