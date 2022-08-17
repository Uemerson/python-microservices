import pika

params = pika.URLParameters("amqps://bzosxusq:r0IheCfzOwXA_q16uSvtxxXQnrhApYtz@jackal.rmq.cloudamqp.com/bzosxusq")

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish():
    channel.basic_publish(exchange='', routing_key='main', body='hello')
