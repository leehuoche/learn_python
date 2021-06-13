#!/usr/bin/env python
import pika
import sys

credentials = pika.PlainCredentials('guest1', 'guest1')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='192.168.137.128',credentials=credentials))

channel = connection.channel()

channel.exchange_declare(exchange='amq.fanout', exchange_type='fanout',durable=True)


for i in range(10):
    message ="pub info: Hello World: "+str(i)
    channel.basic_publish(exchange='amq.fanout', routing_key='', body=message)
    print(" [x] Sent %r" % message)
connection.close()