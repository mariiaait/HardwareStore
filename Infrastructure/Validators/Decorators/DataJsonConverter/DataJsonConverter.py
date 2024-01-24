from Configuration.config import MATERIAL_ID, MATERIAL_NAME, MATERIAL_PRICE
from DataAccess.Domains.Material import Material


def converting_data_material_to_json(func):
    def wrapper(*args, **kwargs):
        index = 0
        material = None
        for arg in args:
            if isinstance(arg, Material):
                material = arg
            if material is not None: break
            index += 1

        if material is not None:
            data_to_json = {
                MATERIAL_ID: material.id,
                MATERIAL_NAME: material.name,
                MATERIAL_PRICE: material.price
            }
            new_args = args[0:index] + (data_to_json,) + args[index + 1:]
            return func(*new_args, **kwargs)
        else:
            raise ValueError("Type 'Material' is not found.")

    return wrapper
