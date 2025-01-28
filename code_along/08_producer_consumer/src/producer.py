from pathlib import Path
import json
from pprint import pprint
from quixstreams import Application

# .parents[1] = [1] = hamna i 08_producer_costumer [0] = src mappen
data_path = Path(__file__).parents[1] / "data"
#print(data_path)

# Läser in json filen
with open(data_path / "jokes.json", "r") as file:
    jokes = json.load(file)

#pprint(jokes)

# En form av öppning av kafka, localhost:9092 är som en port mot broker container 
app = Application(broker_address="localhost:9092", consumer_group="text-splitter")

jokes_topic = app.topic(name= "jokes", value_serializer="json")

#print(jokes_topic)

def main():
    with app.get_producer() as producer:
        #print(producer)

        for joke in jokes:
            kafka_meg = jokes_topic.serialize(key=joke["joke_id"], value=joke)

            print(f"Preduced  message: key = {kafka_meg.key} value = {kafka_meg.value}")

            producer.produce(
                topic="jokes", key= str(kafka_meg.key), value=kafka_meg.value
            )
            

if __name__ == "__main__":
    #pprint(jokes)
    main()