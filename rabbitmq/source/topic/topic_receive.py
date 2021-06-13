#!/usr/bin/env python
import pika
import sys

credentials = pika.PlainCredentials('guest1', 'guest1')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='192.168.137.128',credentials=credentials))

channel = connection.channel()

channel.exchange_declare(exchange='amq.topic', exchange_type='topic',durable=True)

result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue

# binding_keys = ["#","kern.*","*.critical"]
binding_keys = ["kern.*"]
# if not binding_keys:
#     sys.stderr.write("Usage: %s [binding_key]...\n" % sys.argv[0])
#     sys.exit(1)

for binding_key in binding_keys:
    channel.queue_bind(
        exchange='amq.topic', queue=queue_name, routing_key=binding_key)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" %r:%r" % (method.routing_key, body))


channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()