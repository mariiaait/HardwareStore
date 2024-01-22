import json
import os

from Configuration.config import DEFAULT_MATERIALS_DICT
from Infrastructure.Validators.Decorators.FileExceptionHandlers import try_handle_log_levels


class FileDataContext:
    __instance = None
    __initialized: bool = False

    def __init__(self, path: str):
        if not self.__initialized:
            self._path = path
            self.__connect_of_default()
            FileDataContext.__initialized = True

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    @try_handle_log_levels("Connect to file")
    def __connect_of_default(self) -> None:
        if not os.path.exists(self._path):
            with open(self._path, "w") as file:
                json.dump(DEFAULT_MATERIALS_DICT, file)

    @property
    def path(self) -> str:
        return self._path

    def __repr__(self) -> str:
        return f"{self.__class__}:{self._path}"
