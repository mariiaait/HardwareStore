import os

from Configuration.config import RELATIVE_PATH_TO_SYSTEM_ID_FILE, START_MATERIAL_ID_VALUE


class MaterialFileIdBuilder:
    @staticmethod
    def build_id():
        material_id = START_MATERIAL_ID_VALUE
        if not os.path.exists(RELATIVE_PATH_TO_SYSTEM_ID_FILE):
            with open(RELATIVE_PATH_TO_SYSTEM_ID_FILE, "w") as file:
                file.write(f"{material_id}\n")
        else:
            with open(RELATIVE_PATH_TO_SYSTEM_ID_FILE, "a+") as file:
                file.seek(0)
                lines = file.readlines()
                last_data = lines[-1].strip()
                if last_data.isdigit():
                    material_id = int(last_data)
                    material_id += 1
                    file.write(f"{material_id}\n")
                else:
                    raise ValueError("Id is not a digit")
        return material_id
