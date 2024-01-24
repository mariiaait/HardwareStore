import json
import logging
from typing import Callable

from Presentation.Response.DataResponse import DataResponse

logger = logging.basicConfig(filename='RELATIVE_PATH_TO_LOG_FILE', format='%(asctime)s - %(levelname)s - %(message)s')


def try_handle_log_levels(log_mes: str) -> Callable:
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> DataResponse:
            try:
                result = func(*args, **kwargs)
                logging.info(f"INFO: {log_mes}\tValues: {args}, {kwargs}")
                if func.__name__ not in ("add", "update", "delete"):
                    return DataResponse(True, result, None)
            except (FileNotFoundError, json.JSONDecodeError, Exception) as ex:
                logging.error(f"ERROR: {ex}\tValues: {args}, {kwargs}")
                return DataResponse(False, None, ex)
        return wrapper

    return decorator
