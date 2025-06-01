# пакет 'geometry_lib'
from .exceptions import ShapeError, InvalidShapeParametersError, NonPositiveValueError, TriangleInequalityError
from .shapes import Shape, Circle, Triangle

__version__ = "0.1.0"

# фабрика экземпляров фигур
def create_shape(*args: float, **kwargs: float) -> Shape:
    num_args = len(args)
    num_kwargs = len(kwargs)
    
    if num_kwargs > 0:
        sides = ['side_a', 'side_b', 'side_c']
        if 'radius' in kwargs and num_kwargs == 1:
            return  Circle(radius=kwargs['radius'])
        elif all(k in kwargs for k in sides) and num_kwargs == 3:
            return Triangle(side_a=kwargs['side_a'], side_b=kwargs['side_b'], side_c=kwargs['side_c'])
    elif num_args > 0:
        if num_args == 1:
            return Circle(radius=args[0])
        elif num_args == 3:
            return Triangle(side_a=args[0], side_b=args[1], side_c=args[2])
    
    raise ValueError("Не удалось определить тип фигуры по аргументами. Круг: (radius) или (radius=val). Треугольник: (a,b,c) или (side_a=a,...).")

# экспорт для пользователей
__all__ = [
        'Shape', 'Circle', 'Triangle',
        'create_shape',
        'ShapeError',
        'InvalidShapeParametersError',
        'NonPositiveValueError',
        'TriangleInequalityError',
        '__version__',
]