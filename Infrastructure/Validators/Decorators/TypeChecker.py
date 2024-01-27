import inspect
import logging
from typing import Callable, get_type_hints

from Configuration.config import RELATIVE_PATH_TO_LOG_FILE

logging.basicConfig(filename=RELATIVE_PATH_TO_LOG_FILE, format='%(asctime)s - %(levelname)s - %(message)s')

class TypeChecker:
    @staticmethod
    def type_check(func: Callable, *args, **kwargs):
        type_hints = get_type_hints(func)
        parameters_in_order = inspect.signature(func).parameters
        pairs = zip(parameters_in_order, args)
        TypeChecker.__check_zipped_types(type_hints, pairs)
        TypeChecker.__check_zipped_types(type_hints, kwargs.items())


    @staticmethod
    def __check_zipped_types(type_hints: dict, data):
        for parameter_name, parameter_value in data:
            parameter_type_hint = type_hints.get(parameter_name, None)
            if parameter_type_hint and not isinstance(parameter_value, parameter_type_hint):
                raise TypeError(f"Type mismatch for argument {parameter_name}. "
                                f"Expected {parameter_type_hint},got {type(parameter_value)}.")