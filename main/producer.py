import pika
import json
import os
from dotenv import load_dotenv

load_dotenv()

params = pika.URLParameters(os.environ.get("AMQP_URI", ""))

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(
        exchange="",
        routing_key="admin",
        body=json.dumps(body).encode(),
        properties=properties,
    )
