import logging
from typing import Callable

from Configuration.config import RELATIVE_PATH_TO_LOG_FILE, CRITICAL_EXIT_CODE
from Presentation.Response.DataResponse import DataResponse

logging.basicConfig(filename=RELATIVE_PATH_TO_LOG_FILE, format='%(asctime)s - %(levelname)s - %(message)s')


def try_handle_log_levels_for_crud(log_mes: str) -> Callable:
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> DataResponse:
            try:
                result = func(*args, **kwargs)
                logging.info(f"{log_mes} Args: {args}, {kwargs}")
                return DataResponse(True, result, None)
            except Exception as ex:
                logging.error(f"{ex} Module: {__name__} Args: {ex.args}")
                return DataResponse(False, None, ex)

        return wrapper

    return decorator


def handle_base_exceptions(log_mes: str) -> Callable:
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                logging.info(f"{log_mes} Args: {args}, {kwargs}")
                return result
            except Exception as ex:
                logging.error(f"{ex} Module: {__name__} Args: {ex.args}")
                exit(CRITICAL_EXIT_CODE)

        return wrapper

    return decorator