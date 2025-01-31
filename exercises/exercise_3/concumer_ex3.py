from quixstreams import Application

app = Application(
    broker_address="localhost:9092",
    consumer_group="order-splitter",
    auto_offset_reset="earliest",
)

order_topic = app.topic(name="orders", value_deserializer="json")

sdf = app.dataframe(topic=order_topic)

def order_output(orders_data):
    print(f"Input: {orders_data}")
    total_price = 0
    for p in orders_data["products"]:
        print(f"Product: {p["name"]} Quantity: {p["quantity"]} Price: {p["price"]}")
        total_price = p["quantity"] * p["price"] + total_price
    print(f"Total price: {total_price:.2f}")
    print("")

sdf = sdf.update(order_output)

if __name__ == "__main__":
    app.run()