from DataAccess.Domains import Material
def decorator(func):
    def wrapper(*args, **kwargs):
        resalt = func(*args, **kwargs)
        data_to_json = {"id": resalt.id, "name": resalt.name, "price": resalt.price}
        return data_to_json
    return wrapper
