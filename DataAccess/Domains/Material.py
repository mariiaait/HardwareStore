class Material:
    '''Material class description'''
    __id: int = 0

    def __init__(self, name: str, price: float):
        self._name: str = name
        self._price: float = price
        self.__id: int = Material.set_id()

    @property
    def name(self) -> str:
        return self._name

    @property
    def price(self) -> float:
        return self._price

    @property
    def id(self) -> int:
        return self.__id

    @classmethod
    def set_id(cls) -> int:
        cls.__id += 1
        return cls.__id

    def __setattr__(self, key, value):
        types_dict = {'__id': int, '_name': str, '_price': float}
        if key not in types_dict:
            raise AttributeError('Attribute was not found')

        if not isinstance(value, (types_dict[key])):
            raise TypeError('Incorrect data type')

        object.__setattr__(self, key, value)


