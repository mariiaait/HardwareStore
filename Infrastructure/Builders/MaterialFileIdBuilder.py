import os

from Configuration.config import RELATIVE_PATH_TO_SYSTEM_ID_FILE, START_MATERIAL_ID_VALUE
from Infrastructure.Validators.Decorators.ExceptionHandlers.FileExceptionHandlers import handle_base_exceptions


class MaterialFileIdBuilder:

    @staticmethod
    @handle_base_exceptions("Creating id for object of Material type")
    def build_id():
        material_id = START_MATERIAL_ID_VALUE
        if os.path.exists(RELATIVE_PATH_TO_SYSTEM_ID_FILE):
            with open(RELATIVE_PATH_TO_SYSTEM_ID_FILE, "r") as file:
                line = file.readline()
                last_data = line.strip()

                if last_data.isdigit():
                    material_id = int(last_data)
                    material_id += 1
                else:
                    raise ValueError("Id is not a digit")
        MaterialFileIdBuilder.__write(RELATIVE_PATH_TO_SYSTEM_ID_FILE, material_id)
        return material_id

    @staticmethod
    def __write(path, data):
        with open(path, "w") as file:
            file.write(f"{data}\n")
