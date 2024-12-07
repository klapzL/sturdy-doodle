from asyncio import AbstractEventLoop

from aio_pika import connect_robust
from aio_pika.abc import AbstractRobustConnection

from src.config.settings import settings


async def get_connection(loop: AbstractEventLoop) -> AbstractRobustConnection:
    return await connect_robust(url=settings.RMQ_URL, loop=loop)
