import logging
from settings import LOGS_MAIN



def set_logger(name: str = 'BalvaneraWebStudio') -> logging.Logger:

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler = logging.FileHandler(LOGS_MAIN, encoding='utf-8')
    file_handler.setFormatter(formatter)

    # Консоль
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    # Добавляем хендлеры (один раз!)
    if not logger.hasHandlers():
        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)


    return logger
