from loguru import logger

logger.remove()

logger.add('api.log', enqueue=True)
