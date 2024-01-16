from DataAccess.Domains import Material


class DataJsonConverter:
    @staticmethod
    def to_json(data: Material):
        return {"id": data.id, "name": data.name, "price": data.price}
