from pathlib import Path
import json
from pprint import pprint
from quixstreams import Application

data_path = Path(__file__).parent / "data"

with open(data_path / "orders.json", "r") as file:
    orders = json.load(file)

app = Application(broker_address="localhost:9092", consumer_group="order-splitter")

order_topic = app.topic(name= "orders", value_serializer="json")

def main():
    with app.get_producer() as producer:
        for order in orders:
            kafka_meg = order_topic.serialize(key=order["order_id"], value=order)
            print(f"Preduced  message: key = {kafka_meg.key} value = {kafka_meg.value}")
            producer.produce(
                topic="orders", key= str(kafka_meg.key), value=kafka_meg.value
            )
            

if __name__ == "__main__":
    main()