import math
from .base import Shape
from ..exceptions import NonPositiveValueError

class Circle(Shape):
    def __init__(self, radius: float):
        if not isinstance(radius, (int, float)):
            raise TypeError(f"Радиус должен быть числом, получен тип: {type(radius).__name__}.")
        if radius <= 0:
            raise NonPositiveValueError(parameter_name="radius", value=radius)
        self.radius: float = float(radius)
        
    def area(self) -> float:
        return math.pi * (self.radius ** 2)
    
    # для разработчиков вывод
    def __repr__(self) -> str:
        return f"Circle(radius={self.radius})"
        
    # для обычных пользователей
    def __str__(self) -> str:
        return f"Круг с радиусом {self.radius}"