import json

from DataAccess.Contexts.FileDataContext import FileDataContext


class DefaultFileDataInitializer:
    @staticmethod
    def initializer(context: FileDataContext, default_file_data_path: str):
        with open(context.path, "w", encoding="utf-8") as file:
            json.dump(DefaultFileDataInitializer.__get_test_data(default_file_data_path), file, indent=3)

    @staticmethod
    def __get_test_data(default_file_data_path):
        with open(default_file_data_path, "r", encoding="utf-8") as file:
            return json.load(file)
