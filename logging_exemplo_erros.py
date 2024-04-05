from loguru import logger

logger.debug("um aviso para o desenvolvedor")
logger.info("Informação importante do processo")
logger.warning("Um aviso que algo vai parar de funcionar")
logger.error("Aconteceu uma falha")
logger.critical("Aconteceu uma falha que aborta a aplicação")