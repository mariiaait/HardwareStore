from Configuration.config import MATERIAL_ID, MATERIAL_NAME, MATERIAL_PRICE
from DataAccess.Domains import Material


def converting_data_material_to_json(func):
    def wrapper(*args, **kwargs):
        material = None
        for arg in args:
            if isinstance(arg, Material):
                material = arg
                break

        if material is not None:
            data_to_json = {
                MATERIAL_ID: material.id,
                MATERIAL_NAME: material.name,
                MATERIAL_PRICE: material.price
            }
            return func(data_to_json, **kwargs)
        else:
            raise ValueError("Type 'Material' is not found.")

    return wrapper