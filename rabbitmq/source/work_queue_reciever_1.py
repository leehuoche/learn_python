#!/usr/bin/env python
import pika
import time

credentials = pika.PlainCredentials('guest1', 'guest1')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='192.168.137.128',credentials=credentials))

channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" work queue 1 receive %r" % body.decode())
    time.sleep(5)
    # print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)

channel.start_consuming()