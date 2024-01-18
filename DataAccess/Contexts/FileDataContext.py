class FileDataContext:
    __instance = None
    __initialized = False

    def __init__(self, path):
        if not self.__initialized:
            self._path = path
            self.__connect()
            FileDataContaxt.__initialized = True

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    def __repr__(self):
        return f"{self.__class__}:{self._path}"

  @try_handle_log_levels("Connect to file"):
    def __connect(self):
        with open(self._path, "w") as _:
            pass

    @property
    def path(self):
        return self._path
