from Configuration.config import PROTECTED_MATERIAL_ID, PROTECTED_MATERIAL_NAME, PROTECTED_MATERIAL_PRICE


class Material:
    """Material class description"""
    __id: int = 0

    def __init__(self, name: str, price: float):
        self._id: int = Material.set_id()
        self._name: str = name
        self._price: float = price

    @property
    def name(self) -> str:
        return self._name

    @property
    def price(self) -> float:
        return self._price

    @property
    def id(self) -> int:
        return self._id

    @classmethod
    def set_id(cls) -> int:
        cls.__id += 1
        return cls.__id

    def __setattr__(self, key, value):
        types_dict = {PROTECTED_MATERIAL_ID: int, PROTECTED_MATERIAL_NAME: str, PROTECTED_MATERIAL_PRICE: float}
        if key not in types_dict:
            raise AttributeError('Attribute was not found')

        if not isinstance(value, (types_dict[key])):
            raise TypeError('Incorrect data type')

        object.__setattr__(self, key, value)

    def __getattribute__(self, item):
        if item in (PROTECTED_MATERIAL_ID, PROTECTED_MATERIAL_NAME, PROTECTED_MATERIAL_PRICE):
            raise AttributeError(f'Access to protected attribute {item}')
        return super().__getattribute__(self, item)
