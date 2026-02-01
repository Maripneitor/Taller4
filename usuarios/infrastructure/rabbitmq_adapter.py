import pika
from usuarios.domain.notificador import Notificador

class RabbitMQAdapter(Notificador):
    def __init__(self):
        # Conexión simple
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters('rabbitmq')
        )
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='registro_usuarios')

    def enviar_mensaje(self, mensaje: str):
        self.channel.basic_publish(
            exchange='',
            routing_key='registro_usuarios',
            body=mensaje
        )
