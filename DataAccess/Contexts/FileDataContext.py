import os
class FileDataContext:
    __instance = None
    __initialized = False

    def __init__(self, path):
        if not self.__initialized:
            self._path = path
            self.__connect()
            FileDataContext.__initialized = True

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __connect_or_default(self):
        if not os.path.exists(self._path):
            with open(self._path, "w") as _: #In the future, change this line to constant
                pass

    @property
    def path(self):
        return self._path
