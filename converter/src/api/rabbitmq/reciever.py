from api.rabbitmq import RabbitMQClient


class MessageReciever(RabbitMQClient):
    def get_message(self, queue):
        method_frame, header_frame, body = self.channel.basic_get(queue)
        if method_frame:
            self.channel.basic_ack(method_frame.delivery_tag)
            return method_frame, header_frame, body

    def consume_messages(self, queue):
        def callback(ch, method, properties, body):
            print(" [x] Received %r" % body)

        self.channel.basic_consume(queue=queue, on_message_callback=callback, auto_ack=True)

        self.channel.start_consuming()
