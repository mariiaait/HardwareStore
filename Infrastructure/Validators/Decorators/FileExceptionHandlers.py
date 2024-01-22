import json
import logging
import datetime
from typing import Callable

logging.basicConfig(filename='example.log', format='%(asctime)s - %(levelname)s - %(message)s')


def try_handle_log_levels(log_mes: str) -> Callable:
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> dict:
            try:
                result = func(*args, **kwargs)
                logging.info(f"INFO: {datetime.datetime.now()}\t{log_mes}\tValues: {args}, {kwargs}")
                if func.__name__ not in ("add", "update", "delete"):
                    return result
            except (FileNotFoundError, json.JSONDecodeError, Exception) as ex:
                logging.error(f"ERROR: {datetime.datetime.now()}\t{ex}\tValues: {args}, {kwargs}")

        return wrapper

    return decorator
