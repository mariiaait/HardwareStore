from Configuration.config import MATERIAL_ID, MATERIAL_NAME, MATERIAL_PRICE
from DataAccess.Domains import Material


class DataJsonConverter:
    """Class which convert objects Material to JSON format"""
    @staticmethod
    def to_json(data: Material):
        """Convert Material object to dictionary format"""
        return {MATERIAL_ID: data.id, MATERIAL_NAME: data.name, MATERIAL_PRICE: data.price}
