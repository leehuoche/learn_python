#!/usr/bin/env python
import pika

credentials = pika.PlainCredentials('guest1', 'guest1')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='192.168.137.128',credentials=credentials))

channel = connection.channel()

channel.exchange_declare(exchange='amq.fanout', exchange_type='fanout',durable=True)

result = channel.queue_declare(queue='sub1', exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='amq.fanout', queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" sub1:%r" % body)

channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True)

channel.start_consuming()