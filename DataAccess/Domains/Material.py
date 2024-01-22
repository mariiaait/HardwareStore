from Configuration.config import PROTECTED_MATERIAL_ID, PROTECTED_MATERIAL_NAME, PROTECTED_MATERIAL_PRICE


class Material:
    """Class which create material with automatic unique id, name and price"""
    __id: int = 0

    def __init__(self, name: str, price: float):
        """Initialize object Material with unique id, name and price
                parameters:
                            name(str): the name of the material
                            price(float): the price of the material
                            id(int): the unique id of the material
        """
        self._id: int = Material.set_id()
        self._name: str = name
        self._price: float = price

    @property
    def name(self) -> str:
        """Get the protected name of material"""
        return self._name

    @property
    def price(self) -> float:
        """Get the protected price of material"""
        return self._price

    @property
    def id(self) -> int:
        """Get the protected id of material"""
        return self._id

    @classmethod
    def set_id(cls) -> int:
        """Generating and return of unique id"""
        cls.__id += 1
        return cls.__id

    def __setattr__(self, key, value):
        """Checking correct type of id, name and price"""
        types_dict = {PROTECTED_MATERIAL_ID: int, PROTECTED_MATERIAL_NAME: str, PROTECTED_MATERIAL_PRICE: float}
        if key not in types_dict:
            raise AttributeError('Attribute was not found')

        if not isinstance(value, (types_dict[key])):
            raise TypeError('Incorrect data type')

        object.__setattr__(self, key, value)

    def __getattribute__(self, item):
        """Checking the restriction of access to protected attributes"""
        if item in (PROTECTED_MATERIAL_ID, PROTECTED_MATERIAL_NAME, PROTECTED_MATERIAL_PRICE):
            raise AttributeError(f'Access to protected attribute {item}')
        return super().__getattribute__(self, item)
