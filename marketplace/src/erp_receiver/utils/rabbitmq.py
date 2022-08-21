from typing import Callable

import pika
from pika.adapters.blocking_connection import BlockingChannel
from pika.spec import Basic, BasicProperties

from market_place.settings import AMQP_URL


class RabbitMQClient:
    def __init__(self):
        url = AMQP_URL
        self.parameters = pika.URLParameters(url)

    def __enter__(self):
        # self.connection = pika.BlockingConnection(pika.ConnectionParameters('127.0.0.1'))
        self.connection = pika.BlockingConnection(self.parameters)
        self.channel = self.connection.channel()

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.channel.close()
        self.connection.close()


class MessageReciever(RabbitMQClient):
    def get_message(self, queue):
        method_frame, header_frame, body = self.channel.basic_get(queue)
        if method_frame:
            self.channel.basic_ack(method_frame.delivery_tag)
            return method_frame, header_frame, body

    def consume_messages(
            self,
            queue,
            callback: Callable[
                [BlockingChannel, Basic.Deliver, BasicProperties, bytes], None
            ]
    ):
        """
            params for callback
            ch: BlockingChannel
            method: Basic.Deliver
            properties: BasicProperties
            body: bytes
        """
        self.channel.basic_consume(queue=queue, on_message_callback=callback, auto_ack=True)

        self.channel.start_consuming()
