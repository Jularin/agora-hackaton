import pika

from erp_system.settings import AMQP_URL


class RabbitMQClient:
    def __init__(self):
        url = AMQP_URL
        self.parameters = pika.URLParameters(url)

    def __enter__(self):
        self.connection = pika.BlockingConnection(self.parameters)
        self.channel = self.connection.channel()

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.channel.close()
        self.connection.close()
