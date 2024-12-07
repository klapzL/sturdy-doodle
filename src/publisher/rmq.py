import aio_pika

from config import settings
from config.rmq import get_connection


async def send_message_to_rabbitmq(message: str):
    connection = await get_connection()
    async with connection:
        channel = await connection.channel()

        await channel.default_exchange.publish(
            aio_pika.Message(body=message.encode()),
            routing_key=settings.RMQ_QUEUE,
        )
        print(f"Sent message: {message}")
