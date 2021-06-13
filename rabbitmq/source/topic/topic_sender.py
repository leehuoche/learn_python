#!/usr/bin/env python
import pika
import sys

credentials = pika.PlainCredentials('guest1', 'guest1')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='192.168.137.128',credentials=credentials))

channel = connection.channel()

channel.exchange_declare(exchange='amq.topic', exchange_type='topic',durable=True)


msg=["kern.critical", "A critical kernel error"]
binding_keys = ["kern.critical", "A critical kernel error"]
zipaa=zip(msg,binding_keys)
for i,routing_key in zipaa:
    # routing_key = sys.argv[1] if len(sys.argv) > 2 else 'anonymous.info'
    message = i
    channel.basic_publish(
        exchange='amq.topic', routing_key=routing_key, body=message)

    print(" [x] Sent %r:%r" % (routing_key, message))


connection.close()