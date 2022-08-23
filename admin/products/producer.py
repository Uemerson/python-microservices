import pika
import os
from dotenv import load_dotenv

load_dotenv()

params = pika.URLParameters(os.environ.get('AMQP_URI'))

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish():
    channel.basic_publish(exchange='', routing_key='main', body=str.encode('hello'))
