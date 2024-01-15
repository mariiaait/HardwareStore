class DataContext:
    __instance = None
    __initialized = False

    def __init__(self, file_path):
        if not self.__instanced:
            self._file_path = file_path
            self.__connect()
            DataContaxt.__initialized = False

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(DataContext, cls).__new__(cls)
        return cls.__instance

    def __connect(self):
    with open(self._file_path, "w") as _:
        pass

    @property
    def file_path(self):
        return self._fale_path

