from Configuration.config import MATERIAL_ID, MATERIAL_NAME, MATERIAL_PRICE
from DataAccess.Domains import Material


class DataJsonConverter:
    @staticmethod
    def to_json(data: Material):
        return {MATERIAL_ID: data.id, MATERIAL_NAME: data.name, MATERIAL_PRICE: data.price}
