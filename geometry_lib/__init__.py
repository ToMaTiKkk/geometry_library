# пакет 'geometry_lib'
from .exceptions import ShapeError, InvalidShapeParametersError, NonPositiveValueError, TriangleInequalityError

__version__ = "0.0.1-dev"

# экспорт для пользователей
__all__ = [
        'ShapeError',
        'InvalidShapeParametersError',
        'NonPositiveValueError',
        'TriangleInequalityError',
        '__version__',
]