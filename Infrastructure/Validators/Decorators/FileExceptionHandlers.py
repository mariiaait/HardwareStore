import json
import logging
import datetime

logger = logging.getLogger(__name__)


def try_handle_log_levels(log_mes):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                logger.info(f"INFO: {datetime.datetime.now()}\t{log_mes}\tValues: {args}, {kwargs}")
                if func.__name__ not in ("add", "update", "delete"):
                    return result
            except FileNotFoundError as ex:
                logger.error(f"ERROR: {datetime.datetime.now()}\t{ex}\tValues: {args}, {kwargs}")
            except json.JSONDecodeError as ex:
                logger.error(f"ERROR: {datetime.datetime.now()}\t{ex}\tValues: {args}, {kwargs}")
            except Exception as ex:
                logger.error(f"ERROR: {datetime.datetime.now()}\t{ex}\tValues: {args}, {kwargs}")

        return wrapper

    return decorator
