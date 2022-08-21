from api.rabbitmq import RabbitMQClient


class MessageConsumer(RabbitMQClient):
    def declare_queue(self, queue_name):
        self.channel.queue_declare(queue=queue_name)

    def send_message(self, exchange, routing_key, body):
        channel = self.connection.channel()
        channel.basic_publish(
            exchange=exchange,
            routing_key=routing_key,
            body=body
        )
