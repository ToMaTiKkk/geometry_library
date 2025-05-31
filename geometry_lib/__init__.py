# пакет 'geometry_lib'
from .exceptions import ShapeError, InvalidShapeParametersError, NonPositiveValueError, TriangleInequalityError
from .shapes import Shape, Circle, Triangle

__version__ = "0.0.1-dev"

# экспорт для пользователей
__all__ = [
        'Shape', 'Circle', 'Triangle',
        'ShapeError',
        'InvalidShapeParametersError',
        'NonPositiveValueError',
        'TriangleInequalityError',
        '__version__',
]