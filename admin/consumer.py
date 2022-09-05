import pika
import os
import django
from dotenv import load_dotenv
import json

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

from products.models import Product

load_dotenv()

params = pika.URLParameters(os.environ.get("AMQP_URI", ""))

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue="admin")


def callback(ch, method, properties, body):
    print("Received in admin")
    id = json.loads(body)
    print(id)
    product = Product.objects.get(id=id)
    product.likes = product.likes + 1
    product.save()
    print("Product likes increased!")


channel.basic_consume(queue="admin", on_message_callback=callback, auto_ack=True)

print("Started consuming")

channel.start_consuming()
channel.close()
