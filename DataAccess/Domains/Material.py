from Configuration.config import PROTECTED_MATERIAL_ID, PROTECTED_MATERIAL_NAME, PROTECTED_MATERIAL_PRICE
from Infrastructure.Builders.MaterialFileIdBuilder import MaterialFileIdBuilder
from Infrastructure.Validators.Decorators.ExceptionHandlers.FileExceptionHandlers import handle_base_exceptions


class Material:
    """Material class description"""

    def __init__(self, name: str, price: float, id: int = None):
        self._id: int = id if id is not None else MaterialFileIdBuilder.build_id()
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

    @handle_base_exceptions("Initializing of Material attributes")
    def __setattr__(self, key, value):
        types_dict = {PROTECTED_MATERIAL_ID: int, PROTECTED_MATERIAL_NAME: str, PROTECTED_MATERIAL_PRICE: float}
        if key not in types_dict:
            raise AttributeError('Attribute was not found')

        if not isinstance(value, (types_dict[key])):
            raise TypeError(f'Incorrect data type for {key}. Expected {types_dict[key]}, got {type(value)}')

        object.__setattr__(self, key, value)
