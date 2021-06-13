#!/usr/bin/env python
import pika
import sys

credentials = pika.PlainCredentials('guest1', 'guest1')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='192.168.137.128',credentials=credentials))

channel = connection.channel()

channel.exchange_declare(exchange='amq.direct', exchange_type='direct',durable=True)

result = channel.queue_declare(queue='route_sub_error', exclusive=True)
queue_name = result.method.queue

# severities = sys.argv[1:]
# if not severities:
#     sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
#     sys.exit(1)
#
# for severity in severities:
#     channel.queue_bind(
#         exchange='amq.direct', queue=queue_name, routing_key=severity)

channel.queue_bind(
        exchange='amq.direct', queue=queue_name, routing_key="error")

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))


channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()