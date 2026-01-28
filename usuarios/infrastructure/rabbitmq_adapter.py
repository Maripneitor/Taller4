import pika
from usuarios.domain.notificador import Notificador

class RabbitMQAdapter(Notificador):
    def __init__(self):
        try:
            self.connection = pika.BlockingConnection(
                pika.ConnectionParameters(host='rabbitmq')
            )
            self.channel = self.connection.channel()
            self.channel.queue_declare(queue='registro_usuarios')
        except Exception as e:
            print(f"Error conectando a RabbitMQ: {e}")

    def enviar_mensaje(self, mensaje: str):
        if hasattr(self, 'channel'):
            self.channel.basic_publish(
                exchange='',
                routing_key='registro_usuarios',
                body=mensaje
            )
            print(f"🐰 [RabbitMQ] Mensaje enviado: {mensaje}")
        else:
            print("⚠️ No hay conexión a RabbitMQ, mensaje no enviado.")
