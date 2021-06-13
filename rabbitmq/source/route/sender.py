#!/usr/bin/env python
import pika
import sys

credentials = pika.PlainCredentials('guest1', 'guest1')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='192.168.137.128',credentials=credentials))

channel = connection.channel()

channel.exchange_declare(exchange='amq.direct', exchange_type='direct',durable=True)


for i in range(1,10):
    if i%2==0:
        ss="error"
    else:
        ss="info"

    severity = ss
    message = severity+'Hello World!'
    channel.basic_publish(
        exchange='amq.direct', routing_key=severity, body=message)
    print(" [x] Sent %r:%r" % (severity, message))


connection.close()