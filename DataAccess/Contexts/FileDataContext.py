class DataContext:
    __instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DataContext, cls).__new__(cls)
        return cls._instance

    # def read_data(self, filename):
    #     with open(filename, 'r') as file:
    #         data = file.read()
    #     return data
    #
    # def write_data(self, filename, data):
    #     with open(filename, 'w') as file:
    #         file.write(data)