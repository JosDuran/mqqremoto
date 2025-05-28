import pika

credenciales = pika.PlainCredentials('jose', 'soCorongo_74')
conexion = pika.BlockingConnection(
    pika.ConnectionParameters('jointocloud.com', 5672, '/', credenciales)
)

canal = conexion.channel()
canal.queue_declare(queue='mi_cola')

# Enviar mensaje
mensaje = 'Hola desde el productor!'
canal.basic_publish(exchange='',
                    routing_key='mi_cola',
                    body=mensaje)

print(f'✅ Mensaje enviado: {mensaje}')
conexion.close()
