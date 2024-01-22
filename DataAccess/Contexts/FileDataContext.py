from Infrastructure.Validators.Decorators.FileExceptionHandlers import try_handle_log_levels


class FileDataContext:
    """Class which create just one unique class object and provides access for connection to the file """
    __instance = None
    __initialized = False

    def __init__(self, path):
        """Initialisation with path and connection to database if object not exist  """
        if not self.__initialized:
            self._path = path
            self.__connect()
            FileDataContext.__initialized = True

    def __new__(cls, *args, **kwargs):
        """Creation a new object if it doesn't exist"""
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    @try_handle_log_levels("Connect to file")
    def __connect(self):
        """Connection to file"""
        with open(self._path, "w") as _:
            pass

    @property
    def path(self):
        """Get the protected path"""
        return self._path

    def __repr__(self):
        """Returning info about class and path"""
        return f"{self.__class__}:{self._path}"
