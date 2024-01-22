import json

from Configuration.config import INDENT, ENCODING_TYPE
from DataAccess.Contexts.FileDataContext import FileDataContext


class DefaultFileDataInitializer:
    @staticmethod
    def initializer(context: FileDataContext, default_file_data_path: str) -> None:
        with open(context.path, "w", encoding=ENCODING_TYPE) as file:
            json.dump(DefaultFileDataInitializer.__get_test_data(default_file_data_path), file, indent=INDENT)

    @staticmethod
    def __get_test_data(default_file_data_path: str) -> dict:
        with open(default_file_data_path, "r", encoding=ENCODING_TYPE) as file:
            return json.load(file)
