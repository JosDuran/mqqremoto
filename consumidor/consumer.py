import pika

credenciales = pika.PlainCredentials('jose', 'soCorongo_74')
conexion = pika.BlockingConnection(
    pika.ConnectionParameters('jointocloud.com', 5672, '/', credenciales)
)

canal = conexion.channel()
canal.queue_declare(queue='mi_cola')

def callback(ch, method, properties, body):
    print(f'📩 Recibido: {body.decode()}')

canal.basic_consume(queue='mi_cola',
                    on_message_callback=callback,
                    auto_ack=True)

print('👂 Esperando mensaje...')
canal.start_consuming()
