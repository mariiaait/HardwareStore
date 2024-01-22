import json
import logging
import datetime

from typing import Callable

from Presentation.Response.DataResponse import DataResponse

logger = logging.getLogger(__name__)


def try_handle_log_levels(log_mes: str) -> Callable:
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> DataResponse:
            try:
                result = func(*args, **kwargs)
                logger.info(f"INFO: {datetime.datetime.now()}\t{log_mes}\tValues: {args}, {kwargs}")
                if func.__name__ not in ("add", "update", "delete"):
                    return DataResponse(True, result, None)
            except FileNotFoundError as ex:
                logger.error(f"ERROR: {datetime.datetime.now()}\t{ex}\tValues: {args}, {kwargs}")
                return DataResponse(False, None, ex)
            except json.JSONDecodeError as ex:
                logger.error(f"ERROR: {datetime.datetime.now()}\t{ex}\tValues: {args}, {kwargs}")
                return DataResponse(False, None, ex)
            except Exception as ex:
                logger.error(f"ERROR: {datetime.datetime.now()}\t{ex}\tValues: {args}, {kwargs}")
                return DataResponse(False, None, ex)
        return wrapper

    return decorator
